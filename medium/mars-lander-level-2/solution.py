import sys
import math
import collections

initialized = False
derekStarting = 0 
derekClosest = 0
derekSwitch = 0

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Finds flat ground
# @param sortedPoints is Ordered Dictionary
def findFlatLand(sortedPoints):
    flatPoints = []
    iterPoint = 0
    for x, y in sortedPoints.items():
        count = 0
        for x2, y2 in sortedPoints.items():
            if y2 == y and x2 != x and ((count - iterPoint) == 1):
                flatPoints.append(x+100)
                flatPoints.append(x2-100)
                break
            count += 1
        iterPoint += 1

    return flatPoints

    # Evaluate what speed we should be going
    # return speed


# Stabilization method on start
def stabilize(horizontalSpeed, verticalSpeed):
   if horizontalSpeed >= 40:
        print("21 4") 
   elif horizontalSpeed <= -40:
        print("-21 4")


# Movement method
def approach(derekStarting, derekCurrent, derekClosest, derekSwitch, verticalSpeed, horizontalSpeed):
    distXL = abs(derekClosest- derekCurrent)
    
    if derekCurrent > derekClosest and horizontalSpeed <= 0:
        if horizontalSpeed > -38:
            print("35 4")
        else: 
            if verticalSpeed > 0:
                print("0 3")
            else:
                print("0 4")
    elif derekCurrent > derekClosest and horizontalSpeed > 0:
        print("60 4")
    elif derekCurrent < derekClosest and horizontalSpeed >= 0:
        if horizontalSpeed < 38:
            print("-35 4")
        else:
            if verticalSpeed > 0:
                print("0 3")
            else:
                print("0 4")
    elif derekCurrent < derekClosest and horizontalSpeed < 0:
        print("-60 4")

# CQB Function for when we enter the landing zone
def cqb(horizontalSpeed, verticalSpeed):
   # Check if h_speed is pos or neg
   if abs(horizontalSpeed) <= 1:
    if verticalSpeed <= -40:
        print("0 4")
    else:
        print("0 2")
   elif horizontalSpeed > 1:
    #print(str(horizontalSpeed if (horizontalSpeed < 45) else 60) + " 4")
    print("21 4")
   elif horizontalSpeed < -1:
    #print(str(horizontalSpeed if (horizontalSpeed > -45) else -60) + " 4")
    print("-21 4")



points = {} 
surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    points[land_x] = land_y


sortedPoints = collections.OrderedDict(sorted(points.items()))
flatLand = findFlatLand(sortedPoints)

# game loop
while 1:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Initialize vars if first turn
    if not initialized:
        derekStarting = x
        derekClosest = (flatLand[0] + flatLand[1]) / 2
        print("Starting Position is " + str(derekStarting), file=sys.stderr)
        print("Point 1 is " + str(flatLand[0]) + " and Point 2 is " + str(flatLand[1]), file=sys.stderr)
        if abs(flatLand[0] - x) < abs(flatLand[1] - x):
            derekSwitch = abs((flatLand[0] - derekStarting) / 2)
        else:
            derekSwitch = abs((flatLand[1] - derekStarting) / 2)

        print("Switch is " + str(derekSwitch), file=sys.stderr)

        initialized = True

    derekClosest = flatLand[0] if abs(flatLand[0] - x ) < abs(flatLand[1] - x) else flatLand[1]
    derekCurrent = x

    # Switch to CQB if within landing zone
    if abs(h_speed) >= 40:
        stabilize(h_speed, v_speed)
        print("Stabilizing...", file=sys.stderr)
    elif x >= flatLand[0] and x <= flatLand[1]:
        cqb(h_speed, v_speed)
        print("CQB Starting...", file=sys.stderr)
    else:
        approach(derekStarting, derekCurrent, derekClosest, derekSwitch, v_speed, h_speed)
        print("Approaching Land zone...", file=sys.stderr)

    print("Rotation = " + str(rotate) + ", Power = " + str(power), file=sys.stderr)



    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
