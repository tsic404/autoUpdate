
import os
from requests import get
from re import search
def check(sourceforge):
    project_name = sourceforge["project"]
    d_filename = sourceforge["d_filename"]
    url = "http://sourceforge.net/projects/{PROJECT_NAME}"
    url = url.replace("{PROJECT_NAME}" ,project_name)
    res = get(url + "/best_release.json").json()
    filename = res['platform_releases']['linux']['filename']

    dl_url = "https://sourceforge.net/projects/" + project_name + "/files" + filename + "/download"
    dl_url = get(dl_url, stream=True, allow_redirects=False).headers['Location']
    ver = search(d_filename, os.path.basename(filename)).groups()[0]
    dl_url = dl_url.split('?')[0]

    print(sourceforge['arch'], ver, dl_url)
