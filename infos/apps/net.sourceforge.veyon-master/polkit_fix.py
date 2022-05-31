

from os import makedirs, popen


def do_extra(app):
    appid = app.appid
    makedirs("usr/share/polkit-1/actions/")
    popen("ln -sf ../../../../opt/apps/" + appid + "/files/share/polkit-1/actions/io.veyon.veyon-configurator.policy usr/share/polkit-1/actions/io.veyon.veyon-configurator.policy").read()
    popen("sed -i 's|/usr/bin/veyon-configurator|/opt/apps/" + appid + "/files/usr/bin/veyon-configurator|g' opt/apps/" + appid + "/files/share/polkit-1/actions/io.veyon.veyon-configurator.policy").read()
    