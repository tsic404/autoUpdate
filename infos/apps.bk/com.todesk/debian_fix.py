

from shutil import copytree
from os.path import join

def do_extra(app):
    appid = app.appid
    copytree(join(app.origin_extracted_path, "DEBIAN"), join(app.package_path,"DEBIAN"))
