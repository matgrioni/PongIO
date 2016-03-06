#!/usr/bin/python

import gopro
import time

g = gopro.GoPro()
g.shutter()

time.sleep(5)
g.getLastImage()
