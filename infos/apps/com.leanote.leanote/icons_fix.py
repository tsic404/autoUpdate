
from os import makedirs
from shutil import move

def do_extra(app):
    appid = app.appid
    makedirs("opt/apps/" + appid + "/entries/icons//hicolor/512x512/apps/")
    move("opt/apps/" + appid + "/files/leanote.png",
         "opt/apps/" + appid + "/entries/icons//hicolor/512x512/apps/leanote.png")
