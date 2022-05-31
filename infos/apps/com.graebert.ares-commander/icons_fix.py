

from os import listdir, makedirs
from shutil import copyfile


def do_extra(app):
    appid = app.appid
    pixmaps = "opt/apps/" + appid + "/files/Resources/pixmaps"
    sizes = listdir(pixmaps)
    for i in sizes:
        app_icon = "opt/apps/" + appid + "/entries/icons/hicolor/" + i + "/apps/"
        makedirs(app_icon)
        copyfile("opt/apps/" + appid + "/files/Resources/pixmaps/" + i + "/program.png",
                    "opt/apps/" + appid + "/entries/icons/hicolor/" + i + "/apps/graebert-gmbh.ares-commander.png")
        mimetypes_icon = "opt/apps/" + appid + "/entries/icons/hicolor/" + i + "/mimetypes/"
        makedirs(mimetypes_icon)
        copyfile("opt/apps/" + appid + "/files/Resources/pixmaps/" + i + "/file-dwg.png",
                    mimetypes_icon + "/file-dwg.png")
        copyfile("opt/apps/" + appid + "/files/Resources/pixmaps/" + i + "/file-dwt.png",
                    mimetypes_icon + "/file-dwt.png")
        copyfile("opt/apps/" + appid + "/files/Resources/pixmaps/" + i + "/file-dxf.png",
                    mimetypes_icon + "/file-dxf.png")
        copyfile("opt/apps/" + appid + "/files/Resources/pixmaps/" + i + "/file-flx.png",
                    mimetypes_icon + "/file-flx.png")
    