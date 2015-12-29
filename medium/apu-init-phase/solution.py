import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
Matrix = [[0 for x in range(height)] for x in range(width)]
    
# Creating the matrix
for i in range(height):
    line = input()  # width characters, each either 0 or .
    for j in range(width):
        Matrix[j][i] = line[j]

cArray = []
for i in range(width):
    for j in range(height):
        coordinates = ""
        if Matrix[i][j] == '0':
            coordinates = coordinates + str(i)+" "+str(j)+" "

            # Find Next Node to the Right
            k = i+1
            print("k is "+str(k), file=sys.stderr)
            while k != width+1:
                if k != width:
                    if Matrix[k][j] == '0':
                        coordinates = coordinates + str(k)+" "+str(j)+" "
                        break
                else:
                    coordinates = coordinates + "-1 -1 "
                k += 1
                
            # Find Next Node to the Bottom
            k = j+1
            while k != height+1:
                if k != height:
                    if Matrix[i][k] == '0':
                        coordinates = coordinates + str(i)+" " +str(k)+" "
                        break
                else:
                    coordinates = coordinates + "-1 -1 "
                k += 1

            cArray.append(coordinates)

for c in cArray:
    print(c)