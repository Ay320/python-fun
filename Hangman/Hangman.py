import random
import Hangman_names
import Hangman_art

word_list = Hangman_names.word_list
logo = Hangman_art.logo
stages = Hangman_art.stages

chosen_word = random.choice(word_list)
lives = 6   # lives remaining

# logo:
print(logo)
#Testing code:
print(f'Pssst, the solution is {chosen_word}.')
# initialise _ list:
display = []
end_of_game = False

for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # if user enter a letter that was already guessed true:
    if guess in display:
        print(f"You've already guessed {guess}")

    life_lost = True    # keep track of lives
    # or use: if guess not in chosen_word

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            life_lost = False

    if life_lost:
        lives-=1
        print(f"'{guess}' was not in the word, you lost a life")

    print(f"{' '.join(display)}")  # display the list as a string

    if lives == 0 :
        end_of_game = True
        print("You lost!")

    if "_" not in display:
        end_of_game = True
        print("You Won!")

    print(stages[lives])