from os import makedirs
from shutil import copyfile

def do_extra(app):
    appid = app.appid
    icons_path = "opt/apps/" + appid + "/files//icons/"
    icons = ["pml", "prl", "tml"]
    sizes = ["16", "24", "32", "48", "64", "128", "256", "512", "1024"]
    icon_prefix = "opt/apps/" + appid + "/entries/icons/hicolor/"
    for size in sizes:
        size_path = icon_prefix + size + 'x' + size + "/apps/"
        makedirs(size_path)
        for icon in icons:
            copyfile(icons_path + icon + "_" + size + ".png", size_path + icon + ".png")