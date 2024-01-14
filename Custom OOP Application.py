import random

class Hangman:
    def __init__(self, word):
        self.word = word.upper()
        self.guesses = set()
        self.max_attempts = 6

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guesses:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        return displayed_word.strip()

    def make_guess(self, letter):
        letter = letter.upper()
        if letter in self.guesses:
            print("You've already guessed that letter. Try again.")
        elif letter in self.word:
            print("Good guess! '{}' is in the word.".format(letter))
            self.guesses.add(letter)
        else:
            print("Incorrect guess. '{}' is not in the word.".format(letter))
            self.max_attempts -= 1
            self.guesses.add(letter)

    def is_game_over(self):
        if self.max_attempts == 0:
            print("Sorry, you've run out of attempts. The word was '{}'.".format(self.word))
            return True
        elif set(self.word) <= self.guesses:
            print("Congratulations! You've guessed the word: '{}'.".format(self.word))
            return True
        return False

def choose_word():
    words = ["informatyka", "python", "gra", "dawid", "jurczynski", "sprawozdanie", "zadanie", "napoleon", "austria", "polska"]
    return random.choice(words)

def main():
    chosen_word = choose_word()
    game = Hangman(chosen_word)

    print("Welcome to Hangman!")
    print(game.display_word())

    while not game.is_game_over():
        guess = input("Guess a letter: ")
        game.make_guess(guess)
        print("Word: {}".format(game.display_word()))
        print("Attempts left: {}".format(game.max_attempts))
        print()

if __name__ == "__main__":
    main()