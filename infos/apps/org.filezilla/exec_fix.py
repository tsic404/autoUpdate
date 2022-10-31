from os import popen

def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/filezilla.desktop'
    shell = "sed -i 's|Exec=filezilla|Exec=/opt/apps/" + appid +"/files/bin/filezilla|g' " + desktop
    popen(shell).read()
