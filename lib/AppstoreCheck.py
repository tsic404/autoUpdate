#!/usr/bin/env python3

from time import sleep
from os.path import getsize
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from requests import get
from subprocess import run
from pyautogui import press
from requests import delete

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 "
                  "Safari/537.36",
    "referer": "https://appstore-dev.uniontech.com/",
}

class Appstore:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.cookies = None

    def _login(self):
        ops = webdriver.ChromeOptions()
        # ops.add_argument("--headless")
        
        login_url = "https://appstore-dev.uniontech.com/"
        driver = webdriver.Chrome(options=ops)
        driver.get(login_url)

        username_xpath= "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/div[2]/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input"
        username_input = driver.find_element(by=By.XPATH, value = username_xpath)
        username_input.send_keys(self.username)
        
        password_xpath = "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/div[2]/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input"
        password_input = driver.find_element(by=By.XPATH, value = password_xpath)
        password_input.send_keys(self.password)
        
        login_btn_xpath = "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/button"
        login_btn = driver.find_element(by=By.XPATH, value = login_btn_xpath)
        login_btn.click()

        sleep(3)
        
        cookies = {}
        for c in driver.get_cookies():
            cookies[c['name']] = c['value']
        
        self.cookies = cookies
    
    def __check(self):
        if (self.cookies == None):
            self._login()
    
    def __search(self, appid: str) -> dict:
        self.__check()
        search_url = "https://appstore-dev.uniontech.com/devprod-api/store-dev-app/app"
        res = get(url= search_url, params= {
            "pageNum": 1,
            "pageSize": 10,
            "name_or_app_id": appid
        },cookies=self.cookies, headers=headers).json()
        if 200 == res['code']:
            return res.get('rows')[0]
        return {}

    def search(self, appid: str) -> dict:
        return self.__search(appid=appid)
    
    def __getAppVersion(self, id: str, systemStr: str = "社区版", arch: str = "X86"):
        self.__check()
        allSystemStr = "0"
        detail_url = "https://appstore-dev.uniontech.com/devprod-api/store-dev-app/app/{id}/detail".format(id=id)
        res = get(url=detail_url, headers=headers, cookies=self.cookies).json()
        if 200 == res.get('status'):
            orin_pks = res.get("datas").get("app_origin_pkgs")
            for i in orin_pks:
                if systemStr in i['systemStr'] or allSystemStr in i['supSys']:
                    if i.get('pkgArch').__eq__(arch):
                        return(i['pkg_name'], i['pkgArch'], i['pkg_version'])
        raise BaseException("failed to get ver info from app store")
    
    def __getappDetial(self, appid):
        self.__check()
        detail_url = "https://appstore-dev.uniontech.com/devprod-api/store-dev-app/app/{id}/detail".format(id=id)
        res = get(url=detail_url, headers=headers, cookies=self.cookies).json()
        return res.get("datas", {})
    
    def __getappUpdateButton(self, appid, arch):
        "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[9]/div/button[2]"
        self.__check()
        appDetial = self.__getappDetial(appid=appid)
        for pkg in appDetial.get("app_origin_pkgs"):
            pass
        pass

    def get_all_systemStr(self, app_id: str):
        self.__check()
        app_info = self.__search(appid=app_id)
        commnuitySystemStr = "社区版"
        allSystemStr = "0"
        detail_url = "https://appstore-dev.uniontech.com/devprod-api/store-dev-app/app/{id}/detail".format(id=app_info['id'])
        res = get(url=detail_url, headers=headers, cookies=self.cookies).json()
        if 200 == res['status']:
            orin_pks = res.get("datas").get("app_origin_pkgs")
            count = 0
            for i in orin_pks:
                count +=1
                if commnuitySystemStr in i['systemStr'] or allSystemStr in i['supSys']:
                    return str(i['systemStr']).strip('[]')
    
    def getVersion(self, appid: str, systemStr: str = "社区版", arch: str = "X86"):
        info = self.__search(appid=appid)
        if arch.__eq__("amd64"): arch = "X86"
        arch = arch.upper()
        appid, arch, ver = self.__getAppVersion(id=str(info.get("id")), systemStr=systemStr, arch=arch)
        return (appid, arch, ver)
    
    def isNeedUpdate(self, appid: str, newVer: str, arch: str = "X86", systemStr: str = "社区版"):
        oldVer = None
        count = 0
        while not oldVer and count < 10:
            try:
                appid, arch, oldVer = self.getVersion(appid=appid, arch=arch, systemStr=systemStr)
            except:
                count += 1
                sleep(10)
        if oldVer is None:
            raise BaseException("failed to get ver info from app store")
        # new ver is more than old ver
        print("app: " + appid, "verion in AppStore: " + oldVer, "version in upstream: " + newVer)
        res = run(["dpkg", "--compare-versions", newVer, "gt", oldVer])
        return res.returncode == 0

    def uploadUpdate(self, appid: str, file: str):

        ops = webdriver.ChromeOptions()
        #ops.add_argument("--headless")
        ops.add_argument('--disable-infobars')
        ops.add_argument('--disable-dev-shm-usage')
        ops.add_argument('--no-sandbox')
        ops.add_argument('--remote-debugging-port=9222')

        login_url = "https://appstore-dev.uniontech.com/"
        driver = webdriver.Chrome(options=ops)
        driver.get(login_url)

        username_xpath= "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/div[2]/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input"
        username_input = driver.find_element(by=By.XPATH, value = username_xpath)
        username_input.send_keys(self.username)
        
        password_xpath = "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/div[2]/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input"
        password_input = driver.find_element(by=By.XPATH, value = password_xpath)
        password_input.send_keys(self.password)
        
        login_btn_xpath = "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/button"
        login_btn = driver.find_element(by=By.XPATH, value = login_btn_xpath)
        login_btn.click()
        sleep(3)

        if not self.cookies:
            cookies = {}
            for c in driver.get_cookies():
                cookies[c['name']] = c['value']
            self.cookies = cookies

        info = self.__search(appid=appid)
        print(info)
        if (info.get("status", 0) == 52):
            revoke_api = "https://appstore-dev.uniontech.com/devprod-api/store-dev-app/app/{id}/revoke".format(id=info.get("id"))
            res = delete(url=revoke_api,cookies=self.cookies, headers=headers).json()
            if res.get("status"):
                print(res.get("desc"))

        upload_page_url = "https://appstore-dev.uniontech.com/#/management-detial?id={id}&type=1&app_id={appid}".format(id=info.get("id"), appid=appid)
        driver.get(upload_page_url)
        sleep(3)

        update_button_xpath = "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div[4]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[9]/div/button[2]"
        update_button = driver.find_element(by=By.XPATH, value=update_button_xpath)
        update_button.click()

        upload_xpath = "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div[4]/div[1]/div[1]/div/label[2]/input"
        upload = driver.find_element(by=By.XPATH, value=upload_xpath)
        upload.send_keys(file)
        press('enter')
        press('enter')
        press('enter')
        press('enter')
        sleep(5)
        
        # begin upload
        try:
            staus_xpth =  "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div[4]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[4]/div/div/div/div[2]"
            process_bar = WebDriverWait(driver=driver, timeout=300).until(
                EC.element_to_be_clickable((By.XPATH, staus_xpth))
            )
            while process_bar.text != "100%":
                print(process_bar.text)
                sleep(5)
        except TimeoutException:
            size = getsize(file)
            sleep(int(size / 350000))
            print("failed to get upload process bar, sleep " + str(int(size / 350000)))

        developer_name_xpath="/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[3]/div/div[2]/div/div[2]/div/div[7]/div/div/input"
        developer_name_input = driver.find_element(by=By.XPATH, value=developer_name_xpath)
        developer_name_input.clear()
        developer_name_input.send_keys("开源社区中心")

        # submit upload
        submit = WebDriverWait(driver=driver, timeout=12).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/div[1]/button[3]"))
        )
        sleep(3)
        submit.click()
        sleep(3)
        driver.close()
