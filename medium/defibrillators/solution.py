'''
    John Ezekiel
    Python3 Solution for CodinGame
    Defibrillator Puzzle
'''
import sys
import math

# Defibrillator Class
class Defib:
    def __init__(self, defib):
        self.id = defib[0]
        self.name = defib[1]
        self.address = defib[2]
        self.contact = defib[3]
        self.lon= float(defib[4].replace(',','.'))
        self.lat= float(defib[5].replace(',','.'))
        
def main():
    lon = float(input().replace(',','.'))
    lat = float(input().replace(',','.'))
    n = int(input())

    # Creating defib class for all defibs and
    # loading them into an array
    defibArray = []
    for i in range(n):
        defib = Defib(input().split(';'))
        defibArray.append(defib)
        
    cDefib = defibArray[0]
    closestDist = getDistance(lon, cDefib.lon, lat, cDefib.lat)
    for d in defibArray:
        dist = getDistance(lon, d.lon, lat, d.lat)
        if closestDist > dist:
            closestDist = dist
            cDefib = d

    print(cDefib.name)
        
# Function
# Returns distance between the user and defib
def getDistance(lonA, lonB, latA, latB):
    x = (lonB - lonA) * math.cos((latA + latB)/2)
    y = (latB - latA)
    dRad = math.sqrt(math.pow(x,2) + math.pow(y,2)) * 6371
    return math.degrees(dRad)

if __name__ == "__main__":
    main()