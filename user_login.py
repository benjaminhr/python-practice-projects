#Hides characters for raw_input password
import getpass
#Prints dictionaries on new lines
import pprint

#Login
def sign_up():
    print """ \n
    ------------------------------------------
    |                                        |
    |         Welcome to signing up!         |
    |                                        |
    ------------------------------------------
    \n
    """
    #While loop incase username is too short
    while True:
        print "----------------"
        #Stores username in variable
        global user_name
        user_name = str(raw_input("| Create username: "))
        print "----------------"

        #Checks for appropriate length
        if len(user_name) < 4:
            print "That username is too short, try again!"
        else:
            #While loop for password length
            while True:
                #Stores password in variable
                global password
                password = getpass.getpass("| Create password: ")

                if len(password) < 4:
                    print "----------------\nPassword is too short, try again!\n----------------"

                else:
                    print "----------------"
                    #Stops password while loop
                    return False
            #Stops sign_up while loop
            return False

#Stores username and password in dictionary
def store():
    #assigns variable to global so that it can be used outside of funct
    global user_pass
    #Dictionary
    user_pass = {}

    #Updates dictionary with new pass and username
    user_pass.update({user_name:password})
    #With "pprint" prints each line of the dictionary individually
    #pprint.pprint(user_pass)

#Signs in user
def sign_in():
    print """
    ------------------------------------------
    |                                        |
    |    Sign in with your new account!      |
    |                                        |
    ------------------------------------------
    """
    #Loops login for incorrect username+password
    while True:
        #Asks for username+password
        enter1 = raw_input("| Username: ")
        print "-----------------------"
        enter2 = getpass.getpass("| Password: ")
        print "-----------------------"

        #Checks dictionary if username equals password
        if user_pass.get(enter1) == enter2:
            print """

   --- You are logged in! ---

        ^__^
        (oo)\_______
        (__)\       )\/\/
            ||----w |
            ||     ||
                """
            return False
        #If wrong, loops runs again
        else:
            print "----------------"
            print "Incorrect username or password, try again!"
            print "----------------"

#Calls functions
def call ():
    sign_up()
    store()
    sign_in()

call()
