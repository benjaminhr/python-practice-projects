#argv = "argument variable"
from sys import argv

#Unpacks argv, instead of holding all arguments, its assigned to four variable
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#To run type in CLI: "python grave7.py first 2nd 3rd"
#You can replace "first 2nd 3rd" with any 3 str/ints

#Using raw_input with argv
script, name = argv

print str(raw_input('What is your name: ')), name
