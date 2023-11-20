from input_data import Data
import random
#from replit import clear

def format_data(account):
    #Format the account data into printable format.
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name},a {account_descr}, from {account_country}."

def check_answer(guess,a_followers,b_followers):
    ## Use if statement to check if user is correct.
    if a_followers>b_followers:
        return guess == "a"
    else:
        return guess == "b"

score=0
game_should_continue=True
#Generate a random account
account_b=random.choice(Data)

#make a game rapeatable.

    
    #Making account at position B become the next account at position A.
    
    #Ask user for a guess.
    
    #Check if user is correct.
    ## Get follower count of each account.
    

    #clear()

    #Give user feedback on their guess.
    # Score keeping.
    