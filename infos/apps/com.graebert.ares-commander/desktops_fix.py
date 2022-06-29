from os import popen
from shutil import copyfile

def do_extra(app):
    appid = app.appid
    desktop_paths = "opt/apps/" + appid + "/files/Resources/"
    desktop_entries = "opt/apps/" + appid + "/entries/applications/"
    desktops = ["graebert-gmbh_ares-commander.desktop","graebert-gmbh_ares-commander-scheme.desktop"]
    for i in desktops:
        copyfile(desktop_paths + i, desktop_entries + i)
        shell = "sed -i 's|" + get_path(desktop_entries + i) +"|/opt/apps/" + appid + "/files/|g' " + desktop_entries + i
        popen(shell).read()

def get_path(desktop):
    shell = "cat " + desktop + """  | grep Path=| awk -F'=' '{print $2}'"""
    res = popen(shell).read()
    return res[:-6]
    