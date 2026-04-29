import random


def print_menu():
    print()
    print("Welcome to Number Guessing Battle! ")
    print("1. Easy Mode - unlimited attempts!!")
    print("2. Medium Mode - 10 attempts is enough!")
    print("3. Hard Mode - just 5 attempts!")
    print("4. Or maybe... my turn to guess?")
    print("5. No quit!")


def is_number(text):
    if text == "":
        return False

    index = 0

    while index < len(text):
        if text[index] < "0" or text[index] > "9":
            return False
        index = index + 1

    return True

def print_line():
    print("------------------------------------")

def play_player_guessing(mode_name, max_attempts, best_scores):
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_numbers = []
    game_over = False
    low = 1
    high = 100

    print()
    print(mode_name, "! Let's get started! ")
    print("I've picked a number between 1 and 100! Your turn to guess!")

    if max_attempts == 0:
        print("You have unlimited attempts!! That's a lot!")
    else:
        print("You have", max_attempts, "attempts.")

    while not game_over:
        print("Current possible range:", low, "-", high)
        guess_text = input("Enter your guess: ")
        print_line()

        if not is_number(guess_text):
            print("I thought we are playing number guessing.")
        else:
            guess = int(guess_text)

            if guess < 1 or guess > 100:
                print("1 and 100!!")
            elif guess in guessed_numbers:
                print("You already guessed that number before...")
            elif guess < low or guess > high:
                print("Heyy! The range is between", low, "and", high)
            else:
                attempts = attempts + 1
                guessed_numbers.append(guess)

                if guess == secret_number:
                    print("Fine. You guessed the number!")
                    print("Total attempts:", attempts)
                    print("Your guesses:", guessed_numbers)

                    if best_scores[mode_name] == 0:
                        best_scores[mode_name] = attempts
                        print("New career best for", mode_name + ":", attempts, "attempts!")
                    elif attempts < best_scores[mode_name]:
                        best_scores[mode_name] = attempts
                        print("New career best for", mode_name + ":", attempts, "attempts!")
                    elif attempts == best_scores[mode_name]:
                        print("You tied your career best for", mode_name + "!")
                    else:
                        print("Your career best for", mode_name, "is still", best_scores[mode_name], "attempts. Try to be smarter next time.")

                    game_over = True
                else:
                    if guess > secret_number:
                        direction_message ="Try a lower number. "
                        if guess - 1 < high:
                            high = guess - 1
                    else:
                        direction_message ="Try a higher number. "
                        if guess + 1 > low:
                            low = guess + 1

                    difference = guess - secret_number
                    if difference < 0:
                        difference = difference * -1

                    if low == high:
                        print("Just say the last number!")
                    elif attempts == 1 and guess == 50:
                        print("The first guess is always 50... right?")
                    elif attempts <= 3 and (guess <= 3 or guess >= 97):
                        print("...really?")
                    elif difference <= 5:
                        print("You are very close! I am getting nervous.")
                    elif difference <= 15:
                        print("Great attempt!")
                    else:
                        print("You are so close!...just kidding. You are still far away.")
                    print(direction_message)

                    if max_attempts != 0:
                        attempts_left = max_attempts - attempts
                        print("Attempts left:", attempts_left)

                        if attempts_left == 1:
                            print("Final chance. This is where heroes are born... or buried.")

                        if attempts_left == 0:
                            print("Game over! You lose.")
                            print("The correct number was", secret_number)
                            print("Your guesses:", guessed_numbers)
                            game_over = True
    return ask_play_again()



def play_computer_guessing():
    low = 1
    high = 100
    attempts = 0
    computer_guesses = []
    game_over = False

    print()
    print("Reverse Mode! My turn to guess now.")
    print("Pick a number between 1 and 100 and I will guess it within 7 attempts.")
    print("After each guess, enter:")
    print("H if your number is higher")
    print("L if your number is lower")
    print("C if I am correct")

    ready = input("Are you ready? Enter Y to start! ")
    print_line()

    if ready == "Y" or ready == "y" or ready == "yes":
        while not game_over:
            if low > high:
                print("Wait... your answers don't make sense.")
                print("I think you lied to me. Then it's my win.")
                print("My guesses:", computer_guesses)
                game_over = True
            else:
                guess = (low + high) // 2
                attempts = attempts + 1
                computer_guesses.append(guess)

                print("Current possible range:", low, "-", high)
                print("My guess is:", guess)
                feedback = input("Is your number Higher, Lower, or Correct? Enter H, L, or C: ")
                print_line()
                
                if is_number(feedback):
                    print("Don't tell me the answer!! Just pick a new number now and I'll pretend that didn't happen.")
                    attempts = attempts - 1
                    computer_guesses.pop()
                elif feedback == "C" or feedback == "c" or feedback == "correct":
                    print("Got you!!")
                    print("Total attempts:", attempts)
                    print("My guesses:", computer_guesses)
                    game_over = True

                elif feedback == "H" or feedback == "h" or feedback == "higher":
                    low = guess + 1
                    print("Okay okay, I will guess higher.")

                elif feedback == "L" or feedback == "l" or feedback == "lower":
                    high = guess - 1
                    print("Fine, I will guess lower.")

                else:
                    print("Hey!! Just enter H, L, or C.")
                    attempts = attempts - 1
                    computer_guesses.pop()
    else:
        print("Too scared to let me guess? Fine.")

    return ask_play_again()

def ask_play_again():
    answer_valid = False
    play_again = True

    while not answer_valid:
        answer = input("Wanna play again? Enter Y or N: ")
        print_line()

        if answer == "Y" or answer == "y" or answer == "yes":
            play_again = True
            answer_valid = True
            print("I won't let you win this time.")
        elif answer == "N" or answer == "n" or answer == "no":
            confirm = input("Do you really want to quit? Please don't leave me..: ")
            print_line()

            if confirm == "Y" or confirm == "y" or confirm == "yes":
                print("Just kidding. You will never leave me. ^^")
            
            print("Yay! Welcome back!")

            play_again = True
            answer_valid = True
        else:
            print("Heyyy!! Just enter Y or N.")

    return play_again




def main():
    running = True
    best_scores = {
        "Easy Mode": 0,
        "Medium Mode": 0,
        "Hard Mode": 0
        }

    while running:
        print_menu()
        choice = input("Which one would you like to play today? ")
        print_line()

        if choice == "1":
            running = play_player_guessing("Easy Mode", 0, best_scores)
        elif choice == "2":
            running = play_player_guessing("Medium Mode", 10, best_scores)
        elif choice == "3":
            running = play_player_guessing("Hard Mode", 5, best_scores)
        elif choice == "4":
            running = play_computer_guessing()
        elif choice == "5":
            print("Did you really manage to escape me? Fine... for now.")
            running = False
        else:
            print("Don't know what you talking about.")


main()