

from shutil import copy
from PIL import Image
from os import remove

from Utils import mkdirs


def do_extra(app):
    appid = app.appid
    content = 'opt/apps/' + appid + '/files/'
    icons_path = 'opt/apps/' + appid + '/entries/icons/hicolor/'
    icons = [512,256,128,64,32,16]
    for i in icons:
        mkdirs(icons_path + str(i) + 'x' + str(i) + '/apps/')
        img = Image.open(content + '/pixmaps/vscode.png')
        img.thumbnail((i,i))
        img.save(icons_path + str(i) + 'x' + str(i) + '/apps/vscode.png', 'png')
    remove(content + '/pixmaps/vscode.png')
        # copy(content + '/pixmaps/com.visualstudio.code.png', icons_path + i + 'x' + i + '/apps/com.visualstudio.code.png')
