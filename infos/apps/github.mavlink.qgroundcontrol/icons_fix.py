
from os import makedirs
from shutil import copyfile

def do_extra(app):
    appid = app.appid
    icon_file = "opt/apps/github.mavlink.qgroundcontrol/files/qgroundcontrol.png"
    makedirs("opt/apps/" + appid + "/entries/icons/hicolor/128x128/apps/")
    copyfile(icon_file, "opt/apps/" + appid + "/entries/icons/hicolor/128x128/apps/qgroundcontrol.png")