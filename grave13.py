#function taking two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#plugging in numbers to function
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#plugging in numbers to arguments - not function directly
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#calling function and doing maths inside arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#calling functions and doing maths with the argument
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
