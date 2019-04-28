import json
from difflib import get_close_matches


collection = json.load(open("collection.json"))


def get(word):
   
      
       word = word.lower()
       
       if word in collection:
          print(collection[word])
          word_search = input("Do you want to search another word (Y or N): ")
          if word_search == "Y":
                   word = input("Enter word: ")
                   output = get(word)
          else:
              return("Goodbye!")
          
       elif len(get_close_matches(word, collection.keys())) > 0:
           word_search = input("Are you looking for the word %s ? Enter Y for Yes or N for No: " % get_close_matches(word, collection.keys())[0])
           if word_search == "Y":
               print( collection[get_close_matches(word, collection.keys())[0]])
               word_search = input("Do you want to search another word (Y or N): ")
               if word_search == "Y":
                   word = input("Enter word: ")
                   output = get(word)
               else:
                   return("Goodbye!")
                
               return("Goodbye!")
           if word_search == "N":
               print( "Word not found. Please try again.")
               word_search = input("Do you want to search another word (Y or N): ")
               if word_search == "Y":
                   word = input("Enter word: ")
                   output = get(word)
               else:
                   return("Goodbye!")
       return("Goodbye!")
           

print('\n***** WELCOME TO THE PYTHON ENGLISH DICTIONARY *****\n')
word = input("Enter word: ")
output = get(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
