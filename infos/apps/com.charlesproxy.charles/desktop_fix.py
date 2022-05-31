import os
import shutil

def do_extra(app):
    appid = app.appid
    target_desktop = "opt/apps/" + appid + "/entries/applications/charles-proxy.desktop"
    shutil.move("opt/apps/" + appid + "/files/etc/charles-proxy.desktop", target_desktop)
    shell="sed -i 's|Exec=charles|Exec=/opt/apps/"+ appid + "/files/bin/charles|g' " + target_desktop
    os.popen(shell).read()
    
    shell="sed -i 's|Icon=*|Icon=charles-proxy|g' " + target_desktop
    os.popen(shell).read()
