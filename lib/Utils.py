from contextlib import contextmanager
from genericpath import isfile
from importlib import import_module
from os import chdir, getcwd, listdir, makedirs, popen, environ as sys_environ
from os.path import exists, basename, join
from shutil import copyfile, copytree
from time import strftime
from json import load, dumps
from yaml import safe_load as yload
import sys
from socket import AF_INET, SOCK_STREAM, socket
from string import ascii_letters


import os
import sys
import requests
from time import sleep
from tqdm import tqdm
from urllib.parse import unquote
from urllib.request import urlopen, Request


from posixpath import basename, splitext
from shutil import move, rmtree
from os import popen, listdir, remove, stat, chmod, walk,getcwd
from tempfile import mkdtemp
from os.path import join, isfile, isdir,exists
from bz2 import BZ2File
from gzip import GzipFile
from zipfile import ZipFile
from tarfile import open as taropen
from lzma import open as lzopen
from sys import argv

import yaml


def singleton(cls):
    """
    usage:
        @sigleton
        class CLASSNAME():
            pass
    """
    instance = {}

    def _singleton(*args, **kargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        return instance[cls]

    return _singleton

@contextmanager
def run_in(path):
    pwd = getcwd()
    if not exists(path):
        makedirs(path)
    chdir(path)
    yield None
    chdir(pwd)
        
@contextmanager
def faketime_at(faketime=None):
    sys_environ["LD_PRELOAD"] = '/usr/lib/x86_64-linux-gnu/faketime/libfaketime.so.1'
    sys_environ['FAKETIME'] = faketime
    yield None
    del sys_environ['FAKETIME']
    del sys_environ['LD_PRELOAD']
        
@contextmanager    
def set_stdout_to(file=sys.stdout):
    origin_stdout = sys.stdout
    sys.stdout = file
    yield None
    sys.stdout = origin_stdout

@contextmanager    
def set_stderr_to(file=sys.stderr):
    origin_stderr = sys.stderr
    sys.stderr = file
    yield None
    sys.stderr = origin_stderr

@contextmanager
def import_module_from(path, module):
    sys.path.append(path)
    try:
        yield import_module(module)
    except BaseException as e:
        print("failed to exec " + module + " because of " + str(e))
        raise e
    finally:
        sys.path.remove(path)
        sys.modules.pop(module)

@singleton
class Logger:
    def __init__(self, output=sys.stdout):
        if type(output) == str:
            self.output = open(output, "a")
        else:
            self.output = sys.stdout

    def debug(self, *msg):
        msg = strftime("%Y/%m/%d %H:%M:%S ") + str(msg)
        self.output.write("\033[0;34m%s\033[0m\n" % msg)
        self.output.flush()

    def warming(self, *msg):
        msg = strftime("%Y/%m/%d %H:%M:%S ") + str(msg)
        self.output.write("\033[0;33m%s\033[0m\n" % msg)
        self.output.flush()

    def info(self, *msg):
        msg = strftime("%Y/%m/%d %H:%M:%S ") + str(msg)
        self.output.write("\033[0;32m%s\033[0m\n" % msg)
        self.output.flush()

    def error(self, *msg):
        msg = strftime("%Y/%m/%d %H:%M:%S ") + str(msg)
        self.output.write("\033[0;31m%s\033[0m\n" % msg)
        self.output.flush()
    
    def write(self, msg):
        self.output.write(msg)
        self.output.flush()

def load_json(json_file):
    file = open(json_file)
    res = load(file)
    return res

def load_yaml(yaml_file):
    with open(yaml_file) as f:
        res = yload(f)
    return res


def json_write(info_json, target):
    target = open(target, 'w+')
    target.write(dumps(info_json, indent=4, separators=(',', ':')))
    target.write('\n')
    target.close()
    
def yaml_write(info_yaml, target):
    with open(target, "w+") as f:
        f.write(yaml.dump_all(info_yaml, indent=4))
        f.write('\n')


def ver_comp(old, new):
    if not new:
        return False
    new = new.replace('-', '.').replace(':', '.')
    old = old.replace('-', '.').replace(':', '.')
    news = new.split('.')
    olds = old.split('.')
    for i in range(0, min(len(news), len(olds))):
        try:
            n = int(news[i])
            o = int(olds[i])
        except ValueError:
            n = news[i]
            o = olds[i]
        if n > o:
            return True
        elif n < o:
            return False
    return len(news) > len(olds)


def get_ver_from_tag(tag):
    start = 0
    end = len(tag)
    # remove non-number char in left
    while start < end and (tag[start] in ascii_letters or tag[start].__eq__('-')):
        start += 1
    # return tag.strip(string.ascii_letters).strip('-').strip(string.ascii_letters)
    end = len(tag)
    # remove non-number char in right
    while end > start and (tag[end - 1] in ascii_letters or tag[end - 1].__eq__('-')):
        end = end - 1
    # print(tag[start:end])
    return tag[start:end]


def mkdirs(target):
    if not exists(target):
        makedirs(target)
    return target

def test_port(ip, port):
    with socket(AF_INET, SOCK_STREAM) as sk:
        sk.settimeout(1)
        try:
            sk.connect((ip, int(port)))
        except Exception:
            return False
        return True

def test_proxy_not_env(proxy_ip, proxy_port):
    if test_port(proxy_ip, proxy_port):
        if not sys_environ.get('https_proxy'):
            sys_environ['https_proxy'] = 'http://' + proxy_ip + ':' + proxy_port
        else:
            del sys_environ['https_proxy']
        if not sys_environ.get('htttp_proxy'):
            sys_environ['http_proxy'] = 'http://' + proxy_ip + ':' + proxy_port
        else:
            del sys_environ['http_proxy']
    else:
        if sys_environ.get('https_proxy'):
            del sys_environ['https_proxy']
        if sys_environ.get('http_proxy'):
            del sys_environ['http_proxy']

def generate_depends(sos):
    res = set()
    shell = '''apt-file search {so_name} | grep {so_name}'''
    for i in sos:
        for j in popen(shell.format(so_name=i)).readlines():
            j = j.strip('\n')
            package, file = j.split(':')
            file = file.strip(' ')
            if file.__eq__("/usr/lib/x86_64-linux-gnu/"+ i) or file.__eq__("/lib/x86_64-linux-gnu/"+ i) and not package.endswith('dbg'):
                res.add(package)
                continue
    return {"Depends" : str(res).strip('{').strip('}').replace("'", '')}

def get_extra_sos(path):
    sos = set()
    shell = "find {path} -name *.so*".format(path=path)
    for i in popen(shell).readlines():
        i = basename(i.strip('\n'))
        sos.add(i)

    shell = '''find {path} -type f -executable -exec sh -c "file '{}' | grep -q 'dynamically linked'" \; -print | xargs ldd | grep '^[^{start}]' | awk '{print $1}\''''
    shell = shell.replace('{path}', path).replace('{start}', path[0])
    needs = set()
    for i in popen(shell).readlines():
        i = basename(i.strip('\n'))
        if not i in sos:
            needs.add(i)
    return list(needs)

def copy_content(src, dest):
    for content in listdir(src):
        origin = join(src, content)
        target = join(dest, content)
        if isfile(origin):
            try:
                copyfile(origin, target)
            except FileExistsError:
                pass
        else:
            copytree(origin, target)

def get_conf(file):
    f = open(file, "r+")
    conf = yload(f)
    f.close()
    return conf

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 "
                  "Safari/537.36",
}

class Downloader:

    def __init__(self) -> None:
        self.max_try_count = 10

    def download(self, url):
        dst = str(self.getfilename(url))
        req = Request(url, headers=headers)
        # get file size
        file_size = int(urlopen(req).info().get('Content-Length', -1))
        first_byte = 0
        # get downloaded size
        if os.path.exists(dst):
            first_byte = os.path.getsize(dst)
        else:
            first_byte = 0
        if first_byte >= file_size:
            return dst
        # set Downlaod headers
        header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
        # Download progess
        pbar = tqdm(
            total=file_size, initial=first_byte, file=sys.stdout,
            unit='B', unit_scale=True, desc=dst.split(os.sep)[-1])
        req = requests.get(url, headers=header, stream=True)
        with(open(dst, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
        pbar.close()
        return dst

    def getfilename(self, url):
        filename = ''
        headers = requests.head(url).headers
        if 'Content-Disposition' in headers and headers['Content-Disposition']:
            disposition_split = headers['Content-Disposition'].split(';')
            if len(disposition_split) > 1:
                if disposition_split[1].strip().lower().startswith('filename='):
                    file_name = disposition_split[1].split('=')
                    if len(file_name) > 1:
                        filename = unquote(file_name[1]).strip('"')
        if not filename and os.path.basename(url):
            if url.__contains__('?'):
                url = url.split('?')[0]
            filename = os.path.basename(url)
        return os.path.join(os.getcwd(), filename)

    def run(self, url):
            file = None
            try_count = 0
            while not file and try_count < self.max_try_count:
                try:
                    file = self.download(url)
                except BaseException as e:
                    print(e)
                    sleep(60)
                try_count += 1
            return file

class Extract:
    def __init__(self, try_count=10) -> None:
        self.try_count = try_count

    def extract(self, file):
        file_prefix = mkdtemp(prefix=getcwd() + "/")
        extract_method_prefix = "extract_"
        try_count = 1

        try:
            while isfile(file) and try_count < self.try_count:
                filename, suffix = self.get_suffix_filename(file)
                extract_method = getattr(self, extract_method_prefix + suffix)
                path = extract_method(file, join(file_prefix, filename))
                if try_count > 1:
                    if exists(file):
                        if isfile(file):
                            remove(file)
                        else:
                            rmtree(file)
                if not path.__eq__(file):
                    file = self.get_dir(path)
                try_count += 1
        except AttributeError as e:
            print(str(e))

        if isdir(file):
            return self.get_dir(file)

    def get_dir(self, path):
        if isfile(path):
            return path
        dirs = listdir(path)
        while len(dirs) == 1 and isdir(path):
            path = join(path, dirs[0])
            if isfile(path): return path
            dirs = listdir(path)
        return path

    def get_suffix_filename(self, file):
        file = basename(file)
        filename, suffix = splitext(file)
        return filename, suffix.strip('.').lower()

    def extract_deb(self, file, extract_path):
        shell_options = "dpkg-deb -R " + file + " " + extract_path
        popen(shell_options).read()
        return extract_path

    def extract_appimage(self, file: str, extract_path):
        shell_options = "--appimage-extract"
        mode = oct(stat(file).st_mode)[-3:]
        for i in mode:
            if int(i) % 2 != 1:
                chmod(file, 0o755)
        popen(file + " " + shell_options).read()       
        extract_path = move("squashfs-root", extract_path)
        for i, j, k in walk(extract_path):
            chmod(i, 0o755)
        return extract_path

    def extract_bz2(self, file, extract_path):
        b_file = BZ2File(file)
        open(extract_path, 'wb+').write(b_file.read())
        b_file.close()
        return extract_path

    def extract_gz(self, file, extract_path):
        g_file = GzipFile(file)
        open(extract_path, 'wb+').write(g_file.read())
        g_file.close()
        return extract_path

    def extract_zip(self, file, extract_path):
        zip_file = ZipFile(file)
        for name in zip_file.namelist():
            zip_file.extract(name, extract_path)
        zip_file.close()
        return extract_path
    
    def extract_tar(self, file, extract_path):
        tar = taropen(file)
        for name in tar.getnames():
            tar.extract(name, extract_path)
        tar.close()
        return extract_path
    
    def extract_tgz(self, file, extract_path):
        with taropen(file, "r:gz") as tars:
            for tar in tars:
                tars.extract(tar.name, extract_path)
        return extract_path

    def extract_xz(self, file, extract_path):
        with lzopen(file) as lzfile:
            open(extract_path, "wb+").write(lzfile.read())
        return extract_path
    
    def extract_txz(self, file, extract_path):
        with taropen(file, "r:xz") as tars:
            for tar in tars:
                tars.extract(tar.name, extract_path)
        return extract_path
