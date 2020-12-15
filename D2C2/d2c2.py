import os
import re
os.chdir("C:/Users/socks/Desktop/Advent/D2C1")
# Check if a "password" meets the policy definition for that password
# Each line contains a policy and a password
# The following line defines a policy requiring position 9 OR position 15 to be a "w" in the password wwwwswwwwwwwwwlwqw (which passes, with both spots)
    # 10-16 w: wwwwswwwwwwwwwlwqw
f = open("input.txt")
valid = 0
for x in f:
    x=x.replace("\n","")
    defin = x.split(":")[0]
    passw = x.split(":")[1].replace(" ","")
    pos1 = int(defin.split("-")[0])-1
    pos2 = int(defin.split("-")[1].split(" ")[0])-1
    letter = defin.split("-")[1].split(" ")[1]
    if (passw[pos1]==letter or passw[pos2]==letter) and not(passw[pos1]==letter and passw[pos2]==letter):
        valid+=1


print ("Valid: "+str(valid))