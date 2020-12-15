# Find how many questions each group said "yes" to
# Blank line is end of groups
# Questions range from a-z
import os
os.chdir("C:/Users/socks/Desktop/Advent/D6C1")

f = open("input.txt","r")

question_list = {}
for x in range(97,123):
    question_list[chr(x)]=False

group_questions = {} # Dictionary containing question_list dictionary
group_id = 0
group_questions[group_id]=question_list.copy() # initialize first group's question list
for line in f:
    line=line.replace('\n','') # Just get rid of that stupid linebreak now :)
    if line=="": #End of group
        group_id+=1
        group_questions[group_id]=question_list.copy()
    else:
        # Convert line to a list so we can loop through it by character
        line=list(line)
        for q in line:
            group_questions[group_id][q]=True

print("Group ID: " + str(group_id))
count=0
for group,group_q_list in group_questions.items():
    for q,yes in group_q_list.items():
        if yes:
            count+=1
print("Total count of group yeses: " + str(count))