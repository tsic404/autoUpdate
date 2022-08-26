#!/bin/env python3

from os import listdir, makedirs, popen
from shutil import move, rmtree
from os.path import join, exists

from scripts.extract import Extract
from scripts.utils import Logger, copy_content, faketime_at, import_module_from, json_write, run_in
from deb_pkg_tools.control import create_control_file, load_control_file, merge_control_fields, unparse_control_fields
from deb_pkg_tools.package import build_package
    
class App:
    def __init__(self, config, app) -> None:
        self.__dict__.update(app)
        self.config = config
        self.tmpfile = None

    @property
    def appid(self):
        appid = self.meta_info.get("appid")
        assert appid is not None
        return self.meta_info.get("appid")
    
    @property
    def id(self):
        return str(self.meta_info.get("id"))
    
    @property
    def name(self):
        name = self.meta_info.get("name")
        assert name is not None
        return self.meta_info.get("name")

    @property
    def arch(self):
        arch = self.meta_info.get("arch")
        assert type(arch) is str
        return arch
    
    @property
    def info_arch(self):
        arch = self.arch
        arch_info = list()
        if arch.__eq__("all"):
            return ["amd64", "mips64", "sw_64","arm64"]
        arch_info.append(arch)
        return arch_info
    
    @property
    def permissions(self):
        permissions = self.config.default_permissions
        if self.deepin_info:
            permissions_info = self.deepin_info.get("permissions") if self.deepin_info.get("permissions") else dict()
            for i in permissions_info.keys():
                if i in permissions.keys():
                    per = permissions_info.get(i)
                    permissions.__setitem__(i, per if per else False)

        return permissions
    
    @property
    def support_plugins(self):
        support_plugins = None
        if self.deepin_info:
            support_plugins = self.deepin_info.get("support-plugins")
        return support_plugins if support_plugins else list()
    
    @property
    def plugins(self):
        plugins = None
        if self.deepin_info:
            plugins = self.deepin_info.get("plugins")
        return plugins if plugins else list()

    @property
    def info(self):
        res = dict()
        res.__setitem__("appid", self.appid)
        res.__setitem__("name", self.name)
        res.__setitem__("version", self.version)
        res.__setitem__("arch", self.info_arch)
        res.__setitem__("permissions", self.permissions)
        res.__setitem__("support-plugins", self.support_plugins)
        res.__setitem__("plugins", self.plugins)
        return res
    
    @property
    def is_deb(self):
        binary = self.build_info.get("binary")
        assert binary is not None
        return binary.get("type", "").__eq__("deb")
    
    @property
    def debian(self):
        debian_info = self.debian_info if self.debian_info is not None else dict()
        
        default_control = self.config.default_debian
        
        patched_control = {
            "Package": self.appid,
            "Version": self.version,
            "Architecture": self.arch
        }
        
        debian_patched = debian_info.get("debian_patched", None)
        if debian_patched:
            for control in debian_patched.keys():
                patched_control.__setitem__(control, debian_patched.get(control))
        
        if self.is_deb:
            if exists(self.origin_extracted_path + "/DEBIAN/control"):
                origin_control = unparse_control_fields(load_control_file(self.origin_extracted_path + "/DEBIAN/control"))
            else:
                origin_control = unparse_control_fields(load_control_file(self.package_path + "/DEBIAN/control"))
            remove_items = debian_info.get("need_remove", dict())
            for item in remove_items.keys():
                if remove_items.get(item) and origin_control.__contains__(item):
                    origin_control.__delitem__(item)

            patched_control.__setitem__("Conflicts", origin_control['Package'])
            patched_control.__setitem__("Replaces", origin_control['Package'])
            patched_control.__setitem__("Version", origin_control['Version'])
            self.version = origin_control['Version']
            patched_control = merge_control_fields(origin_control, patched_control)

        return merge_control_fields(default_control, patched_control)

    def info_write(self):
        info_path = join(self.package_path, "opt", "apps", self.appid, "info")
        json_write(info_json=self.info, target=info_path)

    def debian_write(self):
        debian_path = join(self.package_path, "DEBIAN")
        create_control_file(join(debian_path, "control"), self.debian)
    
    def debian_md5sum(self):
        shell = '''find -type f ! -regex './DEBIAN/.*' -printf '%P\n' | xargs -d '\n' md5sum > DEBIAN/md5sums'''
        with run_in(self.package_path):
            popen(shell).read()
        

    def set_content(self):
        binary = self.build_info.get("binary")
        content = binary.get("content") if  binary.get("content") else None
        if content:
            content_path = content.get("path")
            content_scripts = content.get("fix")

            if content_path:
                old_content = join(self.origin_extracted_path, content_path.strip('/'))
                new_content = join(self.package_path, "opt", "apps", self.appid, "files")
                if not exists(new_content):
                    makedirs(new_content)
                for content in listdir(old_content):
                    move(join(old_content, content), new_content)

            if type(content_scripts) is list:
                for script in content_scripts:
                    with import_module_from(self.app_conf_path, script) as extra:
                        do_extra = extra.__getattribute__(self.config.extra)
                        if do_extra:
                            with run_in(self.package_path):
                                do_extra(self)
    
    def set_entries(self):
        binary = self.build_info.get("binary")
        if binary:
            content = binary.get("content")
            if content:
                content_path = content.get("path") if content.get("path") else None
            entries = binary.get("entries") if binary.get("entries") else dict()
            for entry in entries.keys():
                new_entry_path = join(self.package_path, "opt", "apps", self.appid, "entries", entry)
                if not exists(new_entry_path):
                    makedirs(new_entry_path)
                entry_paths  = entries.get(entry).get("path") if entries.get(entry).get("path") else list()
                fix_scripts = entries.get(entry).get("fix") if entries.get(entry).get("fix") else list()

                for entry_path in entry_paths:
                    if content_path and entry_path.startswith(content_path):
                        entry_path = join(self.package_path, "opt", "apps", self.appid, "files", entry_path[len(content_path):].strip('/'))
                    else:
                        entry_path = join(self.origin_extracted_path, entry_path.strip("/"))
                    copy_content(entry_path, new_entry_path)
                
                for script in fix_scripts:
                    with import_module_from(self.app_conf_path, script) as extra:
                        do_extra = extra.__getattribute__(self.config.extra)
                        if do_extra:
                            with run_in(self.package_path):
                                do_extra(self)

    def extarct_package(self, extract: Extract):
        if not exists(self.origin_extracted_path):
            makedirs(self.origin_extracted_path)
        with run_in(self.origin_extracted_path):
            self.tmpfile, self.origin_extracted_path =(extract.extract(self.origin_file))
        
    def create_deb(self):
        with faketime_at(self.config.faketime):
            self.packaged = build_package(directory=self.package_path, repository=self.config.build_path, check_package=False, copy_files=False)
                
    def package(self):
        makedirs(self.package_path)
        self.extarct_package(Extract(Logger()))
        self.set_content()
        self.set_entries()
        self.info_write()
        self.debian_write()

        self.debian_md5sum()
        
        self.create_deb()
        
    def clean_package(self):
        if exists(self.package_path):
            rmtree(self.package_path)
        if self.tmpfile and exists(self.tmpfile):
            rmtree(self.tmpfile)

    def run(self):
        self.clean_package()
        try:
            self.package()
        except BaseException as e:
            print("build failed for " + self.appid + " because of " + str(e))
        finally:
            return
            self.clean_package()
