import os
os.chdir("C:/Users/socks/Desktop/Advent/D9")

f = open("input.txt","r")

#25 number preamble
#followed by each number being sum of 2 of the 25 previous numbers (must be different, but can be re-used)

numlist = f.readlines()


looper = 25
prevcheck = 25
badnum=-1

no_error = True
while (no_error and looper<len(numlist)):
    thisnum = int(numlist[looper])
    #print (thisnum)
    found = False
    for x in range(looper-prevcheck,looper):
        for y in range(looper-prevcheck,looper):
            if (x!=y):
                if thisnum==int(numlist[x])+int(numlist[y]):
                    found=True
    if not(found):
        no_error=False
        badnum=thisnum
    looper+=1


print ("Invalid number is " + str(badnum))

hackfound = False
looper=0
while not(hackfound) and looper<len(numlist):
    numcheck = int(numlist[looper])
    innerloop=1
    minnum=numcheck
    maxnum=numcheck
    while(numcheck<badnum and looper+innerloop<len(numlist)):
        curnum = int(numlist[looper+innerloop])
        numcheck += curnum
        if curnum<minnum:
            minnum=curnum
        if curnum>maxnum:
            maxnum=curnum
        innerloop += 1
    if numcheck==badnum:
        hackfound = True
        print ("Looper: " + str(looper))
        print ("Inner Loop:" + str(innerloop))
        print ("Min Number: " + str(minnum))
        print ("Max Number:" + str(maxnum))
        print ("Answer: " + str(minnum+maxnum))
    looper+=1
