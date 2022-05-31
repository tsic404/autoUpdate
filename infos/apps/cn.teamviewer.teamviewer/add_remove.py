

def do_extra(app):
    shell = '''
ROLLOUTFILE="/opt/apps/cn.teamviewer.teamviewer/files/rolloutfile.tv13"
[ -e $ROLLOUTFILE ] && rm $ROLLOUTFILE

true
'''
    with open("DEBIAN/prerm", "a") as f:
        f.write(shell)