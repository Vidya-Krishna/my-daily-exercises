#QUIZ 
questions = (("Seaweeds are an important source of which of the following?"),
      ("The ____ is the stem-like part of the leaf that joins the blade to the stem, is known as:"),
      ("Among the given nutrients, milk is a poor source of which of the following?"),
      ("Which gas is major contributor to greenhouse effect?"),
      ("Which word is common in the botanical names of trees like Ashoka, Tamarind or Coral?"))
options = (("[A] Iron", "[B] Chlorine", "[C] Bromine", "[D] Iodine"),
           ("A] Vein",  "[B] Petiole",  "[C] Stipules","[D] Midrib"),
           ("[A] Carbohydrate", "[B] Calcium", "[C] Protein", "[D] Vitamin C"),
           ("[A] Chloroflurocarbon", "[B] Nitrogen dioxide", "[C] Sulphur dioxide", "[D] Carbon dioxide"),
           ("[A] Terminalia", "[B] Indica", "[C] Salix", "[D] Acacia"),)
key = ("d","b","c","d","b")
j_count = 0
score  = 0
for i in questions:
      print()
      print(i)
      for j in options[j_count]:
            print(j)
      entered_option = input("Choose an answer: ").lower()
      if entered_option == key[j_count]:
            print('You nailed it!!!')
            score += 1
      else:
            print('Better luck next question')
            print(f'correct answer is {key[j_count]}')
            
      j_count += 1
print('Your score is: ', score)

#There are a bunch of things I want to add but those things are breaking this. 

      

