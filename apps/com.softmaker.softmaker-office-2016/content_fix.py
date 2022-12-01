from os import listdir
from os.path import join, exists
from os import makedirs
from shutil import move


def do_extra(app):
    contents = listdir(join(app.originContentPath, "usr/share/"))
    new_content = join(app.package_path, "opt", "apps", app.appid)
    old_content = join(app.originContentPath, "usr/share/office2021")
    for i in contents:
        if i.startswith("office"):
            old_content = join(app.originContentPath, "usr/share/", i)
    if not exists(new_content):
        makedirs(new_content)
    move(old_content, join(new_content, "files"))