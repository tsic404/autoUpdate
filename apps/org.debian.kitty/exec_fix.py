from os import popen
def do_extra(app):
    appid = app.appid
    desktop_path = 'opt/apps/' + appid + '/entries/applications/'
    desktops = ['kitty.desktop', 'kitty-open.desktop']
    for desktop in desktops:
        shell = "sed -i 's|Exec=kitty|Exec=/opt/apps/org.debian.kitty/files/bin/kitty|g' " + desktop_path + desktop
        popen(shell).read()
