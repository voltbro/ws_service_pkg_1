#!/usr/bin/env python

import time
import tqdm
import rospy

configuration_number = 12.67
version = "0.3.14"

print("Service package 1: ver. {}".format(version))
time.sleep(0.8)
print("Service package 1: start configuration ")
time.sleep(0.5)
for i in tqdm.tqdm(range(10000), ascii=True, desc="System check"):
    time.sleep(0.001)

print("Service package 1: successfully configured!")
time.sleep(0.5)
print("Service package 1: configuration checksum : {}".format(configuration_number))
print("Service package 1: please push Ctrl+C to finish")
