from os import popen

def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/veyon-master.desktop'
    shell = "sed -i 's|Exec=/usr/bin/veyon-master|Exec=/opt/apps/" + appid +"/files/usr/bin/veyon-master|g' " + desktop
    popen(shell).read()
    desktop = 'opt/apps/' + appid + '/entries/applications/veyon-configurator.desktop'
    shell = "sed -i 's|Exec=/usr/bin/veyon-configurator|Exec=/opt/apps/" + appid +"/files/usr/bin/veyon-configurator|g' " + desktop
    popen(shell).read()
