'''
From pythonchallenge.com
Not all are own-implementation
New Experience with CTF, lots of tips taken for this ^_^
Hope to improve for other challenges
'''
#Challenge No. 1
s = 'map'
print(''.join([chr(((ord(s) + 2) - ord('a')) % 26 + ord('a')) if s >= 'a' and s <= 'z' else s for s in raw]))

##############################################################

#Challenge No. 2
import re
lines = open("garbage.txt", 'r').read()
print(''.join(re.findall('[a-z]', lines)))

##############################################################

#Challenge No. 3
import re

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

##############################################################

#Challenge No. 7 
from PIL import Image
img = Image.open('oxygen.png')
pix = img.load()
w, h = img.size
m = h // 2

out = ""
c = 0
while(c<w):
    out += chr(pix[c, m][0])
    c += 7

print(out)
# .... smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121] ....
print([chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]])

##############################################################

#Challenge No. 8
import bz2
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(bz2.decompress(un.encode()))
print(bz2.decompress(pw.encode()))
#huge file

##############################################################

#Challenge No. 9
from PIL import Image, ImageDraw
first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,332,155,348,156,353,153,366,149,379,147,394,146,399]
second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,158,121,157,128,156,134,157,136,156,136]

img = Image.new('rgb', (640, 480))
draw = ImageDraw.Draw(img)
draw.polygon(first, fill='white')
draw.polygon(second, fill='white')
img.show()
#Cow ? It's a male 
#Bull

##############################################################

#Challenge No. 10
def seprate(element):
	splittedElementList = []
	splittedElement = element[0]
	for unit in element[1:]:
		if unit in splittedElement:
			splittedElement += unit
		else:
			splittedElementList.append(splittedElement)
			splittedElement = unit
	splittedElementList.append(splittedElement)
	return [(str(len(x)),x[0]) for x in splittedElementList]

a = '1'
for i in range(31):
	res = seprate(a)
	a = ''.join([(x + y) for x, y in res])
	print(len(a))

##############################################################

#Challenge No. 11
from PIL import Image

im = Image.open('cave.jpg')
w,h = im.size
white = 0,0,0
even = Image.new('RGB',[w,h], white)

offset = 0

for i in range( im.size[0] ):
    for j in range(im.size[1]):
        if i % 2 == 0 and j % 2 == 0:  
        	even.putpixel(( i, int(j) ), im.getpixel((i,j)) )

even.show()
#evil

##############################################################

#Challenge No. 12
'''
http://www.pythonchallenge.com/pc/return/evil1.jpg 5 divisions each 5
http://www.pythonchallenge.com/pc/return/evil2.jpg change this to .gfx, download file
http://www.pythonchallenge.com/pc/return/evil3.jpg
http://www.pythonchallenge.com/pc/return/evil4.jpg save and cat to get the message about bert
then,
http://www.pythonchallenge.com/pc/return/bert.html

wc evil2.gfx multiple of 5
divide the file into 5 jpg
Boom Answer !!!
'''
data = open('evil2.gfx', 'rb').read()
for i in range(5):
    open(str(i) + '.jpg', 'wb').write(data[i::5])

##############################################################

#Challenge No. 13
import xmlrpc.client
connection = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(connection.phone("Bert"))
#555-Italy

##############################################################

#Challenge No. 14

from PIL import Image

img = Image.open("wire.png")
w, h = img.size
new = Image.new("RGB", [100,100], (255,255,255))
x, y= 0, 0
state = 0 # 0 for +x 1 for -y 2 for -x 3 for +y
boundary = [99, 99, 0, 1]
for i in range(w):
    new.putpixel((x, y) ,img.getpixel((i,0)))
    if state == 0:
        x += 1
        if x == boundary[0]:
            state = 1
            boundary[0] -= 1
    elif state == 1:
        y += 1
        if y == boundary[1]:
            state = 2
            boundary[1] -= 1
    elif state == 2:
        x -= 1
        if x == boundary[2]:
            state = 3
            boundary[2] += 1 
    elif state == 3:
        y -= 1
        if y == boundary[3]:
            state = 0
            boundary[3] += 1
    
new.show()

##############################################################

#Challenge No. 15
import datetime
import calendar
for year in range(1006, 1996, 10):
    if datetime.datetime(year, 1, 26).weekday() == 0 and calendar.isleap(year):
        print(year)
    
# second youngest 1756, leap year because below Feb 29, take flower tomorrow so, Tuesday born ->  Wolfgang Amadeus Mozart

##############################################################

#Challenge No. 16
from PIL import Image, ImageChops
image = Image.open("mozart.gif")
for y in range(image.size[1]):
    box = 0, y, image.size[0], y + 1
    row = image.crop(box)
    bytes = row.tobytes()
    i = bytes.index(195)
    row = ImageChops.offset(row, -i)
    image.paste(row, box)
image.show()

##############################################################

#Challenge No. 17
import gzip, difflib
data = gzip.open("deltas.gz")
d1, d2 = [], []
for line in data:
    d1.append(line[:53].decode()+"\n")
    d2.append(line[56:].decode())

compare = difflib.Differ().compare(d1, d2)

f = open("f.png", "wb")
f1 = open("f1.png", "wb")
f2 = open("f2.png", "wb")

for line in compare:
    bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
    if line[0] == '+':
        f1.write(bs)
    elif line[0] == '-':
        f2.write(bs)
    else:
        f.write(bs)

f.close()
f1.close()
f2.close()

##############################################################

#Challenge No. 18
