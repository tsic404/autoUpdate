from os import popen

def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/Mailspring.desktop'
    shell = "sed -i 's|Exec=mailspring|Exec=/opt/apps/" + appid + "/files/mailspring|g' " + desktop
    popen(shell).read()
