# WE NEED MORE JOLTAGE
# Plug Jolts != Charger Jolts
# Lots of adapters, all have different output joltage
# Adapter can take input up the 3 jolts lower than its output rating
# Device can take in 3 jolts higher than highest adapter
# Outputs at 0 jolts


import os
os.chdir("D:/Development/AOC2020/D10")

def find_jolt_steps(list:list,jolt_step_list:list=None):
    if jolt_step_list==None:
        jolt_step_list = [0,0,0,0]
    for x in range(0,len(list)):
        if x==0:
            jolt_step_list[list[x]]+=1
        else:
            jolt_step_list[list[x]-list[x-1]]+=1
    return jolt_step_list


f = open("input.txt","r")
adapters=[]
maxjolts = 0
# Build a list of all of our adapters from the file 
for line in f:
    line=line.replace('\n','') # Just get rid of that stupid linebreak now
    adapters.append(int(line))
    if (int(line)>maxjolts):
        maxjolts = int(line)

adapters.append(maxjolts+3) # Device is max+3
adapters.sort() # Must be in order from low to high

jolt_steps = find_jolt_steps(adapters)
print(jolt_steps)
print (jolt_steps[1]*jolt_steps[3])