
def do_extra(app):
    with open("DEBIAN/prerm", "a") as prerm:
        prerm.write('''
[ -f /opt/apps/com.todesk/files/config/todeskd.conf ] && rm /opt/apps/com.todesk/files/config/todeskd.conf

''')