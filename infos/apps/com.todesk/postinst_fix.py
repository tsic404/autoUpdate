from os import popen

def do_extra(app):
    shell = '''sed -i 's|TODESK_INSTALL_PATH=/opt/${TODESK_PACK_NAME}|TODESK_INSTALL_PATH=/opt/apps/com.todesk/files/|g' '''
    popen(shell + "DEBIAN/postinst").read()
