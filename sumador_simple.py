#!/usr/bin/python
# -*- coding: utf-8 -*-

# Jesús Galán Barba
# Ing. en Sistemas de Telecomunicaciones

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 2024))

mySocket.listen(1)

primer_num = 'none'

try:
	while True:
		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept()
		print 'Request received:'
		peticion = recvSocket.recv(1024)
		print peticion
		try:
			num = int(peticion.split()[1][1:])
		except ValueError:
			print 'ERROR: Hay que introducir numeros! Vuelve a intentarlo...'
			recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
							"<html><body><h1>ERROR: Hay que introducir numeros! Vuelve a intentarlo...</h1>" +
							"</body></html>" +
							"\r\n")
			continue
		if primer_num == 'none':
			primer_num = num
			print 'Answering back...'
			recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
							"<html><body><h1>Me has mandado el numero " + str(primer_num) + "</h1>" +
							"<p><h1>Dame otro numero para poder hacer la suma!</h1></p>" +
							"</body></html>" +
							"\r\n")
		else:
			suma = primer_num + num
			print 'Answering back...'
			recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
							"<html><body><h1>Primero me has mandado el numero " + str(primer_num) + "</h1>" +
							"<p><h1>Luego me has mandado el numero " + str(num) + "</h1></p>" +
							"<p><h1>Y la suma de " + str(primer_num) + " + " + str(num) +
							" es " + str(suma) + "</h1></p>" +
							"</body></html>" +
							"\r\n")
			primer_num = 'none'

		recvSocket.close()

except KeyboardInterrupt:
	print "Closing binded socket"
	mySocket.close()
