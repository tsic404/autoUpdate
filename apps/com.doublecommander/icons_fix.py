from os import makedirs
from shutil import copy

def do_extra(app):
    appid= app.appid
    path = "opt/apps/" + appid + "/entries/icons/hicolor/48x48/apps/"
    makedirs(path)
    copy("opt/apps/" + appid + "/files/doublecmd.png", path)
    path = "opt/apps/" + appid + "/entries/icons/hicolor/scable/apps/"
    makedirs(path)
    copy("opt/apps/" + appid + "/files/pixmaps/mainicon/dc_256.svg", path + "doublecmd.svg")