import random
import os
import time
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def read_file(filename):
    """Get data from a file"""
    words_list = []
    with open(filename, "r") as f:
        for line in f:
            words_list.append(line.strip('\n'))
    return words_list


# Get a random word from the file
def get_random_word(words_list):
    """This function chooses a random word"""
    word = random.choice(words_list)
    return word.upper()


def calc_chances(level):
    """This function is used to calc the chances"""
    if level == 'easy':
        tries = 7
    elif level == 'medium':
        tries = 5
    elif level == 'hard':
        tries = 3
    else:
        tries = 3
    return tries


# Play the game
def show_spaces(f_word):
    """This function take a word. shows some letters and hides the other"""
    spaced_word = ["_" for number in range(len(f_word))]
    enumerated_list = list(enumerate(f_word))
    showed_letters = random.sample(f_word, k=int(len(f_word) / 2))
    diminished_letters = []
    for i in f_word:
        if i not in showed_letters:
            diminished_letters.append(i)
    for a_tuple in enumerated_list:
        if a_tuple[1] in showed_letters:
            spaced_word[a_tuple[0]] = a_tuple[1]
    return spaced_word

def calc_time(previous_time):
    """Calculates the time between every user input."""
    current_time = time.time()
    spent_time = current_time - previous_time
    return spent_time


def is_file_exist(filename):
    """Checks if the file exists"""
    if os.path.exists(filename):
        words_list = read_file(filename)
    else:
        print("file doesn't exist")
    return words_list



def get_high_score():
    """Gets the current high score from a file."""
    with open("high_score.txt", "r") as f:
        high_score = int(f.read())
    return high_score


def is_valid(user_guess):
    if len(user_guess) > 1:
        return False
    elif user_guess not in letters:
        return False
    else:
        return True


def play(word):
    """This function let you play the game."""
    score = 0
    previous_time = time.time()
    word = word
    blank_word = ''.join(show_spaces(word))
    used_letters = []
    level = input('Choose between "easy", "medium" and "hard": ').lower()
    while level != 'easy' and level != 'medium' and level != 'hard':
        level = input('Error, please choose again: ').lower()
    tries = calc_chances(level)
    print("Let's start playing:" + blank_word)
    guess = input("Enter a letter: ").upper()
    while not is_valid(guess):
        guess = input("Error! Enter a valid guess: ").upper()
    elapsed_time = calc_time(previous_time)
    previous_time = time.time()
    while tries > 1:
        if guess in used_letters:
            print("You already guessed the letter ", guess)
        elif guess in word:
            score = calc_score(elapsed_time, score)
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += blank_word[i]
            blank_word = new
            print(blank_word)
            print("Your current score is: ", score)
            print("Hey, you guessed the correct letter")
        else:
            print("Sorry, your guess is incorrect. Guess again.")
            used_letters.append(guess)
            tries -= 1
            print(f"You have {tries} guesses left")

        if "_" not in blank_word:
            print("Congratulations you won!")
            user_level = evaluation(calc_time(previous_time), len(word))
            print(f'You got {user_level} in our test.')
            break

        guess = input("Enter a letter: ").upper()
        while not is_valid(guess):
            guess = input("Error! Enter a valid guess: ").upper()
    else:
        print("Sorry you ran out of guesses. The word was {}.".format(word))
    high_score = get_high_score()
    print("High Score: ", high_score)
    update_high_score(score, high_score)

def update_high_score(score, high_score):
    """Updates the high score and writes it to a file."""
    if score > high_score:
        high_score = score
        with open("high_score.txt", "w") as f:
            f.write(str(high_score))
    return high_score


def calc_score(elapsed_time, score):
    """Calculates the score based on the elapsed time of user input."""
    if elapsed_time <= 10:
        score += 200
    elif elapsed_time <= 20:
        score += 100
    return score


def set_language():
    language = input("Choose between English, French, and Spanish: ").title()
    while language != "English" and language != "French" and language != "Spanish":
        language = input("Choose a valid language, please. ").title()
    return language


def evaluation(time, word_length):
    if time < 30 and word_length > 7:
        return "C+"
    elif time >= 30 and time < 60 and word_length > 7:
        return "C"
    elif time < 30 and word_length == 7:
        return "B+"
    elif time >= 30 and time < 60 and word_length == 7:
        return "B"
    elif time < 30 and word_length < 7:
        return "A+"
    elif time >= 30 and time < 60 and word_length < 7:
        return "A"


def would_the_user_like_to_play_again():
    play_again = input("Did you enjoy the game? If you would like to play again, click 1. if not, click 2: ")
    while play_again != '1' and play_again != '2':
        play_again = input("Error! Choose a valid input, click 1 to play again or 2: ")
    if play_again == '1':
        return True
    if play_again == '2':
        return False
