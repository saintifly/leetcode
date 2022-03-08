# -*- coding:utf-8 -*-#
import time
from websocket import create_connection
import websocket
'''
要同时安装websocket 和websocket-client两个库
'''
while 1:
	ws = websocket.WebSocket()
	ws.connect("ws://192.168.0.1:8080/xx/xxxx",header = ["Host:xxxx",
		"cookie:xxxx"])
	if ws.connected:
		print(sw.gestatus())
		print("Receiving...")
		result = ws.recv()
		print(str(result)) ##转换字符串很重要，否则会报错
		ws.close()