from os import popen

def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/owncloud.desktop'
    shell = "sed -i 's|Exec=owncloud|Exec=/opt/apps/" + appid +"/files/AppRun|g' " + desktop
    popen(shell).read()
