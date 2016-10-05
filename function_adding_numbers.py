import sys

start = ""
def main(start):
    #Asks the user if they would like to add two numbers
    print """\n
    -----------------------------------------------
    Welcome to the addition and multiplication bot!
    ----------------------------------------------- \n
    """

    print "Would you like to add two numbers together? Hit RETURN."
    print "If you would not like to do so, CTRL-C."
    raw_input("> ")

    #Asks for numbers and adds to variable
    numbers1 = int(raw_input('Number 1: '))
    numbers2 = int(raw_input('Number 2: '))

    #Function takes two numbers and adds them
    def addition(numb1, numb2):
        answer = numbers1 + numbers2
        #Prints the result
        print "%r + %r = %r \n" % (numb1, numb2, answer)

    #Calls the function
    addition(numbers1, numbers2)

    #Asks for multiplication
    answer_2 = numbers1 + numbers2
    print 'Would you like to multiply your previous result: %r?' % answer_2
    print 'RETURN to continue, CTRL-C to cancel.'
    raw_input("> ")

    #Creates variable for number
    numbers3 = int(raw_input('What number would you like to multiply by: '))

    #Function for multiplication
    def multiplication(numb3):
        answer_mult = answer_2 * numbers3

        #Prints result
        print "%r x %r = %r \n" % (answer_2, numbers3, answer_mult)
        print "Thank you for using my addition and multiplication bot! \n"
    multiplication(numbers3)

main(start)
