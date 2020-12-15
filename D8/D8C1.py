#acc+- to accumulator
#jmp jumps to a new instruction relative to itself (+1 is next instruction)
#nop: nothing
import os
os.chdir("C:/Users/socks/Desktop/Advent/D8")

f = open("input.txt","r")

accumulator=0

lines = f.readlines()

exec_lines = []
cur = 0
cont = True
while (cont):
    if cur in exec_lines or cur>=len(lines):
        cont=False
    else:
        exec_lines.append(cur)
        if (lines[cur].split(' ')[0]=="acc"):
            accumulator+=int(lines[cur].split(' ')[1])
        elif (lines[cur].split(' ')[0]=="jmp"):
            cur+=int(lines[cur].split(' ')[1])-1
    cur+=1

print(accumulator)