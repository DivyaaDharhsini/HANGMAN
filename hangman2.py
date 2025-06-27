import random
print("Welcome to Hangman!\n")
know_rules = input("Do you know the rules? (Yes/No): ").strip().lower()

if know_rules == 'no':
    print("\n📜 HANGMAN RULES:")
    print("- Your goal is to save the Stickman before he hangs! \n")
    print("- A random word will be chosen.")
    print("- You must guess the word one letter at a time.")
    print("- You have 6 incorrect guesses before you lose.")
    print("- Repeated guesses don’t cost you, but they don't help either.")
    print("- The game ends when you guess all letters or run out of attempts.\n")

while True:
    words = ['python', 'hangman', 'computer', 'science',"apple", "beach", "chair", "dance", "earth", "flower", "grape", "happy", "island", "juice"]
    word = random.choice(words)
    guesses = ['_'] * len(word)
    attempt = 6
    used_letters = []
   

    while attempt > 0 and '_' in guesses:
        print('Word:', ' '.join(guesses))
        print('Used:', ', '.join(used_letters))
        guess = input('\nGuess a letter: ').lower()

        if guess in used_letters:
            print("Already guessed!")
            continue

        used_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guesses[i] = guess
        else:
            attempt -= 1
            print(f"Wrong! {attempt} attempts left.")

    if '_' not in guesses:
        print("\nCongrats you saved the Stickman! 🕺")
        print("The word was:", word)
    else:
        print("\nYou lost! The word was:", word)
        print("No worries, even legends lose sometimes! Try again!")
       
    play_again = input("\nDo you want to play again? (Yes/No): ").strip().lower()
    if play_again != 'yes':
        print("\nThanks for playing Hangman! Goodbye! <3\n")
        break

input("\nPress Enter to exit...")
