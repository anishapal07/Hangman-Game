import random

def play_hangman():
    # 1. Small list of 5 predefined words
    word_list = ["python", "github", "coding", "developer", "script"]
    
    # Select a random word from the list
    secret_word = random.choice(word_list)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Text-Based Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    
    # 2. Main game loop (while loop)
    while incorrect_guesses < max_incorrect_guesses:
        # 3. Create the display word with guessed letters and underscores (strings/lists)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                
        print(f"\nCurrent word: {display_word.strip()}")
        
        # Check if the player has won (no more underscores)
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: '{secret_word}'!")
            break
            
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        
        # Get player input
        guess = input("Guess a single letter: ").lower()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
            
        # Add valid guess to the list of guessed letters
        guessed_letters.append(guess)
        
        # 4. Check if the guess is correct (if-else)
        if guess in secret_word:
            print("Good guess!")
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1
            
    # Check if the player lost by running out of guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame Over! You've run out of guesses.")
        print(f"The correct word was: '{secret_word}'")

# Run the game
if __name__ == "__main__":
    play_hangman()