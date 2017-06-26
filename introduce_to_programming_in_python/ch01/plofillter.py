#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import stddraw
import stdio

x0 = stdio.readFloat()
y0 = stdio.readFloat()
x1 = stdio.readFloat()
y1 = stdio.readFloat()

stddraw.setXscale(x0, x1)
stddraw.setYscale(y0, y1)

stddraw.setPenRadius(0.0)
stddraw.setPenColor(stddraw.DARK_BLUE)

while not stdio.isEmpty():
    x = stdio.readFloat()
    y = stdio.readFloat()
    stddraw.point(x, y)

stddraw.show()
