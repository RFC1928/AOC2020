# WE NEED MORE JOLTAGE
# Plug Jolts != Charger Jolts
# Lots of adapters, all have different output joltage
# Adapter can take input up the 3 jolts lower than its output rating
# Device can take in 3 jolts higher than highest adapter
# Outputs at 0 jolts
# Exercise 1 was to find how many 1 volt and 3 volt jumps
# Exercise 2 is to find how many ways to get from 0 to device voltage


import os
os.chdir("D:/Development/AOC2020/D10")

f = open("input.txt","r")

class Adapter:
    def __init__(self,jolts,combos):
        self.jolts=jolts
        self.combos=combos
    def __lt__(self, other):
        return self.jolts<other.jolts
    def __eq__(self, other):
        return self.jolts==other.jolts


adapters = []
maxjolts = 0

# Build a list of all of our adapters from the file 
for line in f:
    line=line.replace('\n','') # Just get rid of that stupid linebreak now
    adapters.append(Adapter(int(line),0))
    if maxjolts<int(line):
        maxjolts=int(line)

mydev=maxjolts+3
adapters.append(Adapter(mydev,1)) # Add our device - Set to 1 combo, since we know it's the final one and has to have one way to get there
adapters.append(Adapter(0,0)) # Add 0

adapters.sort()

#print (adapters)

def build_combos(jolts,x):
    global adapters
    for i in range(x+1,min(x+4,len(adapters))): # Can't go down and can't go beyond 3 nums
            if jolts>=(adapters[i].jolts-3) and jolts<=(adapters[i].jolts-1):
                if adapters[i].combos!=0:
                    # This node has already been calculated. Simply add it to this one's total
                    adapters[x].combos+=adapters[i].combos
                else:
                    adapters[x].combos+=build_combos(adapters[i].jolts,i)

    #print ("Val " + str(nodes[x].jolts) + " - Combos: " + str(nodes[x].combos))
    return adapters[x].combos

print(build_combos(0,0))
print (adapters[0].combos)

