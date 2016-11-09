#-*-coding:utf-8-*-
import sys
from baseClass.Client import Client
from MyPixelsParser import MyPixelsParser

# server HOST and PORT#
#HOST = '104.199.218.103'
HOST = '127.0.0.1'
PORT = 9001

client = Client()
if client.connect_server(HOST, PORT) == False:
    print '서버 연결오류'
    sys.exit()

#Your AI
myAI = MyPixelsParser()

client.set_parser(myAI)

#Client Loop
client.client_run()
