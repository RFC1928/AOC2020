# Find the product of any 2 numbers in the input that sum up to 2020

f = open("input.txt","r")
numlist = []
for x in f:
    numlist.append(x.replace('\n',''))

for x in numlist:
    for y in numlist:
        if (int(x)+int(y)==2020):
            print(" X:"+x+"; Y:"+y+"; X+Y="+str(int(x)+int(y))+"; X*Y="+str(int(x)*int(y)))