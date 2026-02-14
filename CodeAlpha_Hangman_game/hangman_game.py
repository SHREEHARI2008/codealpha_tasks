import random

# Predefined list of words
words = ["python", "computer", "science", "keyboard", "program"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Display blanks
hidden_word = ["_"] * len(word)

while incorrect_guesses < max_incorrect and "_" in hidden_word:
    print("\nWord:", " ".join(hidden_word))
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)
    
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        print("❌ Wrong guess!")
        incorrect_guesses += 1

# Game result
if "_" not in hidden_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The correct word was:", word)
