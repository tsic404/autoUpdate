from os import makedirs
from shutil import copy, rmtree

def do_extra(app):
    appid = app.appid
    icons_size = ["16", "32", "64", "128", "256", "1024"]
    for i in icons_size:
        makedirs("opt/apps/" + appid + "/entries/icons/hicolor/" + i + "x" + i + "/apps/")
        copy("opt/apps/" + appid + "/files/data/supertuxkart_" + i + ".png",
             "opt/apps/" + appid + "/entries/icons/hicolor/" + i + "x" + i + "/apps/supertuxkart.png")
    rmtree( "opt/apps/" + appid + "/entries/icons/hicolor/1024x1024/")
