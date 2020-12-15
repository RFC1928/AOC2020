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
        #print("".join(x))
        line+=1
        over+=right

    print ("Right: "+str(right)+"; Down: " + str(down)+"; Trees hit: " + str(trees))

treesearch(3,1)