# Project 2
# This program is a word game that is similar to anagrams.
# Date Completed: 6/1/23
import random

alphabet = 'aaabcdeeefggghijkklmnoooppprsssttttuuuwy'

six_letters = []

vowels = ["a", 'e', 'i', 'o', 'u']

for i in range(6):
  index = random.randint(0, 39)
  six_letters.append(alphabet[index])
there_are_vowels = False
for i in six_letters:
  if i in vowels:
    there_are_vowels = True
if there_are_vowels == False:
  six_letters[1] = "a"

wordfile = open("words.txt", 'r')
word_string = wordfile.read()
word_string.replace("\n", "")
word_list = word_string.split()
word_set = set(word_list)
inputted_words = []
possible_words = []

for word in word_set:
  add_word = True
  for letter in word:
    if letter not in six_letters:
      add_word = False

  if add_word == True:
    possible_words.append(word)


def uses_letters(user_input):
  for i in user_input:
    if i not in six_letters:
      return False


def is_real_word(user_input):
  if user_input in word_set:
    inputted_words.append(user_input)
    return True
  else:
    return False


def main():
  points = 0
  keep_going = True
  print("Welcome to Anagrams!")
  print("\nA. PLAY\nB. RULES\nC. LEAVE")

  choice = input('\nChoose a b or c: ')
  if choice == "a":
    string = ""
    for i in six_letters:
      string += i.upper() + " "
    print(string)
    while keep_going == True:
      userinput = input("\nType a word using the letters above:")
      userinput = userinput.lower()
      if userinput == "leave":
        print(f"\nfinal score: {points}")
        scorefile = open("scores.txt", "a")
        scorefile.write("\n" + str(points))
        choice2 = input("\nWould you like to see all the possible words?")
        if choice2 == "yes":
          for i in possible_words:
            print(i)
          print("\nThanks for playing")
          break
        else:
          print("\nThanks for playing")
          break
      elif uses_letters(userinput) == False:
        print("\nYou can only use the letters in the list above")
      elif userinput in inputted_words:
        print("You already entered that word")
      elif is_real_word(userinput) == True:
        if userinput not in possible_words:
          print("You can only use each letter once!")
        else:
          points += len(userinput) * 100
        print(f"score:{points}")
      elif is_real_word(userinput) == False:
        print("\nThat's not a word!")
        print(f"score:{points}")

  elif choice == "b":
    print("\nHOW TO PLAY:")
    print(
      "\nWith six given letters, try to create as many words as possible! You can only use each letter once.\nAnytime you want to leave, type 'leave'"
    )
    input()
    main()
  else:
    print("Thanks for playing")


main()
