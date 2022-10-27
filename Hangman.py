from random import choice

intents = 6
count_letter = 0
list_words = ["casa", "casita", "externo", "libreria", "jorge", "nafta", "arrancar"]
letters_used = []
random_word = choice(list_words).upper()
len_word = len(random_word)

def generate_secret_word(len_word):
    return "-" * len_word

generate_new_word = generate_secret_word(len_word)

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

def check_letters_used(letters_list, letter):
    if letter not in letters_list:
        letters_list.append(letter)
    else: 
        return print("Try another letter...")

    return print(f"Letters used: {letters_list}")

print(f"The word has {len_word} letters. Try: {generate_secret_word(len_word)}")


while intents != 0 and count_letter < len_word:
    insert_letter = input("Select a letter: ").upper()
    check_if_letter_is_in_word(insert_letter, random_word, letters_used)

if count_letter == len_word or insert_letter == random_word:
    print("YOU WIN")
else:
    print("YOU LOSE")