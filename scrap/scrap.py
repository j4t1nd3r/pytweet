#! C:\Python310\python.exe
import re
import sys

## title
print("### Hello, welcome to Python Tweet bot script. ###\n")

## menu stored as a list
menu = ['Publish new tweet to twitter',
'Add a new tweet to list',
'Look at list with available tweets',
'Publish a tweet from the list']

# menu printed with its index
print("These are the available choices:")
for (i, menu_opt) in enumerate(menu, start=0):
    print(" ", i, " ", menu_opt)


# user input as an index for the menu
menu_option = ((input("\n Select Option (0-3):")))
if not re.match("[0-3]", menu_option):
    print("Incorrect menu option")
    sys.exit("Exiting")

print("You have selected:", menu[int(menu_option)])


## Add Tweet
tweet = input("Enter a new tweet: ")
print("New Tweet: " + tweet, "\n")

print("Would you like to add this tweet to the list?")
print(" 0 No")
print(" 1 Yes")

menu_option = ((input("\n Select Option (0-1):")))
if re.match("[0]", menu_option):

if re.match("[1]", menu_option):

