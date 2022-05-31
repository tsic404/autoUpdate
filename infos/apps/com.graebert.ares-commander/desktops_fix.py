from os import popen
from shutil import copyfile

def do_extra(app):
    appid = app.appid
    desktop_paths = "opt/apps/" + appid + "/files/Resources/"
    desktop_entries = "opt/apps/" + appid + "/entries/applications/"
    desktops = ["graebert-gmbh_ares-commander.desktop","graebert-gmbh_ares-commander-scheme.desktop"]
    for i in desktops:
        copyfile(desktop_paths + i, desktop_entries + i)
        shell = "sed -i 's|/opt/graebert-gmbh/ARES-Commander-2022/|/opt/apps/" + appid + "/files/|g' " + desktop_entries + i
        popen(shell).read()
