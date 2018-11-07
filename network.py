import urllib3 file = urllib3.urlopen('http://helloworldbook2.com/data/message.txt')
message = file.read()
print message