from sys import argv

script, filename = argv

#Variable for user input, filename
txt = open(filename)

#prints filename
print "Here is your file: %r" % (filename)
#Reads the contents of the txt file
print txt.read()

#Asks for filename again with prompt + raw_input
print "Type the filename again: "
file_again = raw_input("> ")

#Reads content of filename that was collected from raw_input
txt_again = open(file_again)

print txt_again.read()
