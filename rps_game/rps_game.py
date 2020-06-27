# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function `get_hand` to get the string representation of the user's hand
# call the function `get_hand` to get the string representation of the computer's hand
# call the function `determine_winner` to figure out who won
# print out the player hand and computer hand
# print out the winner
import random

def get_hand(number):
    if number == 0:
        hand = "scissor"
        return hand
    elif number == 1:
        hand = "rock"
        return hand
    elif number == 2:
        hand = "paper"
        return hand
    return get_hand()

def determine_winner(usr,comp):
    def get_result():
        if user_hand == "scissor" and comp_hand == "paper":
            print("winner is user")
        elif user_hand == "rock" and comp_hand == "scissor":
            print("winner is user")
        elif user_hand == "paper" and comp_hand == "rock":
            print("winner is user")
        elif user_hand == "scissor" and comp_hand == "scissor":
            print("Draw!")
        elif user_hand == "rock" and comp_hand == "rock":
            print("Draw!")
        elif user_hand == "paper" and comp_hand == "paper":
            print("Draw!")
        else:
            print("winner is computer")
    win = get_result()
    return win

user = int(input("Enter number based on your choice, 0 = scissor, 1 = Rock, 2 = Paper: "))
computer = random.randint(0, 2)
user_hand = get_hand(user)
comp_hand = get_hand(computer)
print(f"You choose {user_hand}, computer choose {comp_hand}!")

determine_winner(user_hand, comp_hand)
