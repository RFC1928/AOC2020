import os
import re
os.chdir("C:/Users/socks/Desktop/Advent/D3C1")
# SkiTree
def treesearch(right,down):
    right=int(right)
    down=int(down)
    f = open("input.txt")
    trees=0
    line=0
    over=0
    for x in f:
        x=x.replace('\n',''""'')
        if line!=0: # We skip the first line
            if line%down==0: # Make sure we're intending to check this line
                if over>=len(x):
                    over=over%len(x)
                x=list(x)
                if x[over]=="#":
                    x[over]="X"
                    trees+=1
                else:
                    x[over]="O"
                over+=right # Only move over if we're on a line we're processing (line%down=0)
        else:
            over+=right # If it's line 0, still need to go over
        #print("".join(x))
        line+=1 # Always increment line
    print ("Right: "+str(right)+"; Down: " + str(down)+"; Trees hit: " + str(trees))
    return trees

print(treesearch(1,1)*treesearch(3,1)*treesearch(5,1)*treesearch(7,1)*treesearch(1,2))