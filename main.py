#! C:\Python310\python.exe
import tweepy
import keys
import re
import sys

## Set  message contents to none
new_text = None

## --- List interaction --- ##
## Read file
def list():
    with open('text.txt', 'r') as file:
        text = file.read() 
        text = text.split("\n")
        return text

## Show list
def list_show():
    text = list()
    print("### List of tweets from file ###")
    for (i, tweet_opt) in enumerate(text, start=0):
        print(" ", i, " ", tweet_opt)
        return text

## Add to list
def list_add_file(new_text):
    with open('text.txt', 'a') as file:
        file.write(f'\n{new_text}')
    list_show()

def list_add():
    list_show()
    new_text = input("Please enter a new tweet:\n")
    list_add_file(new_text)

## Remove from list
def list_remove():
    list_show()
    text = list()
    remove_text = input('Please pick a tweet to remove:\n')
    text.pop(int(remove_text))
    with open('text.txt', 'w') as f:
        f.write('\n'.join(text))
    list_show()

## --- Message interaction --- ##
def new_message(): 
    new_text = input("Please enter a new tweet:\n")
    print("Would you like to add this tweet to the list?")
    print(" 0 No")
    print(" 1 Yes")
    menu_option = ((input("\n Select Option (0-1):")))
    if re.match("[0]", menu_option):
     print('action for selecting No goes here')
    elif re.match("[1]", menu_option):
        list_add_file(new_text)
        print("Would you like to post this via twitterbot now?")
        print(" 0 No")
        print(" 1 Yes")
        menu_option = ((input("\n Select Option (0-1):")))
        if re.match("[0]", menu_option):
            print('action for selecting No goes here')
        elif re.match("[1]", menu_option):
            tweet(api, new_text)

## --- Tweepy interaction --- ##
def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_key_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)
    print('Tweeted successfully!')

api = api()
new_message()