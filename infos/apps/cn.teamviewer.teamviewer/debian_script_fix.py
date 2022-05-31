
from os import remove
from os.path import join
from shutil import copytree

def do_extra(app):
    copytree(join(app.origin_extracted_path, "DEBIAN"), "DEBIAN")
    remove("DEBIAN/control")
    remove("DEBIAN/conffiles")
