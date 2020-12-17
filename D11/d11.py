# Calculating ideal spot to sit
# Have a map of seats (. is floor, L is empty seat, # is occupied)
# All rules run at once
#   If seat is empty and all adjacent (including diagonal) are empty, seat becomes occupied
#   If >= 4 adjacent seats are occupied, seat becomes empty
#   Floor is basically a seat that's permanently empty


import os
os.chdir("D:/Development/AOC2020/D11")

f = open("input.txt","r")

# BUILD DICTIONARY
y=0
seatmap = {}
for line in f:
    x=0 # Reset x
    line=line.replace('\n','') # I hate this character
    for char in list(line): # Loop through each character on the line
        seatmap[(x,y)]=char
        x+=1
    y+=1 # Increment y for next line


def display_seats(seatmap):
    x=0
    y=0
    for y in range (0,1000):
        linehadstuff=False
        for x in range(0,1000):
            if (x,y) in seatmap:
                print(seatmap[x,y],end="")
                linehadstuff=True
        if (linehadstuff):        
            print ("")

def apply_rules_part1(seatmap):
    newmap = seatmap.copy()
    for k,v in newmap.items():
        if v=="L":
            # Currently empty. Check if all spots around are empty to switch to occupied
            has_occupied=False
            for x in range(k[0]-1,k[0]+2):
                for y in range(k[1]-1,k[1]+2):
                    if (x,y) in seatmap:
                        if (seatmap[(x,y)]=="#"):
                            has_occupied=True
            if not(has_occupied):
                newmap[k]="#" # Switch this seat to occupied because none of its adjacent ones were ocupied
        elif v=="#": # Currently occupied. Check if 4+ others around it are occupied
            num_occupied=0
            for x in range(k[0]-1,k[0]+2):
                for y in range(k[1]-1,k[1]+2):
                    if (x,y) in seatmap:
                        if (x,y)!=k:
                            if (seatmap[(x,y)]=="#"):
                                num_occupied+=1
            if (num_occupied>=4):
                newmap[k]="L"
    
    return newmap

def part1(seatmap):
    # PART 1: Run rules until it stabilizes and count number of occupied seats
    oldval = -1 # Make sure this doesn't match right away
    newval = 0 
    for k,v in seatmap.items():
        if v=="#":
            newval+=1
    while (oldval!=newval):
        oldval=newval # Move oldval to newval's #
        seatmap = apply_rules_part1(seatmap)
        newval = 0 # Reset newval to 0 and count it
        for k,v in seatmap.items():
            if v=="#":
                newval+=1

    print ("Occupied seats after stabilizing: " + str(newval))


def parse_dir (seatmap, curx, cury, xdir, ydir):
    if (xdir==0 and ydir==0):
        # EEK!
        return False
    
    newx=curx+xdir
    newy=cury+ydir
    while (newx,newy) in seatmap:
        #print ("Checking " + str(newx) + "," + str(newy))
        if seatmap[(newx,newy)]=="#":
            #print ("Returning true")
            return True
        elif seatmap[(newx,newy)]=="L":
            return False
        #Increment!
        newx=newx+xdir
        newy=newy+ydir


    return False # Didn't find anything, so assume we're good to go!
    


def apply_rules_part2(seatmap):
    # Similiar to part 1 except if we run into floor, we continue moving in that direction
    newmap = seatmap.copy()
    for k,v in newmap.items():
        if v=="L":
            # Currently empty. Check if all spots that we can see are empty
            has_occupied=False
            for x in range(-1,2):
                for y in range(-1,2):
                    if (x!=0 or y!=0): # Move in some direction!
                        if not(has_occupied):
                            has_occupied=parse_dir(seatmap,k[0],k[1],x,y)
            if not(has_occupied):
                newmap[k]="#" # Switch this seat to occupied because none of its adjacent ones were ocupied
        elif v=="#": # Currently occupied. Check if 4+ others around it are occupied
            num_occupied=0
            for x in range(-1,2):
                for y in range(-1,2):
                    if (x!=0 or y!=0): # Move in some direction!
                        if (parse_dir(seatmap,k[0],k[1],x,y)):
                            num_occupied+=1
            if (num_occupied>=5):
                newmap[k]="L"
    
    return newmap

def part2(seatmap):
    #WTF. Rules changed! Now rules say skip floor and move on to the next seat in that direction
    oldval = -1 # Make sure this doesn't match right away
    newval = 0 
    for k,v in seatmap.items():
        if v=="#":
            newval+=1
    while (oldval!=newval):
        oldval=newval # Move oldval to newval's #
        seatmap = apply_rules_part2(seatmap)
        newval = 0 # Reset newval to 0 and count it
        for k,v in seatmap.items():
            if v=="#":
                newval+=1

    print ("Occupied seats after stabilizing: " + str(newval))


#part1(seatmap)
part2(seatmap)