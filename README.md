# Hangman-Script

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Use `python Hangman.py` to execute script

## Description

I made a python script that allows to play hangman from the console. The user will have 6 tries to find the word, in case of running out of tries he will lose.

## Technologies used

1. Python

## Libraries used

1. random

## Galery

![hangman-script](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/hangman-0.jpg)

![hangman-script](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/hangman-1.jpg)

![hangman-script](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/hangman-2.jpg)

![hangman-script](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/hangman-3.jpg)

![hangman-script](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/hangman-4.jpg)

## Portfolio Link

`https://diegolibonati.github.io/DiegoLibonatiWeb/#/projects?q=Hangman%20Script`

## Video

https://user-images.githubusercontent.com/99032604/198900729-70cad371-f6ca-4429-9305-ed48bedbb491.mp4

## Documentation

The variable `intents` refers to the remaining attempts the user has before losing. The `count_letter` variable refers to the length of the word to be guessed but in this one 1 will be added each time a letter is found above the word to be guessed. The `list_words` list refers to the words that can be selected by the computer for guessing. The variable `letters_used` refers to the letters that were used. The `random_word` variable refers to a word chosen at random from the `list_words`. Finally the variable `len_word` refers to the length of the selected word:

```
intents = 6
count_letter = 0
list_words = ["casa", "casita", "externo", "libreria", "jorge", "nafta", "arrancar"]
letters_used = []
random_word = choice(list_words).upper()
len_word = len(random_word)
```

The `generate_secret_word()` function will return the length of the word but in `*`. If the word is `Home` it will return `****`. Then this function will be assigned to the variable `generate_new_word`:

```
def generate_secret_word(len_word):
    return "-" * len_word

generate_new_word = generate_secret_word(len_word)
```

The function `check_if_letter_is_in_word()` basically as its name indicates checks that the letter we type is in the word that was chosen to guess. If it is not it will be added to the list of letters used and if it is the user will be asked to play another letter. If it is found a message that the letter was found will be displayed and the letter will be shown in the word in the console, if the complete word was found the player will win and if it is not found an attempt will be subtracted:

```
def check_if_letter_is_in_word(letter_selected, random_word, letters_list):

    global count_letter
    global intents
    global generate_new_word

    letter_in_word_times = 0

    if letter_selected in random_word and len(letter_selected) == 1 and letter_selected not in letters_list:
        check_letters_used(letters_used, insert_letter)
        for index, letter in enumerate(random_word):
            if letter == letter_selected:
                list_word = list(generate_new_word)
                list_word[index] = letter_selected
                generate_new_word = ''.join(list_word)
                count_letter+=1
                letter_in_word_times+=1
    elif letter_selected == random_word:
        count_letter = len(random_word)
        return print("NICE")
    elif letter_selected in letters_list:
        return check_letters_used(letters_used, insert_letter)
    else:
        check_letters_used(letters_used, insert_letter)
        intents -= 1

    return print(f"¡The letter is in word {letter_in_word_times} times!. Your progress: {generate_new_word}. Intents remaning: {intents}")
```

The `check_letters_used()` function basically checks if the chosen letter is in the `letters_list` if it is it will ask the user to play another letter, if not it will add it to the list:

```
def check_letters_used(letters_list, letter):
    if letter not in letters_list:
        letters_list.append(letter)
    else:
        return print("Try another letter...")

    return print(f"Letters used: {letters_list}")
```

As long as the user has attempts to continue playing and has not guessed the word, he/she can continue playing:

```
while intents != 0 and count_letter < len_word:
    insert_letter = input("Select a letter: ").upper()
    check_if_letter_is_in_word(insert_letter, random_word, letters_used)
```

If the user wins, a message will be displayed and if the user loses, another message will be displayed:

```
if count_letter == len_word or insert_letter == random_word:
    print("YOU WIN")
else:
    print("YOU LOSE")
```
