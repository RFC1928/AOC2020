import os
import re
os.chdir("C:/Users/socks/Desktop/Advent/D4C1")

f = open("input.txt","r")
required = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
optional = ["cid"]
missing_required=0
errored=0
issue=0

passport = ""
mypid =0
for l in f:
    l=l.replace("\n","")
    if l=="": #Blank line signifies end of passport
        items = passport.split(" ")
        missing=False # Assume we're missing no required fields to start
        error=False
        for r in required: #Loop through required fields
            contained=False # Assume we haven't found this field yet
            itemerror=False
            for i in items: # Loop through all the items in this passport
                thisitem=i.split(":")[0] # Just take the name of the field
                if (r==thisitem): # Compare it to the current required item
                    contained=True
                    v=i.split(":")[1] # Value of field
                    if r=="byr":
                        if (int(v)<1920 or int(v)>2002 or len(v)!=4):
                            itemerror=True
                            print("byr: "+v)
                    elif r=="iyr":
                        if (int(v)<2010 or int(v)>2020 or len(v)!=4):
                            itemerror=True
                            print("iyr: "+v)
                    elif r=="eyr":
                        if (int(v)<2020 or int(v)>2030 or len(v)!=4):
                            itemerror=True
                            print("eyr: "+v)
                    elif r=="hgt":
                        if ("cm" in v):
                            v=int(v.replace("cm",""))
                            if (v<150 or v>193):
                                itemerror=True
                                print("hgt-cm: "+str(v))
                        elif ("in" in v):
                            v=int(v.replace("in",""))
                            if (v<59 or v>76):
                                itemerror=True
                                print("hgt-in: "+str(v))
                    elif r=="hcl":
                        if len(re.findall("\#[0-9a-f]{6}",v))==0:
                            itemerror=True
                            print("hcl: "+v)
                    elif r=="ecl":
                        if (v!="amb" and v!="blu" and v!="brn" and v!="gry" and v!="grn" and v!="hzl" and v!="oth"):
                            itemerror=True
                            print("ecl: "+v)
                    elif r=="pid":
                        if len(re.findall("[0-9]{9}",v))==0:
                            itemerror=True
                            print("pid: "+v)

            if not(contained):
               missing=True
            if itemerror:
                error=True
        if missing:
            missing_required+=1
            issue+=1
        elif error:
            issue+=1
            print (passport)
        if error:
            errored+=1
        mypid+=1 # Keep track of which passport this is for debugging
        passport="" # Reset for the next passport
    else:
        passport+=" "+l

print ("Total passports: " + str(mypid))
print ("Valid Passports: " + str(mypid-issue))
print ("Only Missing Passports: " + str(mypid-missing_required))
print ("Issues: " + str(issue))
print ("Missing Required Sections: " + str(missing_required))
print ("Errors: " + str(errored))