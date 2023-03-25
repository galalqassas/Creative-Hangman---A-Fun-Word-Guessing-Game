from functions import *
filename = set_language() + '.txt'
words_list = is_file_exist(filename)
word = get_random_word(words_list)
play(word)
while would_the_user_like_to_play_again():
    play(word)
