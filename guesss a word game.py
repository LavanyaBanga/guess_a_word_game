import random

def select_word():
    word_list = ["HTML", "Database", "Java", "Python", "CSS"]
    return random.choice(word_list)

def play_game():
    word = select_word()
    guessed_letters = []
    attempts = 6

    print("The selected word is:", word)  

    while attempts > 0:
        print("Attempts left:", attempts)
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        guess = input("Guess a letter or the whole word: ").lower()
        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess.lower() in word.lower(): 
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                attempts -= 1
        elif len(guess) == len(word) and guess.isalpha():
            if guess.lower() == word.lower():
                print("Congratulations buddy!! You guessed the word:", word)
                break
            else:
                print("Incorrect guess!")
                attempts -= 1
        else:
            print("Invalid input! Please enter a single letter or the whole word.")

        if set(word.lower()) == set(guessed_letters):
            print("Congratulations buddy!! You guessed the word:", word)
            break

    if attempts == 0:
        print("Game over! The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing!")

play_game()