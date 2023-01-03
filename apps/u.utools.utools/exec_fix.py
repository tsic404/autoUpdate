from os import popen

def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/utools.desktop'
    shell = "sed -i 's|Exec=/opt/uTools/utools|Exec=/opt/apps/u.utools.utools/files/utools|g' " + desktop
    popen(shell).read()