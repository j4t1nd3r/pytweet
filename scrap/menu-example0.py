#!/usr/bin/env python3

menu_options = {
    1: 'Publish new tweet to twitter',
    2: 'Add a new tweet to list',
    3: 'Look at list with available tweets',
    4: 'Publish a tweet from the list',
    5: 'Back to Main Menu'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key])
def option1():
     print('Handle option \'Option 1\'')

def option2():
    ## Read file
    # opening the file in read mode
    print("### Look at list of available tweets ###")
    file = open("tweets.txt", "r")  
    # reading the file
    text = file.read()  
    # replacing end splitting the text 
    # when newline ('\n') is seen.
    text = text.split("\n")
    file.close()
    # for (i, tweet_opt) in enumerate(text, start=0):
    #     print(" ", i, " ", tweet_opt)
    print(text)

def option3():
     print('Handle option \'Option 3\'')

def option4():
     print('Handle option \'Option 4\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 5.')