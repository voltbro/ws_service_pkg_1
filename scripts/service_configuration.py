#!/usr/bin/env python

import time
import tqdm

configuration_number = 91.929291819

print("Service package 1: start configuration ")
for i in tqdm.tqdm(range(10000), ascii=True, desc="System check"):
    time.sleep(0.001)

print("Service package 1: successfully configured!")
print("Service package 1: configuration number : {}".format(configuration_number))