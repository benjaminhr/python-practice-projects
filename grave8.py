from sys import argv

#User is prompted in command line with script
script, user_name = argv
#When asking user for x then > appears.
prompt = '> '

#Prompts user for questions stored in variables
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

#Prints all variables with string formatters
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Sweet.
""" % (likes, lives, computer)
