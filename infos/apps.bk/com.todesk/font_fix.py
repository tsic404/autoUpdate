

from os import listdir, makedirs, popen


def do_extra(app):
    appid = app.appid
    makedirs("usr/share/fonts/todesk/")
    fonts = listdir("opt/apps/" + appid + "/files/res/fonts/")
    for font in fonts:
        popen("ln -sf ../../../opt/apps/" + appid + "/files/res/" + font + " usr/share/fonts/todesk/").read()