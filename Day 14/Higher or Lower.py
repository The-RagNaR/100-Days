from input_data import Data
import random
Score = 0  # initial score
def format_data(account):
    #Format the account data into printable format.
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name}, {account_descr}, from {account_country}."
   
game = True 
Repeat = True
while Repeat:
      # Generate a random account
      choice_1 = random.randint(0,4)
      choice_2 = random.randint(0,4)
      while choice_2 == choice_1:
            choice_1 = random.randint(0,4)
      account_A = Data[choice_1]
      account_B = Data[choice_2]

      # printing the generated data
      print("\nA:",format_data(account_A))
      print("\n\n******vs*********\n\n")
      print("B:",format_data(account_B))


      # Use if statement to check if user is correct.
      user_Choice = input("\n\nA or B\n").lower()
      who_is_largest = 'a'
      if account_A['follower_count'] > account_B['follower_count']:
            who_is_largest = "a"
      else:
            who_is_largest = 'b'
            
      # Score Checking and giving score
      
      # initial Score
      if user_Choice == who_is_largest:
           Score += 1 
      else:
            game = False
      
      if game:
            pass
      else:
            print('Well Played')
            print(f'Your Score is: {Score}\n\n')
            # make a game rapeatable.
            print("Play again: y/n")
            replay = input().lower()
            if replay == "y":
                  Repeat = True
                  Score = 0
            elif replay == "n":
                  break