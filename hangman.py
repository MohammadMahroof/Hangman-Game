from hangman_art import stages, logo
from hangman_words import word_list
import random

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
word_length = len(chosen_word)

placeholder = ""
for position in range(word_length):
    placeholder+="_"
print("Word to guess : " + placeholder)    

game_over = False
correct_letters = []

while not game_over:
    print(f"**************************************{lives}/6 Lives left**************************************")

    guess = input("Guess a letter :")
    if guess in correct_letters:
        print(f"Yo have already guessed {guess}!")
    
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"

    print(f"Word to guess : {display}")

    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess}, that's not in word {chosen_word}. You lose a life.") 
        if lives == 0:
            game_over = True
            print(f"**************************************IT WAS {chosen_word}!, YOU LOSE**************************************")

    if "_" not in display:
        game_over = True
        print("**************************************YOU WIN**************************************")                       


    print(stages[lives])    