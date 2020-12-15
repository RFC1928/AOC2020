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

max = 0
for seat in f:
    rowstr = list(seat[0:7].replace('B',"1").replace('F',"0"))
    row = calc_binary(rowstr)

    colstr = list(seat[7:10].replace('R',"1").replace('L',"0"))
    col = calc_binary(colstr)
    
    val = (row*8)+col
    if val>max:
        max=val
        print (str(seat) + " " + str(val) + " " + str(row) + " " + str(col))

print (max)