from time import sleep
import os
import pickle

# http://introtopython.org/terminal_apps.html
# #What-are-terminal-apps?

#names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']

#functions

def display_title_bar():

    os.system('clear') #clear entire terminal
    print("\t**********************************************")
    print("\t***  Greeter - Hello old and new friends!  ***")
    print("\t**********************************************")

def get_user_choice():

    print("\n[1] See a list of friends.")
    print("[2] Tell me about someone new.")
    print("[q] Quit.")

    return input("What would you like to do? ")

def show_names():
    print("\nHere are the people I know.\n")
    for name in names:
        print(name.title())


def get_new_name():
    new_name = input("\nPlease tell me the person's name: ")
    if new_name in names:
        print("\n%s is an old friend! Thank you, though." % new_name.title())
    else:
        names.append(new_name)
        print("\nI'm so happy to know %s!\n" % new_name.title())

def load_names():

    try:
        file_object = open('names.pydata', 'rb')
        names = pickle.load(file_object)
        file_object.close()
        return names
    except Exception as e:
        print(e)
        return []

def quit():
    try:
        file_object = open('names.pydata', 'wb')
        pickle.dump(names, file_object)
        file_object.close()
        print("\nThanks for playing, I will remember these good friends.")

    except Exception as e:
        print("\nThanks, I wont remember these names")
        print(e)

names = load_names()

choice = ''
display_title_bar()

while choice != 'q':


    choice = get_user_choice()

    display_title_bar()

    if choice == '1':
        #show all names
        show_names()

    elif choice == '2':
        #get new name and greet
        get_new_name()

    elif choice == 'q':
        quit()
        print("\nThanks for playing. Bye.")

    else:
        print("\nI didn't understand that choice.\n")

'''
Favorite Games

    Write a terminal app that asks people for their favorite games.
    Your app should offer users the choice of:
        Seeing all current games that are stored.
        Entering a new game.
            If the game is already stored, don't store it. Inform the user that you know that game, and like it too.
            If the game is not already stored, store it and tell the user you are happy to learn about that game.
        Quit.
            Your app should store all games when the program quits, so that it remembers all the games the next time it runs.
    Bonus: Add a "stats" element in your title bar that shows how many games are currently stored.



'''
