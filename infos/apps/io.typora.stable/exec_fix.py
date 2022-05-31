from os import popen


def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/typora.desktop'
    shell = "sed -i 's|Exec=typora|Exec=/opt/apps/" + appid +"/files/bin/typora|g' " + desktop
    popen(shell).read()
