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
