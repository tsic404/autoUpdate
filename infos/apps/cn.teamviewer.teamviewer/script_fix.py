

from os import popen
from posix import listdir


def do_extra(app):
    appid = app.appid
    script_path = "opt/apps/" + appid + "/files/tv_bin/script/"
    scripts = [
        "DEBIAN/postinst",
        "DEBIAN/postrm",
        "DEBIAN/prerm",
        "DEBIAN/preinst",
        script_path + "com.teamviewer.TeamViewer.Desktop.service",
        script_path + "com.teamviewer.TeamViewer.policy",
        script_path + "com.teamviewer.TeamViewer.service",
        script_path + "teamviewer_setup",
        script_path + "teamviewerd.DEB.conf",
        script_path + "teamviewerd.RHEL.conf",
        script_path + "teamviewerd.RPM.conf",
        script_path + "teamviewerd.service",
        script_path + "teamviewerd.sysv",
        script_path + "tv-delayed-start.sh",
        script_path + "tvw_aux",
        script_path + "tvw_config",
        script_path + "tvw_daemon",
        script_path + "tvw_exec",
        script_path + "tvw_extra",
        script_path + "tvw_main",
        script_path + "tvw_profile",
        script_path + "tvw_update"
    ]
    shell ="sed -i 's/\/opt\/teamviewer/\/opt\/apps\/cn.teamviewer.teamviewer\/files/g' "
    for i in scripts:
        popen(shell + i).read()
    
    shell = "sed -i 's/ConfigureUpateDEB//g' "
    popen(shell + "DEBIAN/postinst").read()


