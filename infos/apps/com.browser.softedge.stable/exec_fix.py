

from os import popen


def do_extra(app):
    appid = app.appid
    print(appid)
    desktop = 'opt/apps/' + appid + '/entries/applications/microsoft-edge.desktop'
    shell = "sed -i 's/Exec=\/usr\/bin\/microsoft-edge-stable/Exec=\/opt\/apps\/com.browser.softedge.stable\/files\/microsoft-edge/g' " + desktop
    popen(shell).read()
