#!/usr/bin/python
# -*- coding; utf-8 -*-

import time

cicle = 1
while True:
    for i in ["---", " \\ ", " | ", " / "]:
        time.sleep(0.1)
        cicle += 1
        print("\rcicle: %3d %s" % (cicle, i), end="")
