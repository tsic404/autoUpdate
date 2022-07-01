#!/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from pyautogui import press
from requests import get
from time import sleep

from package import App

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

def get_cookie(username, password):
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    
    login_url = "https://appstore-dev.uniontech.com/"
    driver = webdriver.Chrome(options=ops)
    driver.get(login_url)

    username_xpath= "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/div[2]/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input"
    username_input = driver.find_element(by=By.XPATH, value = username_xpath)
    username_input.send_keys(username)
    
    password_xpath = "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/div[2]/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input"
    password_input = driver.find_element(by=By.XPATH, value = password_xpath)
    password_input.send_keys(password)
    
    login_btn_xpath = "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/button"
    login_btn = driver.find_element(by=By.XPATH, value = login_btn_xpath)
    login_btn.click()

    sleep(3)
    
    cookies = {}
    for c in driver.get_cookies():
        cookies[c['name']] = c['value']
    driver.close()
    
    return cookies

def get_seach(cookies: dict(), app_id: str):
    
    search_url = "https://appstore-dev.uniontech.com/devprod-api/store-dev-app/app"
    res = get(url= search_url, params= {
        "pageNum": 1,
        "pageSize": 10,
        "name_or_app_id": app_id
    },cookies=cookies, headers=headers).json()
    if 200 == res['code']:
        return res.get('rows')[0]
    return None

def get_community_count(cookies: dict(), app_id: str):
    app_info = get_seach(cookies=cookies, app_id=app_id)
    commnuitySystemStr = "社区版"
    allSystemStr = "0"
    detail_url = "https://appstore-dev.uniontech.com/devprod-api/store-dev-app/app/{id}/detail".format(id=app_info['id'])
    res = get(url=detail_url, headers=headers, cookies=cookies).json()
    if 200 == res['status']:
        orin_pks = res.get("datas").get("app_origin_pkgs")
        count = 0
        for i in orin_pks:
            count +=1
            if commnuitySystemStr in i['systemStr'] or allSystemStr in i['supSys']:
                print(i['pkg_name'], i['pkgArch'], i['pkg_version'], )
    if len(orin_pks) > 1:
        return "[{count}]".format(count=count)
    return ""

def get_all_systemStr(cookies: dict(), app_id: str):
    app_info = get_seach(cookies=cookies, app_id=app_id)
    commnuitySystemStr = "社区版"
    allSystemStr = "0"
    detail_url = "https://appstore-dev.uniontech.com/devprod-api/store-dev-app/app/{id}/detail".format(id=app_info['id'])
    res = get(url=detail_url, headers=headers, cookies=cookies).json()
    if 200 == res['status']:
        orin_pks = res.get("datas").get("app_origin_pkgs")
        count = 0
        for i in orin_pks:
            count +=1
            if commnuitySystemStr in i['systemStr'] or allSystemStr in i['supSys']:
                return i['systemStr']

def get_adapt_info(cookies: dict(), keys: list()):
    url = "https://appstore-dev.uniontech.com/devprod-api/store-dev-app/adapt-info"
    res = get(url=url, cookies=cookies, headers=headers).json()
    ret = {}
    for i in keys:
        ret[i] = res['datas'].get(i)
    return ret

def submit(app: App, file: str, username: str, password: str, developer_name="appdeveloper"):
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    
    login_url = "https://appstore-dev.uniontech.com/"
    driver = webdriver.Chrome(options=ops)
    driver.get(login_url)

    username_xpath= "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/div[2]/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input"
    username_input = WebDriverWait(driver=driver, timeout=12).until(
        EC.element_to_be_clickable((By.XPATH, username_xpath))
    )
    username_input.send_keys(username)
    
    password_xpath = "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/div[2]/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input"
    password_input = WebDriverWait(driver=driver, timeout=12).until(
        EC.element_to_be_clickable((By.XPATH, password_xpath))
    )
    password_input.send_keys(password)
    
    login_btn_xpath = "/html/body/app-root/app-login-web/div/div[2]/div[2]/form/button"    
    login_btn = WebDriverWait(driver=driver, timeout=12).until(
        EC.element_to_be_clickable((By.XPATH, login_btn_xpath))
    )
    login_btn.click()
    
    sleep(3)

    search_xpth="/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[1]/div/div[1]/input"
    search_input = WebDriverWait(driver=driver, timeout=12).until(
        EC.element_to_be_clickable((By.XPATH, search_xpth))
    )

    search_input.send_keys(app.id)
    search_input.send_keys(Keys.ENTER)

    "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/div[3]/table/tbody/tr[4]/td[9]/div/button[2]"

    sleep(3)
    try:
        app_ver_info_xpath="/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/div[3]/table/tbody/tr/td[4]/div"
        app_ver = WebDriverWait(driver=driver, timeout=12).until(
            EC.element_to_be_clickable((By.XPATH, app_ver_info_xpath))
        )
        if app_ver.text.__eq__(app.version):
            return False
        app_info_xpath="/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/div[3]/table/tbody/tr/td[9]/div/button[3]"
        app_info = WebDriverWait(driver=driver, timeout=12).until(
            EC.element_to_be_clickable((By.XPATH, app_info_xpath))
        )
        if not app_info.text.__eq__("更新"):
            raise NoSuchElementException
        app_info.send_keys(Keys.ENTER)
    except NoSuchElementException as e:
        app_info_xpath = "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/div[3]/table/tbody/tr/td[9]/div/button[5]"
        app_info = WebDriverWait(driver=driver, timeout=12).until(
            EC.element_to_be_clickable((By.XPATH, app_info_xpath))
        )
        app_info.send_keys(Keys.ENTER)

    sleep(3)
    "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[4]/div/div/div"
    "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[9]/div/button[2]"
    xpath_value = "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[9]/div/button[2]"
    update_btn = WebDriverWait(driver=driver, timeout=12).until(
        EC.element_to_be_clickable((By.XPATH, xpath_value))
    )
    update_btn.send_keys(Keys.ENTER)
    
    upload_xpath = "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div[3]/div[2]/div/label/input"
    upload = driver.find_element(by=By.XPATH, value=upload_xpath)
    upload.send_keys(file)

    press('enter')
    press('enter')
    
    sleep(5)
    
    "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[4]/div/div/div/div[2]"
    staus_xpth =  "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[4]/div/div/div/div[2]"
    process_bar = WebDriverWait(driver=driver, timeout=12).until(
        EC.element_to_be_clickable((By.XPATH, staus_xpth))
    )
    
    while process_bar.text != "100%":
        sleep(5)
    
    
    developer_name_xpath="/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/form/div[3]/div/div[2]/div/div[2]/div[1]/div[7]/div/div/input"
    developer_name_input = driver.find_element(by=By.XPATH, value=developer_name_xpath)
    developer_name_input.clear()
    developer_name_input.send_keys(developer_name)


    submit = WebDriverWait(driver=driver, timeout=12).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/section/div/div[2]/div[2]/div[1]/button[3]"))
    )
    sleep(3)
    submit.click()
    sleep(3)
    driver.close()
