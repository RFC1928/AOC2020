import os
import re
os.chdir("C:/Users/socks/Desktop/Advent/D2C1")
# Check if a "password" meets the policy definition for that password
# Each line contains a policy and a password
# The following line defines a policy requiring 10-16 "w"s in the password wwwwswwwwwwwwwlwqw (which passes, with 16 ws)
    # 10-16 w: wwwwswwwwwwwwwlwqw
f = open("input.txt")
valid = 0
invalid = 0
for x in f:
    x=x.replace("\n","")
    defin = x.split(":")[0]
    passw = x.split(":")[1]
    passw=passw.replace(" ","")
    min = int(defin.split("-")[0])
    max = int(defin.split("-")[1].split(" ")[0])
    letter = defin.split("-")[1].split(" ")[1]
    pattern = "[^"+letter+"]+"
    val_let_len=len(re.sub(pattern,"",passw))
    if min<=val_let_len and max>=val_let_len:
        valid+=1
    else:
        invalid+=1

print ("Valid: "+str(valid))
print ("Invalid: "+str(invalid))