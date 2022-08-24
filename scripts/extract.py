
from posixpath import basename, splitext
from shutil import move, rmtree
from scripts.utils import singleton
from os import popen, listdir, remove, stat, chmod, walk,getcwd
from tempfile import mkdtemp
from os.path import join, isfile, isdir,exists
from bz2 import BZ2File
from gzip import GzipFile
from zipfile import ZipFile
from tarfile import open as taropen
from lzma import open as lzopen

@singleton
class Extract:
    def __init__(self, logger, try_count=10) -> None:
        self.logger = logger
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
        except AttributeError:
            self.logger.error("can't extract" + file)
        if isdir(file):
            return file_prefix, self.get_dir(file)

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

    def extract_appimage(self, file, extract_path):
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
