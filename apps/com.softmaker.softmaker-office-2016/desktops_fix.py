from os import popen

def do_extra(app):
    appid = app.appid
    icon_shell = "sed -i 's|Icon=application-x-pml21|Icon=pml|g' opt/apps/" + appid + "/entries/applications/planmaker-2021.desktop"
    exec_shell = "sed -i 's|Exec=/usr/bin/planmaker21|Exec=/opt/apps/" + appid + "/files/planmaker|g' opt/apps/" + appid + "/entries/applications/planmaker-2021.desktop"
    path_shell = "sed -i 's|Path=/usr/share/office2021|Path=/opt/apps/" + appid + "/files/|g' opt/apps/" + appid + "/entries/applications/planmaker-2021.desktop"
    popen(exec_shell).read()
    popen(icon_shell).read()
    popen(path_shell).read()
    icon_shell = "sed -i 's|Icon=application-x-prl21|Icon=prl|g' opt/apps/" + appid + "/entries/applications/presentations-2021.desktop"
    exec_shell = "sed -i 's|Exec=/usr/bin/presentations21|Exec=/opt/apps/" + appid + "/files/presentations|g' opt/apps/" + appid + "/entries/applications/presentations-2021.desktop"
    path_shell = "sed -i 's|Path=/usr/share/office2021|Path=/opt/apps/" + appid + "/files/|g' opt/apps/" + appid + "/entries/applications/presentations-2021.desktop"
    popen(exec_shell).read()
    popen(icon_shell).read()
    popen(path_shell).read()
    icon_shell = "sed -i 's|Icon=application-x-tml21|Icon=tml|g' opt/apps/" + appid + "/entries/applications/textmaker-2021.desktop"
    exec_shell = "sed -i 's|Exec=/usr/bin/textmaker21|Exec=/opt/apps/" + appid + "/files/textmaker|g' opt/apps/" + appid + "/entries/applications/textmaker-2021.desktop"
    path_shell = "sed -i 's|Path=/usr/share/office2021|Path=/opt/apps/" + appid + "/files/|g' opt/apps/" + appid + "/entries/applications/textmaker-2021.desktop"
    popen(exec_shell).read()
    popen(icon_shell).read()
    popen(path_shell).read()