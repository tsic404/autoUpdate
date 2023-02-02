from os import popen, makedirs
from shutil import copyfile
def do_extra(app):
    appid = app.appid
    # makedirs("opt/apps/" + appid + "/entries/applications/")
    copyfile("opt/apps/" + appid + "/files/picgo.desktop", "opt/apps/" + appid + "/entries/applications/picgo.desktop")
    desktop = 'opt/apps/' + appid + '/entries/applications/picgo.desktop'
    shell = "sed -i 's|Exec=AppRun --no-sandbox|Exec=/opt/apps/" + appid + "/files/AppRun|g' " + desktop
    popen(shell).read()