from os import listdir
from os.path import join,isfile
from shutil import copyfile, copytree

def do_extra(app):
    appid = app.appid
    content = 'opt/apps/' + appid + '/files/'
    icons_path = 'opt/apps/' + appid + '/entries/icons'
    copy_content(content + "/usr/share/icons", icons_path)

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
