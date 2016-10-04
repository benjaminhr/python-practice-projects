#Functions and Variables
'''
>functions name code, whilst variables name strings or numbers
>they accept arguments
'''
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" %arg1

def print_none():
    print "I got nothin'."

print_two("Ben", "Robson")
print_two_again("Benjamin", "Robinosn")
print_one("Hey")
print_none()
