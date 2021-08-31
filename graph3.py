import os
import requests

url = 'https://static01.nyt.com/newsgraphics/2018/03/27/fuel-economy-comparison/ce9568d54089dbe7d5516d63d0328dcbcf31cdb1/cafe-combined.csv'

proxies = {}
response = requests.get(url=url, proxies=proxies)
with open("response.csv", "wb") as f:
    f.write(response.content)