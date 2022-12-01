from os import makedirs
from shutil import copy

def do_extra(app):
    appid = app.appid
    icon = "opt/apps/" + appid + "/files/guiscrcpy.png"
    entry_icon = "opt/apps/" + appid + "/entries/icons/hicolor/512x512/apps/"
    makedirs(entry_icon)
    copy(icon, entry_icon)
