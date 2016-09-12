#Backslash escapes quotes that are using within the string
print "I am \"sarcastic\" often."

# "\t" = tab
cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."

#This allows the usage of backslash
backslash_cat = "I'm \\ a \\ cat."

#Creates a tabbed list
fat_cat = """
I'll do a list:
\t* cat food
\t* fishes
\t* catnip\n\t* Grass
"""

print cat
print persian_cat
print backslash_cat
print fat_cat

#Fun piece of little code
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i

#Some more fun
for i in ["Ben", "harry", "high"]:
    print "%s \n" % i
else:
    print "Nothing"
