
from scripts.utils import singleton
from sqlite3 import connect

@singleton
class VerDB:
    def __init__(self, config) -> None:
        self.config = config
        self.db = connect(config.ver_db, check_same_thread=False)
        create_table = '''
        CREATE TABLE IF NOT EXISTS apps
        (appid TEXT PRIMIARY KEY UNIQUE NOT NULL,
        ver TEXT NOT NULL,
        url TEXT);
        '''
        try:
            self.db.execute(create_table)
            self.db.commit()
        except:
            pass
    
    def get_ver(self, appid):
        cur = self.db.cursor()
        cur.execute("SELECT ver FROM apps WHERE appid='{appid}'".format(appid=appid))
        res = cur.fetchone()
        if res:
            return res[0]
        return ""
    
    def get_url(self, appid):
        cur = self.db.cursor()
        cur.execute("SELECT url FROM apps WHERE appid='{appid}'".format(appid=appid))
        res = cur.fetchone()
        if res:
            return res[0]
        return ""

    def set_ver_url(self, appid, ver=None, url=None):
        cur = self.db.cursor()
        cur.execute("INSERT INTO apps(appid, ver, url) VALUES ('{appid}', '{ver}', '{url}') ON CONFLICT (appid) DO UPDATE SET ver='{ver}', url = '{url}';".format(appid=appid, ver=ver, url=url))
        self.db.commit()
