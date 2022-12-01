from os import listdir
from os.path import join, exists
from os import makedirs
from shutil import move

def do_extra(app):
    content = listdir(join(app.originContentPath, "opt/graebert-gmbh"))[0]
    new_content = join(app.package_path, "opt", "apps", app.appid)
    old_content = join(app.originContentPath, "opt/graebert-gmbh", content)
    if not exists(new_content):
        makedirs(new_content)
    move(old_content, join(new_content, "files"))
