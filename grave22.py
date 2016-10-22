numbers = []

def loop(top_limit):
    i = 0
    while i < top_limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i += + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

print "What would you like to be the top limit: "
top_limit = int(raw_input('> '))

print "What would you like your increment to be: "
increment = int(raw_input('> '))

loop(top_limit)
