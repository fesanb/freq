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
	sleep(0.1)


g.setmode(g.BCM)
g.setup(16, g.IN, pull_up_down=g.PUD_DOWN)
g.add_event_detect(16, g.RISING, callback=freq)

dbid = 0
v = [0] * 30
x = 0

f = ["5hz", "10hz", "11hz", "20hz", "53hz", "100hz", "190hz", "253hz", "350hz", "500hz", "600hz", "700hz", "800hz", "900hz", "1000hz", "1500hz", "3000hz", "6000hz", "9000hz", "12000hz", "15000hz", "18000hz", "21000hz"]

writeDB = "UPDATE freq SET {} = {} WHERE id = {}".format(x, v, i2)

print("      Raspberry Pi - Frequency test")
print("        Written by Stefan Bahrawy")
print("")
print("This test will read frequencies and store them in a database.")
print("It will prompt for changes.")
print("")
print("Each test will work for 30 sec, then prompt for new frequency. So be patient.")
print("")
input("Hit enter to set you first frequency and start the reading.")


for x in f:
	input("Set frequency to \x1b[1;31m {} \x1b[0m, and hit enter. Sit back and relax for 30sec".format(x))
	infreq = 0
	for d in range(30):
		sleep(1)
		v[d] = infreq
		infreq = 0
	print("Reading done, now DB insert")
	for i in range(30):
		i2 = i + 1
		print(x, v[i], i2)
		print(writeDB)
		db_insert(x, v[i], i2)
		input("pause")
	print("\x1b[1;32m 30 readings stored in database column {} \x1b[0m".format(x))
	print("")

print("")
print("The test is complete")
