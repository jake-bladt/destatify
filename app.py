import requests, bs4, re, time

def getMasterPage():
    pagedata = requests.get("https://www.baseball-reference.com/boxes/")
    return bs4.BeautifulSoup(pagedata.text, 'html.parser')
