import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Link():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.severed = False
        
    def sever(self):
        print(str(self.n1)+" "+str(self.n2))
        self.severed = True

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
linkArr = []
exits = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    link = Link(n1, n2)
    linkArr.append(link)
    
for i in range(e):
    ei = int(input())  # the index of a gateway node
    exits.append(ei)

# game loop
while 1:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    print("Skynet is on node "+str(si), file=sys.stderr)

    # Figure out where the AI is
    # Sever the node closest to an exit gateway based on the AI's location
    foundLink = False
    for l in linkArr:
        if not l.severed:
            # Check if it's an exit node
            # We need to find if the virus is the other node first, then cut that
            if l.n1 == si or l.n2 == si:
                for e in exits:
                    if l.n1 == e or l.n2 == e:
                        l.sever()
                        foundLink = True
                        break
            else:
                for e in exits:
                    if l.n1 == e or l.n2 == e:
                        linkToSever = l
            
    # The conditional is here because the game will not end after print and end up queuing this as the next move
    if not foundLink:      
        linkToSever.sever()

