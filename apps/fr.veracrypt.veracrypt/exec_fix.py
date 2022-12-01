from os import popen

def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/veracrypt.desktop'
    shell = "sed -i 's|Exec=/usr/bin/veracrypt|Exec=/opt/apps/fr.veracrypt.veracrypt/files/bin/veracrypt|g' " + desktop
    popen(shell).read()