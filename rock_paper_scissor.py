import random

computer_wins = 0
player_wins = 0
# while computer_wins < 2 and player_wins < 2:
for time in range( 5 ):
    print( "ROCKS" )
    print( "PAPER" )
    print( "SCISSORS" )

    print( f"player score is  {player_wins} " )
    print( f"computer score is {computer_wins} " )
    user = input( "enter your choice: " )
    if user == "QUIT" or user == "Q":
        break
    random_var = random.randint( 1, 3 )
    computer = ""
    if random_var == 1:
        computer = "ROCKS"
    elif random_var == 2:
        computer = "PAPER"
    else:
        computer = "SCISSORS"

    print( f"THE COMPUTER PLAYS {computer} " )
    if user == computer:
        print( "its a tie buddy between you and the computer" )
    elif user == "ROCKS":
        if computer == "PAPER":
            print( "computer won !!!!!!1" )
            computer_wins += 1
        else:
            print( "player won the game" )
            player_wins += 1
    elif user == "PAPER":
        if computer == "ROCKS":
            print( "player won the game" )
            player_wins += 1
        else:
            print( "computer won the game" )
            computer_wins += 1
    elif user == "SCISSORS":
        if computer == "ROCKS":
            print( "computer won the game" )
            computer_wins += 1
        else:
            print( "player won the game" )
            player_wins += 1
    else:
        print( "please enter a valid move" )

print( f"player score is  {player_wins} " )
print( f"computer score is {computer_wins} " )
