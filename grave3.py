#Strings and text
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#Prints x and y strings with string formattings
print x
print y

#Reuses the previous strings with string formattings
#Not-to-self: %r is for raw data and used in debugging
print "I said: %r." % x
print "I also said: '%s'." %y

'''Using string formatting but calling it on different line:
Line 17, includes %r but does not reference the string until
line 21
'''
hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

#Two strings printed together
w = "This is the left side of..."
e = "a string with a right side."

print w + e

#EXERCISE 7
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # Prints 10 times a period

end1 = "b"
end2 = "e"
end3 = "n"

#Wanted to use title() method for, hence created new variable
name = end1 + end2 + end3
print name.title()

print end1 + end2, #By including a comma, they are printed on the same line with comment
print end3
