
from os import makedirs, popen
from os.path import join
from shutil import move

def do_extra(app):
    appid = app.appid
    move(join(app.origin_extracted_path, "etc"), "opt/apps/" + appid + "/files/etc")
    makedirs("etc/sysctl.d/")
    makedirs("etc/udev/rules.d")
    popen("ln -sf ../../opt/apps/" + appid + "/files/etc/sysctl.d/99-megasync-inotify-limit.conf etc/sysctl.d/99-megasync-inotify-limit.conf").read()
    popen("ln -sf ../../../opt/apps/" + appid + "/files/etc/udev/rules.d/99-megasync-udev.rules etc/udev/rules.d/99-megasync-udev.rules").read()
