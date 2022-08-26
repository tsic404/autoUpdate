# from os.path import join
from os import popen
# from shutil import move

def do_extra(app):
    appid = app.appid
    # move(join("opt/apps/" + appid + "/files", "DEBIAN"), "DEBIAN")
    popen("sed -i 's|virtualbox-6.1|org.virtualbox.virtualbox|g' DEBIAN/postinst").read()
    popen("sed -i 's|virtualbox-6.1|org.virtualbox.virtualbox|g' DEBIAN/prerm").read()
