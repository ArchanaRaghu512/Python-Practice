'''
 Program:to retrive data into text file
 Author:Archana

'''

from urllib.request import urlopen

url = "https://www.fhwa.dot.gov/bridge/nbi/2016/delimited/NE16.txt"

#'wb' instead of 'w' to decode bytestream to utf 8
#f.write(urlopen('https://www.fhwa.dot.gov/bridge/nbi/2016/delimited/NE16.txt').read())

f = open('urlData.txt','wb')
urlretrive = urlopen(url)
reader = urlretrive.read()

f.write(reader)
f.close()

