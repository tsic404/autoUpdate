

from shutil import copy
from package import App

from scripts.utils import mkdirs


def do_extra(app: App):
    appid = app.appid
    content = 'opt/apps/' + appid + '/files/'
    icons_path = 'opt/apps/' + appid + '/entries/icons/hicolor/'
    icons = ['1024']
    for i in icons:
        mkdirs(icons_path + i + 'x' + i + '/apps/')
        copy(content + '/pixmaps/com.visualstudio.code.png', icons_path + i + 'x' + i + '/apps/com.visualstudio.code.png')

