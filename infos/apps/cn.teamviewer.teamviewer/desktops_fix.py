

from os import makedirs, popen
from shutil import copy


def do_extra(app):
    appid = app.appid
    desktops = ['com.teamviewer.TeamViewer.desktop',
                'teamviewer8.desktop',
                'teamviewerapi.desktop'
                ]
    pre_path = "opt/apps/" + appid + "/files/tv_bin/desktop/"
    aft_path = "opt/apps/" + appid + "/entries/applications/"
    shell = "sed -i 's/Exec=\/opt\/teamviewer\//Exec=\/opt\/apps\/cn.teamviewer.teamviewer\/files\//g' "
    for i in desktops:
        copy(pre_path + i, aft_path + i)
        popen(shell + aft_path + i).read()
