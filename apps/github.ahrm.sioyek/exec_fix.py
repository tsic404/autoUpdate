from os import popen
def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/sioyek.desktop'
    shell = "sed -i 's|Exec=sioyek|Exec=/opt/apps/github.ahrm.sioyek/files/bin/sioyek|g' " + desktop
    popen(shell).read()