import os
import shutil

def do_extra(app):
    appid = app.appid
    shutil.copy("opt/apps/" + appid + "/files/liteide.desktop",
                "opt/apps/" + appid + "/entries/applications/liteide.desktop")

    desktop = 'opt/apps/' + appid + '/entries/applications/liteide.desktop'
    shell = "sed -i 's|Exec=liteide|Exec=/opt/apps/" + appid + "/files/AppRun|g' " + desktop
    os.popen(shell).read()
