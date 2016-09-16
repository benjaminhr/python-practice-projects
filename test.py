from sys import argv

script, filename = argv

txt = open(filename)
print "Here is your filename: %r" % filename
print txt.read()

print "What would you like to add? "
prompt = raw_input('> ')

txt.write(prompt)
txt.write("\n")

print txt.read()
txt.close()
