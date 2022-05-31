from os import popen
from shutil import copyfile

def do_extra(app):
    appid = app.appid
    desktop_entries = "opt/apps/" + appid + "/entries/applications/"
    copyfile("opt/apps/" + appid + "/files/koodo-reader.desktop", 
                desktop_entries + "koodo-reader.desktop")
    shell = "sed -i 's|Exec=AppRun --no-sandbox|Exec=/opt/apps/" + appid + "/files/AppRun|g' " + desktop_entries + "koodo-reader.desktop"
    popen(shell).read()
