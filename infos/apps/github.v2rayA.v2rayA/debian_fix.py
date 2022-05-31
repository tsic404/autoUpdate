

from shutil import copytree
from os.path import join


def do_extra(app):
    copytree(join(app.origin_extracted_path, "DEBIAN"), "DEBIAN")
