#acc+- to accumulator
#jmp jumps to a new instruction relative to itself (+1 is next instruction)
#nop: nothing
import os
os.chdir("C:/Users/socks/Desktop/Advent/D8")

f = open("input.txt","r")


lines = f.readlines()

def test_run(lines):
    accumulator=0
    exec_lines = []
    cur = 0
    cont = True
    while (cont):
        if cur in exec_lines:
            return -1
        elif cur>=len(lines):
            return accumulator
        else:
            exec_lines.append(cur)
            if (lines[cur].split(' ')[0]=="acc"):
                accumulator+=int(lines[cur].split(' ')[1])
            elif (lines[cur].split(' ')[0]=="jmp"):
                cur+=int(lines[cur].split(' ')[1])-1
        cur+=1

accum = -1
looper = 0
while (accum==-1):
    if (lines[looper].split(' ')[0]=="jmp"):
        newlines = lines.copy()
        newlines[looper]='nop ' + lines[looper].split(' ')[1]
        accum=test_run(newlines)
    elif (lines[looper].split(' ')[0]=="nop"):
        newlines = lines.copy()
        newlines[looper]='jump ' + lines[looper].split(' ')[1]
        accum=test_run(newlines)
    looper+=1

print (accum)

