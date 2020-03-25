import mysql.connector
import RPi.GPIO as g
from time import sleep

global infreq
infreq = 0


def freq(x):
	global infreq
	infreq += 1


def db_insert(f, v, dbid):
	cnx = mysql.connector.connect(user='pi', database='freq', password='feiten')
	cursor = cnx.cursor()
	cursor.execute(writeDB)
	cnx.commit()


g.setmode(g.BCM)
g.setup(16, g.IN, pull_up_down=g.PUD_DOWN)
g.add_event_detect(16, g.RISING, callback=freq)

dbid = 0
v = [0] * 30

f = ["5hz", "10hz", "11hz", "20hz", "53hz", "100hz", "190hz", "253hz", "350hz", "500hz", "600hz", "700hz", "800hz", "900hz", "1000hz", "1500hz", "3000hz", "6000hz", "9000hz", "12000hz", "15000hz", "18000hz", "21000hz"]

writeDB = "UPDATE freq({}) VALUES({}) WHERE id={}".format(f, v, dbid)
xi = 0

for x in f:
	input("Set frequency to {}").format(x)
	for d in range(30):
		sleep(1)
		v[d] = infreq
		infreq = 0

	for i in range(30):
		# db_insert(f[x], v[i], i)
		print(x, v[i], i)

	# x =+ 1
	# input("Change frequency")
