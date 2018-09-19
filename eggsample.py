#!/usr/bin/env python
import math

d = []
r = 130

for z in range(-r, r):
    for x in range(-r, r):
        d.append({"x": 1.0 * x / r, "y": math.sin(math.pi * x * 2 / r) * math.sin(math.pi * z / r), "z": 1.0 * z / r})

print "function eggsample() { return { data: "
print d
print "}; }"




