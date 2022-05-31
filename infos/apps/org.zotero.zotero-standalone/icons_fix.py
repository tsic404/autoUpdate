
from os import makedirs
from shutil import copyfile


def do_extra(app):
    appid=app.appid
    sizes = ["16", "32", "48", "256"]
    for i in sizes:
        makedirs("opt/apps/" + appid + "/files/entries/icons/hicolor/" + i + "x" +i + "/apps/")
        copyfile("opt/apps/" + appid + "/files/chrome/icons/default/default" + i + ".png",
                    "opt/apps/" + appid + "/files/entries/icons/hicolor/" + i + "x" +i + "/apps/zotero.png")
