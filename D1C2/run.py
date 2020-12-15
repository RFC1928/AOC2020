# Find the product of any 3 numbers in the input that sum up to 2020

f = open("input.txt","r")
numlist = []
for x in f:
    numlist.append(x.replace('\n',''))

for x in numlist:
    for y in numlist:
        for z in numlist:
            if (int(x)+int(y)+int(z)==2020):
                print(" X:"+x+"; Y:"+y+"; Z:"+z+"; X+Y+Z="+str(int(x)+int(y)+int(z))+"; X*Y*Z="+str(int(x)*int(y)*int(z)))