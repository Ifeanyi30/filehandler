#import socket

# my_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# my_connect.connect(('data.pr4e.org', 80))
# cdm = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# my_connect.send(cdm)

#page = []
# while True:
#     data = my_connect.recv(512)
#     if (len(data) < 1) :
#         break
#   page.append(data.decode())
#     print(data.decode(), end='')
# my_connect.close()

#with open('c:/Users/Ifeanyi Eze/Documents/newpage.html', 'a') as file:

#   file.write("".join(page))
#   file.close()

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://dr-chuck.com/page2.html')

for line in fhand:
    print(line.decode().strip())