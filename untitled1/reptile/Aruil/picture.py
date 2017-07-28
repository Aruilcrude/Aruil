import urllib.request
import os

def download(xue = 'lenx',pase = 10):
    os.mkdir(xue)
    os.chdir(xue)
    url = ''