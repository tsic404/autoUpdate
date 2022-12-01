import os
import shutil

def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/supertuxkart.desktop'
    shutil.copy('opt/apps/' + appid  + "/files/data/supertuxkart.desktop", desktop)
    shell = "sed -i 's|Exec=supertuxkart|Exec=/opt/apps/" + appid + "/files/run_game.sh|g' " + desktop
    os.popen(shell).read()
