from os import makedirs, popen
from shutil import copyfile

def do_extra(app):
    appid = app.appid
    desktop_file = "session-desktop.desktop"
    desktop_entries = "opt/apps/" + appid + "/entries/applications/"
    copyfile("opt/apps/" + appid + "/files/" + desktop_file, 
                desktop_entries + desktop_file)
    shell = "sed -i 's|Exec=AppRun|Exec=/opt/apps/" + appid + "/files/AppRun|g' " + desktop_entries + desktop_file
    popen(shell).read()
