import random
import math

def play():
    user = input("What's ur choice? r for rock p for paper s for scissor \n")
    user = user.lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        return (0,user,computer)

    if i_win(user,computer):
        return (1,user,computer)

    return (-1,user,computer)

def i_win(player,opponent):
    if (player == 'r'and opponent == 's') or (player == 's' and opponent == 'r') or (player == 'p' and opponent == 'r'):
        return True
    return False 

def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary or computer_wins < wins_necessary:
        result,user,computer = play()

        if result == 0:
            print("You both chose {}.It's a tie".format(user))

        elif result == 1:
            player_wins += 1
            print("You chose {} and opponent chose {} so You won".format(user,computer))

        else:
            computer_wins += 1
            print("You chose {} and opponent chose {} so You lost".format(user,computer))
        print("\n")

    if player_wins > computer_wins:
        print("You won the best of {} games".format(n))

    else:
        print("You lost the best of {} games".format(n))

if __name__ == "__main__":
    play_best_of(3)