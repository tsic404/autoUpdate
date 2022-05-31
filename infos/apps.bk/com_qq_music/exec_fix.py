import os
import shutil

def do_extra(info):
    appid = info['meta']['appid']
    desktop = "opt/apps/" + appid + '/entries/applications/qqmusic.desktop'
    shell = "sed -i 's|Exec=/opt/qqmusic/qqmusic|Exec=/opt/apps/" + appid +"/files/qqmusic|g' "
    os.popen(shell + desktop).read()
