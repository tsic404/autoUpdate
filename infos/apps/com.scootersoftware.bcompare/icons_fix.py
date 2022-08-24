
import os
import shutil

def do_extra(app):
    app_id = app.appid
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/48x48/apps")
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/16x16/apps")
    
    shutil.copyfile("opt/apps/" + app_id + "/files/share/pixmaps/bcomparefull32.png",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/16x16/apps/bcomparefull32.png")
    
    shutil.copyfile("opt/apps/" + app_id + "/files/share/pixmaps/bcompare.png",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/48x48/apps/bcompare.png")

    shutil.copyfile("opt/apps/" + app_id + "/files/share/pixmaps/bcomparehalf32.png",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/16x16/apps/bcomparehalf32.png")
    
