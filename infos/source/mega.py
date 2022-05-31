

# from info import AbsSource
# from json import dumps, loads
# from yaml import full_load as yloads

# def strip_non_ascii(string):
#     stripped = (c for c in string if 0 < ord(c) < 127)
#     return ''.join(stripped)


# class Source(AbsSource):

#     def check(self):
#         d_url ="https://mega.nz/linux/repo/"
#         url = "https://sg.static.mega.co.nz/cms/sync/sync"
#         json = self.get_text_by_url(url)
#         st = json.find("sync")
#         data = loads(json[st + 4:])
#         for i in data:
#             if i.get('name').__contains__("Debian 10"):
#                 d_url = d_url + i['64']
#         print(d_url)

from infos.source.github import Source as source

class Source(source):

    def check(self):
        url , ver = super().check()
        return "https://mega.nz/linux/repo/Debian_10.0/amd64/megasync-Debian_10.0_amd64.deb", ver.strip('_')
