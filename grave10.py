from sys import argv

script, filename = argv

#Asks user if they want file to be deleted
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you don't want that, hit RETURN."

raw_input("?")

#Opens file
print "Opening the file..."
target = open(filename, 'w')

#Deletes (truncates) file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

print "I'm going to write these to the file."

#User raw_input from lines 22-24 put into txt file
target.write('%s \n %s \n %s \n' % (line1,line2,line3))
#Most importantly, closing the file
print "And finally, we close it."
target.close()
