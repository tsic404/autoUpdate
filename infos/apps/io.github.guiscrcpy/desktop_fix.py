import os
import shutil

def do_extra(app):
    appid = app.appid
    applications_path ='opt/apps/' + appid + '/entries/applications/'
    desktop = 'opt/apps/' + appid + '/entries/applications/guiscrcpy.desktop'
    shutil.copy('opt/apps/' + appid  + "/files/guiscrcpy.desktop", desktop)
    shell = "sed -i 's|Exec=guiscrcpy|Exec=/opt/apps/" + appid + "/files/AppRun|g' " + desktop
    os.popen(shell).read()
