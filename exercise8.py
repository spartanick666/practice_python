
player1 = input('Player1, please pick "rock", "paper", or "scissors": ').lower()
while player1 != "rock" and player1 != "paper" and player1 != "scissors":
    print("Are you sure? Please pick again")
    player1 = input('Player1, please pick "rock", "paper", or "scissors": ').lower()

player2 = input('Player2, Please pick "rock", "paper", or "scissors": ').lower()
while player2 != "rock" and player2 != "paper" and player2 != "scissors":
    print("Did you choose correctly? Try again")
    player2 = input("Player2, please pick rock, paper, or scissors: ").lower()

if player1 == player2:
    print("The game is a tie")
elif player1 == ("rock") and player2 == ("paper") or player1 == ("paper") and player2 == ("scissors") \
        or player1 ==("scissors") and player2 == ("rock"):
    print("Player 2 Wins!")
elif player2 == ("rock") and player1 == ("paper") or player2 == ("paper") and player1 == ("scissors") \
        or player2 ==("scissors") and player1 == ("rock"):
    print("Player 1 Wins!")

