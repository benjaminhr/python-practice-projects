#Returning functions and using functions to set variables
#Adding function
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

#Subtracting function
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

#Multiplying function
def multiply(a ,b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

#Dividing function
def divide(a ,b):
    print "MULTIPLYING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

#Calls functions and sets variables
age = add(30,5)
height = subtract(78,4)
weight = multiply(10,10)
iq = divide(100,2)

#Prints variables with string formatters
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#Using variables in functions
what = add(, subtract(height, multiply(weight, divide(iq, 2))))
#Otherwise prints final operation and not answer
result_of_what = what

#Prints above variable
print "That becomes: ", result_of_what, "Can do you do it by hand?"
