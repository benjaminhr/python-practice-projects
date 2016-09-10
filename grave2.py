#Various variable assignments used in printing within strings
my_name = 'benjamin'
my_age = 10
my_height = 175
my_weight = 70
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'
my_weight_in_pounds = my_weight * 1.35

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "%s's weight in pounds is %d" % (my_name[0].upper() + my_name[1:], my_weight_in_pounds)

Everything = "%r %r %r" % (my_name, my_eyes, my_teeth)

print Everything.title()
