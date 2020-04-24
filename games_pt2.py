import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
    result = random.randint(1, 2)
    if bet <= 0:
        print("Your bet needs to be above 0 to play")
        return 0
    if result == 1:
        print("Heads!")
    elif result == 2:
        print("Tails!")
    if (guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
        print("Congratulations, you won " + str(bet * .5) + " dollars!")
        return bet
    else:
        print("Sorry, you lost " + str(bet * .5) + " dollars.")
        return -bet

def cho_han(guess, bet):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    result = num1 + num2
    if bet <= 0:
        print("Your bet needs to be above 0 to play")
        return 0
    if result % 2 == 0:
        print("Even!")
    else:
        print("Odd!")
    if (guess == "Even" and result % 2 == 0) or (guess == "Odd" and result % 2 != 0):
        print("Congratulations, you won " + str(bet * .5) + " dollars!")
        return bet
    else:
        print("Sorry, you lost " + str(bet * .5) + " dollars.")
        return -bet

def card_picker(player1_bet, player2_bet):
    player_1 = random.randint(1, 10)
    player_2 = random.randint(1, 10)
    if player_1 > player_2:
        print("Player 1! You won " + str(player1_bet * .5) + " dollars!")
        return player1_bet
    elif player_2 > player_1:
        print("Player 2! You won " + str(player2_bet * .5) + " dollars!")
        return player2_bet
    else:
        return 0
  
def roulette(guess,bet):
    random_number = random.randint(0, 33)
    if random_number % 2 == 0:
        print("Even!")
    elif random_number % 2 != 0:
        print("Odd!")
    if guess == random_number:
        print("Your number, " + str(guess) + "matched! You won " + str(bet * 35) + "Dollars!")
        return bet * 35
    else:
        print("Your number, " + str(guess) + "does not match! You lost " + str(bet) + "Dollars!")
    if (random_number % 2 == 0 and guess == "Even") or (random_number % 2 != 0 and guess == "Odd"):
        print("Congatulations! You guessed correctly! You won " + str(bet * 2))
        return bet
    else:
        print("You lost " + str(bet))
        return -bet

    
#Call your game of chance functions here

money += coin_flip("Heads", 10)