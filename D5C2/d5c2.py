# Find what seat is mine based on a list of everyone else's seats
import os
os.chdir("C:/Users/socks/Desktop/Advent/D5C1")

f = open("input.txt","r")

def calc_binary(val_list):
    x=1
    val = 0
    for i in reversed(val_list):
        if i=="1":
            val+=x
        x*=2
    return val

allseats = {}
for i in range(20,997):
    allseats[i]=False

for seat in f:
    rowstr = list(seat[0:7].replace('B',"1").replace('F',"0"))
    row = calc_binary(rowstr)

    colstr = list(seat[7:10].replace('R',"1").replace('L',"0"))
    col = calc_binary(colstr)
    
    seatid = (row*8)+col

    allseats[seatid]=True

for seatid,val in allseats.items():
    if not(val):
        print(seatid)

