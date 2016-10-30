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

def store():
    global user_pass
    user_pass = {}

    user_pass.update({user_name:password})
    pprint.pprint(user_pass)

def sign_in():
    print """ \n
    ------------------------------------------
    |                                        |
    |    Sign in with your new account!      |
    |                                        |
    ------------------------------------------
    """

    while True:
        enter1 = raw_input("| Username: ")
        print "-----------------------"
        enter2 = getpass.getpass("| Password: ")
        print "-----------------------"

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
        else:
            print "----------------"
            print "Incorrect username or password, try again!"
            print "----------------"

sign_up()
store()
sign_in()
