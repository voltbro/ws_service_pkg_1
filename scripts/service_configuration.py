#!/usr/bin/env python

import time
import tqdm

configuration_number = 11.67
version = "0.3.9"

print("Service package 1: ver. {}".format(version))
time.sleep(0.8)
print("Service package 1: start configuration ")
time.sleep(0.5)
for i in tqdm.tqdm(range(10000), ascii=True, desc="System check"):
    time.sleep(0.001)

print("Service package 1: successfully configured!")
time.sleep(0.5)
print("Service package 1: configuration checksum : {}".format(configuration_number))