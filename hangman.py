import random

# Hangman stages (visuals)
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

# Words and hints
WORDS = [
    ("python", "A popular programming language"),
    ("elephant", "A large land animal with a trunk"),
    ("guitar", "A musical instrument with strings"),
    ("astronaut", "A person trained for space travel"),
    ("pyramid", "Famous triangular structure in Egypt"),
]

# Choose a random word and hint
word, hint = random.choice(WORDS)
guessed = ["_"] * len(word)
tries = 0
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Hint:", hint)

while tries < len(HANGMAN_PICS) - 1:
    print(HANGMAN_PICS[tries])
    print("Word: " + " ".join(guessed))
    print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("✅ Good guess!\n")
    else:
        tries += 1
        print("❌ Wrong guess!\n")

    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
        break
else:
    print(HANGMAN_PICS[tries])
    print("💀 Game Over! The word was:", word)
