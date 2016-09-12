#By using comma, in terminal it is not printed on the next line
#Raw_input() gets input from user, returns data input in a string
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#Question is printed, variable is called, raw_input saves answers and then is printed
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#Another way to use raw_input
name = raw_input('What is your name? ')

if name == "ben":
    print "You are the correct one."
else:
    print "You are the wrong one."

#Converting raw_input into string
usr_age = int(raw_input('How old are you? '))

if usr_age < 5:
    print "You are old."
elif usr_age == 7:
    print "You are Harold."
else:
    print "You are too young"
