

from os import makedirs
from shutil import copy



def do_extra(app):
    appid = app.appid
    icon_name = "TeamViewer.png"
    icons = ['16','20','24','32','48','256']
    pre_path = "opt/apps/" + appid + "/files/tv_bin/desktop/"
    aft_path = "opt/apps/" + appid + "/entries/icons/hicolor/"
    for i in icons:
        target = aft_path + i +'x' +i + "/apps/"
        makedirs(target)
        copy(pre_path + "teamviewer_" + i + ".png", target + icon_name)
