# -*- coding:utf-8 -*-#
import time
from websocket import create_connection
import websocket

while 1:
	ws = websocket.WebSocket()
	ws.connect("ws://192.168.0.1:8080/xx/xxxx",header = ["Host:xxxx",
		"cookie:xxxx"])
	if ws.connected:
		print(sw.gestatus())
		print("Receiving...")
		result = ws.recv()
		print(str(result))
		ws.close()