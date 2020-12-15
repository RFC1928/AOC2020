# How many bag colors can be the outermost layer of a shiny gold bag?
# descr1 descr2 bags contain # descr1 descr2 bags(,|.) descr1 descr2 bags
import os
os.chdir("C:/Users/socks/Desktop/Advent/D7")

f = open("input.txt","r")

class Bag:
    inner_bags = []

    def __init__(self,desc):
        self.desc=desc

class inner_bag_ref:
    def __init__(self,num,bag):
        self.num=num
        self.bag=bag


# Have a list of bags. Whenever bag is mentioned, check if it's in the list of bags. If so, grab a reference to it
# Each bag contains its own inner bags, which are references to inner bags
# If no inner bags are allowed, it's an empty array
# Inner bags are objects as well - containing reference to the bag and number required

bags = {}
for line in f:
    line=line.replace('\n','') # Just get rid of that stupid linebreak now :)
    rules = line.split(" ")
    outer_bag_desc = rules[0] + " " + rules[1]
    bags[outer_bag_desc] = {}

    x=4
    while (x<=len(rules)-4):
        num = rules[x]
        if (num!="no"):
            inner_bag_desc = rules[x+1] + " " + rules[x+2]
            bags[outer_bag_desc][inner_bag_desc]=num
        x+=4

# return a list of bags that can contain this one
def find_containing(color):
    retlist = []
    for bag,innerbags in bags.items():
        for innerbag,num in innerbags.items():
            if (innerbag==color):
                retlist.append(bag)
    return retlist

                

all_colors = find_containing('shiny gold')
searchlist = all_colors.copy()
while (len(searchlist)>0):
    col_list = find_containing(searchlist.pop())
    for x in col_list:
        if x not in searchlist:
            searchlist.append(x)
        if x not in all_colors:
            all_colors.append(x)

#print ("ALL COLORS")
#print (all_colors)
#print (len(all_colors))


# PART 2: Find how many bags our shiny gold bag has to contain
"""
a[b]=3
a[c]=4

b[d]=1
d[e]=1

b=2
a[b]=9
a[c]=4
a=10
"""
def num_inside(color):
    count = 0
    if (color in bags):
        for innerbag,num in bags[color].items():
            num=int(num)
            count+=num*(1+num_inside(innerbag))
    return count

print (num_inside('shiny gold'))