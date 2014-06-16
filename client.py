import socket
import sys
import utils
import connect

class infos():
	def __init__(self):
		self.team = "NONE"
		self.port = 0
		self.host = "localhost"
		self.level = 1

def receive(s):
	ret = ""
	while 42:
		dat = s.recv(1024)
		if (ord(dat[0]) != 0):
			i = 0
			while ord(dat[i]) != 0:
				ret += dat[i]
				i+= 1
		break
	return ret

def play(s):
	i = 0
	while 42:
		if i == 0:
			i = 1
			s.sendall("avance\n")
			print "j'avance\n"
			continue
		else:
			dat = receive(s)
			print dat
			if dat == "ok\n":
				s.sendall("avance\n")
			elif dat == "mort\n":
				print "DEAD"
				break
			else:
				print dat
	"""		if dat == "":
				print "UN OWEN WAS HER"
			if dat and "mort\n" in dat:
				print "mort\n"
				break
			elif dat and "ok\n" in dat:
				print "ok"
				s.sendall("avance")
				print "j'avance\n"
			elif dat and "elevation en cours\n" in dat:
				print "elevation en cours\n"
				dat = receive(s)
				print dat
			elif not dat:
				print "NO DATA ARGHFGDHFH"
				continue
			else:
				print dat """
	s.shutdown(socket.SHUT_WR)
	s.close()

if (len(sys.argv) < 5) or (len(sys.argv) > 7):
	utils.usage()
else:
	infos = infos()
	connect.init_infos(sys.argv, infos)
	s = connect.connect(infos)
	play(s)
