#! C:\Python310\python.exe

## Read file
def list():
    with open('text.txt', 'r') as file:
        global text
        text = file.read() 
        text = text.split("\n")
        return text

## Show list
def list_show():
    text = list()
    print("### List of tweets from file ###")
    for (i, tweet_opt) in enumerate(text, start=0):
        print(" ", i, " ", tweet_opt)

## Add to list
def list_add():
    list_show()
    new_text = input("Please enter a new tweet:\n")
    with open('text.txt', 'a') as file:
        file.write(f'\n{new_text}')
    list_show()

## Remove from list
def list_remove():
    list_show()
    remove_text = input('Please pick a tweet to remove:\n')
    text.pop(int(remove_text))
    with open('text.txt', 'w') as f:
        f.write('\n'.join(text))
    list_show()
