import RPi.GPIO as g
from time import sleep

g.setmode(g.BCM)
g.setup(16, g.IN, pull_up_down=g.PUD_DOWN)

global infreq
infreq = 0


def freq(channel):
    global infreq
    infreq += 1


g.add_event_detect(16, g.RISING, callback=freq)


while True:
    sleep(1)
    print(infreq)
    infreq = 0
