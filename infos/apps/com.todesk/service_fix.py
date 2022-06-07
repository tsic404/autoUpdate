
from os import makedirs, popen
from os.path import join
from shutil import move

def do_extra(app):
    appid = app.appid
    move(join(app.origin_extracted_path, "etc"), join(app.package_path, "opt/apps/" + appid + "/files/etc"))
    shell = "sed -i 's|/opt/todesk/|/opt/apps/"+ appid + "/files/|g' "
    popen(shell + "opt/apps/" + appid + "/files/etc/systemd/system/todeskd.service").read()
    makedirs("etc/systemd/system/")
    popen("ln -sf ../../../opt/apps/" + appid + "/files/etc/systemd/system/todeskd.service etc/systemd/system/todeskd.service").read()
    