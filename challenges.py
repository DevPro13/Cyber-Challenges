#Challenge No. 1
s = 'map'
for x in s:
    print(chr(ord(x) if ord(x)+2 < ord('a') else  ord(x)+2 if ord(x)+2 < ord('z') else ord(x)-24 ))

##############################################################

#Challenge No. 2
import re
lines = open("garbage.txt", 'r').read()
print(''.join(re.findall('[a-z]', lines)))

##############################################################

#Challenge No. 3
import re

# def neighbours(c):
#     unfiltered = [c-3,c-2,c-1,c+1,c+2,c+3]
#     return [r for r in unfiltered if (r>-1 and r < 81)]

garbage = open("garbage.txt", "r").read()

pattern = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')

print(''.join(re.findall(pattern, garbage)))

##############################################################

#Challenge No. 4
import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
for i in range(400):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + soup.text.split(' ')[-1]
    print(soup.text)
#peak.html

##############################################################

#Challenge No. 5

import pickle
from urllib.request import urlopen

response  = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
output = pickle.load(response)

for each in output:
    print("".join([k * v for k, v in each]))
#Channel

##############################################################

#Challenge No. 6

import zipfile
index = 90052
myzip = zipfile.ZipFile('channel.zip','r')
res = b""
while(True):
    try:
        data = myzip.open(str(index)+'.txt', 'r').read()
        index = data.decode("utf-8").split(' ')[-1]
        res += myzip.getinfo(str(index)+'.txt').comment
    except:
        break
print(res.decode("utf-8"))
# 46145
# Collect the comments.
# HOCKEY

# it's in the air -> OXYGEN 

#Challenge No. 7 