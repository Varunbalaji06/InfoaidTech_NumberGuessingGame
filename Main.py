import random
print("Welcome to the Number Guessing Game")
print("Here the Computer will guess a number between 1 to 100")
print("You must try to guess it within 10 attempts")
player_name = input("Enter your name: ")
print(f"Hello,{player_name}") 
while True:
    Comp_guess = random.randrange(1,100)
    attempts = 0
    while attempts < 10:
        player_guess = int(input("Enter the guessed number: "))
        attempts+=1

        if player_guess == Comp_guess:
            print(f"Congratulations , {player_name}!! You guessed the number {Comp_guess} correctly in {attempts} attempts.")
            break
        elif player_guess < Comp_guess:
            print("Your Guess is Low , Try Again..")
        else:
            print("Your Guess is High , Try Again..")

    else:
        print(f"Sorry {player_name}, You Failed to guess the number in 10 attempts..")
        print(f"The number to be Guessed was {Comp_guess}")
        print("Game Over!!")
    play_again = input("Do you want to play again?? (Yes/No): ").lower()
    if play_again!="yes":
        print("Thanks For playing , GoodBye!!")
        break
