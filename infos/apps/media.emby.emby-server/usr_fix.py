
from shutil import move
from os import makedirs, symlink
from os.path import join

def do_extra(app):
    appid = app.appid
    move(join(app.origin_extracted_path, "usr"), 
            "opt/apps/" + appid + "/files/usr")
    makedirs("lib/systemd/system/")
    symlink("../../../../opt/apps/" + appid + "/files/usr/lib/systemd/system/emby-server.service",
                "lib/systemd/system/emby-server.service")
    symlink("../../../../opt/apps/" + appid + "/files/usr/lib/systemd/system/emby-server@.service",
                "lib/systemd/system/emby-server@.service")