

from deb_pkg_tools.control import create_control_file, load_control_file, unparse_control_fields
from os.path import join


def do_extra(app):
    appid = app.appid
    if app.is_deb:
        origin_control = unparse_control_fields(load_control_file(app.origin_extracted_path + "/DEBIAN/control"))
        origin_control['Version'] = app.version
        create_control_file(join(app.origin_extracted_path, "DEBIAN/control"), origin_control)
        