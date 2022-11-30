from os import popen

def do_extra(app):
    appid = app.appid
    print(appid)
    desktop = 'opt/apps/' + appid + '/entries/applications/microsoft-edge-beta.desktop'
    shell = "sed -i 's/Exec=\/usr\/bin\/microsoft-edge-beta/Exec=\/opt\/apps\/com.browser.softedge\/files\/microsoft-edge-beta/g' " + desktop
    popen(shell).read()