

from os import makedirs
from shutil import copyfile


def do_extra(app):
    appid = app.appid
    icons_size = ["32", "48", "64", "128", "256"]
    icon_entry = "opt/apps/" + appid + "/entries/icons/hicolor/"
    for i in icons_size:
        makedirs(icon_entry + i + "x" + i + "/apps")
        copyfile("opt/apps/" + appid + '/files/bin/smartgit-' + i + '.png',
                    icon_entry + i + "x" + i + "/apps/smartgit.png")
    makedirs(icon_entry + "scalable/apps")
    copyfile("opt/apps/" + appid + "/files/bin/smartgit.svg",
                icon_entry + "scalable/apps/smartgit.svg")