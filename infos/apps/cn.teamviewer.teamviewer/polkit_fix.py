


from os import makedirs
from shutil import copy


def do_extra(app):
    appid = app.appid
    polkit_path = "opt/apps/" + appid + "/files/tv_bin/script/com.teamviewer.TeamViewer.policy"
    polkit_deepin = "opt/apps/" + appid + "/entries/polkit/actions/"
    makedirs(polkit_deepin)
    copy(polkit_path, polkit_deepin)
