import os
import shutil

def do_extra(app):
    appid = app.appid
    desktop = "opt/apps/" + appid + '/entries/applications/codium.desktop'
    desktop2 = "opt/apps/" + appid + '/entries/applications/codium-url-handler.desktop'
    shell = "sed -i 's|Exec=/usr/share/codium/codium|Exec=/opt/apps/" + appid +"/files/codium/bin/codium|g' "
    os.popen(shell + desktop).read()
    os.popen(shell + desktop2).read()
