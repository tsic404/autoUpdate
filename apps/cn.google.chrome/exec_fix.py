from os import popen

def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/google-chrome.desktop'
    shell = "sed -i 's|Exec=/usr/bin/google-chrome-stable|Exec=/opt/apps/cn.google.chrome/files/google-chrome|g' " + desktop
    popen(shell).read()
