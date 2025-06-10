# CLI string operations code.
#count_vowels(word), reverse_string(s), is_palindrome(text), string_sort(words)
            
                    # count_vowels(word)
# def count_vowels(user_input_word):
#     # word_list = []
#     # for i in user_input_word: word_list.append(i)
#     vowels_occurences = {}
#     vowels = ["a", "e", "i", "o", "u"]
#     for i in vowels:
#         count = 0
#         for j in user_input_word:
#             if i == j: count += 1       
#         vowels_occurences[i] = count
#     print(vowels_occurences)
#     total = 0
#     for value in vowels_occurences.values():
#         print(value)
#         total += value
#     print("vowels = ", total)

# # wow = True
# # while wow:
# user_input_word = input("Enter a string to check vowel occurences: ").lower()
# print("~~~~~*** ** * ** ***~~~~~")
# print(user_input_word)#
# # print(f"{user_input_word} has {count_vowels(user_input_word)}")
# count_vowels(user_input_word)
#                                 #--------------------------------
# input = input("Enter a string to check vowel occurences: ").lower()
# print(input.count("a"))
# print(input.count("e"))
# print(input.count("i"))
# print(input.count("o"))
# print(input.count("u"))
                                #--------------------------------
                    # I ---------------------------------

def count_vowels(user_input_word: str):
    # word_list = []
    # for i in user_input_word: word_list.append(i)
    vowels_occurences = {}
    vowels = ["a", "e", "i", "o", "u"]
    for i in vowels:
        count = 0
        for j in user_input_word:
            if i == j: count += 1       # if i in j did not give me any error!
        vowels_occurences[i] = count
    print(vowels_occurences)
    total = 0
    for value in vowels_occurences.values():
        print(value)
        total += value
    print("vowels = ", total)

                    # II ---------------------------------
def reverse_string(s) -> str:
    print(s.lower()[::-1])

                    # III ---------------------------------
def is_palindrome(text) -> bool:
    reverse_text = text.lower()[::-1]
    return (reverse_text == text.lower())
                    # IV ---------------------------------
def string_sort(words: list) -> list:
    sorted_words = sorted(words)
    print(words)
    print(sorted_words)
    # words.sort()
    # print(words)

while True:
    print("""1. counts vowels \n2. reverse a string \n3. check if it is a palindrome \n4. to sort a list of strings \n5. to exit!""")
    user_option = int(input("Choose and enter a number from above: "))
    match user_option:
        case 1: 
            user_input_word = input("Enter a string to check vowel occurences: ").lower()
            print("~~~~~*** ** * ** ***~~~~~")
            print(user_input_word)#
            count_vowels(user_input_word)
            print("~~~~~*** ** * ** ***~~~~~")
        case 2: 
            print("~~~~~*** ** * ** ***~~~~~")
            s = input("Enter a string to reverse it: ")
            reverse_string(s)
            print("~~~~~*** ** * ** ***~~~~~")
        case 3: 
            print("~~~~~*** ** * ** ***~~~~~")
            text = input("Enter a string to check if it is a plaindrome: ")
            is_palindrome(text)
            print("~~~~~*** ** * ** ***~~~~~")
        case 4: 
            print("~~~~~*** ** * ** ***~~~~~")
            words = input("Enter words separated by spaces, to sort them: ").split()
            string_sort(words)
            print("~~~~~*** ** * ** ***~~~~~")
        case 5: 
            break
        case _: 
            print("~~~~~*** ** * ** ***~~~~~")
            print("Invalid input, please select nly from 1 to 5")
            print("~~~~~*** ** * ** ***~~~~~")


                    # I ---------------------------------

def count_vowels(user_input_word: str):
    # word_list = []
    # for i in user_input_word: word_list.append(i)
    vowels_occurences = {}
    vowels = ["a", "e", "i", "o", "u"]
    for i in vowels:
        count = 0
        for j in user_input_word:
            if i == j: count += 1       # if i in j did not give me any error!
        vowels_occurences[i] = count
    print(vowels_occurences)
    total = 0
    for value in vowels_occurences.values():
        print(value)
        total += value
    print("vowels = ", total)

                    # II ---------------------------------
def reverse_string(s) -> str:
    print(s.lower()[::-1])

                    # III ---------------------------------
def is_palindrome(text) -> bool:
    reverse_text = text.lower()[::-1]
    if len(text) % 2 == 0: print(True)
    elif reverse_text == text.lower():print(True)
    else: print(False)

                    # IV ---------------------------------
def string_sort(words: list) -> list:
    sorted_words = sorted(words)
    print(words)
    print(sorted_words)
    # words.sort()
    # print(words)

while True:
    print("""1. counts vowels \n2. reverse a string \n3. check if it is a palindrome \n4. to sort a list of strings \n5. to exit!""")
    user_option = int(input("Choose and enter a number from above: "))
    match user_option:
        case 1: 
            user_input_word = input("Enter a string to check vowel occurences: ").lower()
            print("~~~~~*** ** * ** ***~~~~~")
            print(user_input_word)#
            count_vowels(user_input_word)
            print("~~~~~*** ** * ** ***~~~~~")
        case 2: 
            print("~~~~~*** ** * ** ***~~~~~")
            s = input("Enter a string to reverse it: ")
            reverse_string(s)
            print("~~~~~*** ** * ** ***~~~~~")
        case 3: 
            print("~~~~~*** ** * ** ***~~~~~")
            text = input("Enter a string to check if it is a plaindrome: ")
            is_palindrome(text)
            print("~~~~~*** ** * ** ***~~~~~")
        case 4: 
            print("~~~~~*** ** * ** ***~~~~~")
            words = input("Enter words separated by spaces, to sort them: ").split()
            string_sort(words)
            print("~~~~~*** ** * ** ***~~~~~")
        case 5: 
            break
        case _: 
            print("~~~~~*** ** * ** ***~~~~~")
            print("Invalid input, please select nly from 1 to 5")
            print("~~~~~*** ** * ** ***~~~~~")



#---------------------------------------------------------------------------------------------------
#just another num_guessing code
import random

def mini_proj_num_guess():
  low = 1
  high = 100
  cg = random.randint(low, high)
  gc = 0
  is_running = True
  
  while is_running:
    n = input(f'Guess an int between {low}, {high}: ')

    if n.isdigit():
      n = int(n)
      if n < 0 or n > 100:
        print(f'range bound error, please enter an int between {low}, {high} ')
      elif n > cg:
        gc += 1
        print('cold, try a lower number')
      elif n < cg:
        gc += 1
        print('hot, try a high number')
      else:
        gc += 1
        print(f'correct, it matched in {gc} times')
        is_running = False
    else:
      invalid_gc += 1
      print('please enter an **int**  between {low}, {high} ')

mini_proj_num_guess()

#passed for inputs: space, just return/enter, -ve inputs, out of range ints
#need to add Difficulty levels (e.g., fewer attempts allowed) | Tracking all previous guesses | Scoring system

