#!/usr/bin/python

from math import ceil
from math import sqrt

# A: (0, 0, 0) => (0, 0, 0)
# B: (2000, 0, 0) => (p, 0, 0)
# C: (2000, 2000, 0) => (q, r, 0)
# D: (3000, 1500, 1700) => (s, t, u)

p = 2000
q = 2000
r = 2000
s = 3000
t = 1500
u = 1700

xArr = []
yArr = []
zArr = []

with open("coords.txt") as fileName:
    content = [ line.strip('\n') for line in fileName.readlines() ]

    for item in xrange(len(content)):
        test = content[item]
        d1 = float(test.split(' ')[0])
        d2 = float(test.split(' ')[1])
        d3 = float(test.split(' ')[2])
	d4 = float(test.split(' ')[3])

	# Formulas for 3 points (d1, d2, d3)
        # Based off of the Trilateration Wikipedia article
        # x = float((((d1**2) + (d2**2) + (q**2)) / (2 * q)))
        # y = float(((((d1**2) - (d3**2) + (q**2) + (r**2)) / (2 * r)) - ((q / r) * x)))
        # z = float((d1**2) - (x**2) - (y**2))

        # Formulas for for 3 points
        # 3 Points (d1, d2, d3, d4)
        # Based off of http://jwilson.coe.uga.edu/EMAT6680Fa05/Schultz/6690/Barn_GPS/Barn_GPS.html
	x = (((d1**2) - (d2**2) + (p**2)) / (2 * p))
        y = ((((d1**2) - (d2**2) + (r**2) + (q**2)) - ((q * ((d1**2) - (d2**2) + (p**2))) / p)) / (2 * r))
        z = ((d1**2) - (((d1**2) - (d2**2) + (p**2)) / (2 * p)) - ((((d1**2) - (d2**2) + (r**2) + (q**2)) - ((q * ((d1**2) - (d2**2) + (p**2))) / p)) / (2 * r)))

        # Get square root of z, if z is negative
        # make it positive, so we take the square root of it
        if z < 0:
            z = float(sqrt(z * -1))
        else:
            z = float(sqrt(z))

        print str(int(ceil(x))) + "," + str(int(ceil(y))) + "," + str(int(ceil(z)))

        xArr.append(int(ceil(x)))
	yArr.append(int(ceil(y)))
	zArr.append(int(ceil(z)))

xNum = str(ceil(sum(xArr) / len(xArr)))
yNum = str(ceil(sum(yArr) / len(yArr)))
zNum = str(ceil(sum(zArr) / len(zArr)))

print "sctf{" + xNum + ", " + yNum + ", " + zNum + "}"
