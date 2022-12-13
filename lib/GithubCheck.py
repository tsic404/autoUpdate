#!/usr/bin/env python3
from os import environ
from string import ascii_letters
from requests import get

headers = {}
headers['Authorization'] = environ['GITHUB_TOKEN']

def check(github, arch):
    github_url = "https://api.github.com/repos/{author}/{project}/releases"
    github_url = github_url.replace("{author}", github['author']).replace("{project}", github['project'])
    json_data = get(github_url, headers).json()
    url, ver = get_latest(json_data, github['suffix'], github['prefix'])
    print(arch, ver, url)

def get_latest(json, suffix, prefix):
    url = ""
    res = json[0]
    for i in json:
        if url.__eq__("") or ver_comp(get_ver_from_tag(res['tag_name']), get_ver_from_tag(i['tag_name'])):
            for asset in i['assets']:
                if asset['name'].endswith(suffix) and asset['name'].startswith(prefix):
                    url = asset['browser_download_url']
                    res = i
    return url, get_ver_from_tag(res['tag_name'])

def ver_comp(old, new):
    if not new:
        return False
    new = new.replace('-', '.').replace(':', '.')
    old = old.replace('-', '.').replace(':', '.')
    news = new.split('.')
    olds = old.split('.')
    for i in range(0, min(len(news), len(olds))):
        try:
            n = int(news[i])
            o = int(olds[i])
        except ValueError:
            n = news[i]
            o = olds[i]
        if n > o:
            return True
        elif n < o:
            return False
    return len(news) > len(olds)

def get_ver_from_tag(tag):
    start = 0
    end = len(tag)
    # remove non-number char in left
    while start < end and (tag[start] in ascii_letters or tag[start].__eq__('-')):
        start += 1
    # return tag.strip(string.ascii_letters).strip('-').strip(string.ascii_letters)
    end = len(tag)
    # remove non-number char in right
    while end > start and (tag[end - 1] in ascii_letters or tag[end - 1].__eq__('-')):
        end = end - 1
    # print(tag[start:end])
    return tag[start:end]
