from os import popen


def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/com.nextcloud.desktopclient.nextcloud.desktop'
    shell = "sed -i 's|Exec=nextcloud|Exec=/opt/apps/github.nextcloud.nextcloud-desktop/files/AppRun|g' " + desktop
    popen(shell).read()