
from ntpath import join
from os import listdir, popen
from shutil import move

def do_extra(app):
    appid = app.appid
    move(join(app.origin_extracted_path, "DEBIAN"), "DEBIAN")
    files = listdir("DEBIAN")
    for i in files:
        popen("sed -i 's|/opt/emby-server|/opt/apps/" + appid +  "/files|g' " + "DEBIAN/" + i).read()
