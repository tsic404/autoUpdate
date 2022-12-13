from os import mkdir, popen

def do_extra(app):
    appid = app.appid
    popen("chmod -R 777 opt/apps/" + appid + "/files/Help").read()
    mkdir("DEBIAN")
    with open("DEBIAN/postinst", "w+") as postinst:
        postinst.write('''#!/usr/bin/env bash
[ /opt/apps/com.graebert.ares-commander/files/Help ] && chmod -R 777 /opt/apps/com.graebert.ares-commander/files/Help
''')
    
    with open("DEBIAN/prerm", "w+") as prerm:
        prerm.write('''#!/usr/bin/env bash
[ /opt/apps/com.graebert.ares-commander/files/Help ] && rm -rf /opt/apps/com.graebert.ares-commander/files/Help
''')
