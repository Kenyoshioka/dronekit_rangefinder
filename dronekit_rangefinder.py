#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# setting up modules used in the program（使うモデュールのリスト）
from __future__ import print_function
from dronekit import connect
import exceptions
import socket
import time
import os

# connect to PixHawk（PixHawkに接続する）
os.system("clear")
vehicle = connect('/dev/ttyS0', heartbeat_timeout = 30, baud = 57600)
time.sleep(2)

# instruction（プログラムの終了する方法）
print("\nPress 'Ctrl + c' to quit.\n\n")
# 3 sec delay（3秒休憩）
time.sleep(3)

# measure distance（無限ループで距離を測る）
while True:

    # reading from rangefinder（レンジファインダーからの値を読み取る）
    rangefinder_distance = vehicle.rangefinder.distance
    # print out the reading from rangefinder（プリントアウト）
    print ("Rangefinder Distance: %.2f [m]" % float(rangefinder_distance))
    # 1 sec delay（1秒休憩）
    time.sleep(1)
