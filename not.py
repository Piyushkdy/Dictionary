import json
from difflib import get_close_matches


collection = json.load(open("collection.json"))


def lookup(word):
   
      
       word = word.lower()
       if word in collection:
          print(collection[word])
          yn = input("Do you want to search another word (Y or N): ")
          if yn == "Y":
                   word = input("Enter word: ")
                   output = lookup(word)
          else:
              return("Goodbye!")
          
       elif len(get_close_matches(word, collection.keys())) > 0:
           yn = input("Are you looking for the word %s ? Enter Y for Yes or N for No: " % get_close_matches(word, collection.keys())[0])
           if yn == "Y":
               print( collection[get_close_matches(word, collection.keys())[0]])
               yn = input("Do you want to search another word (Y or N): ")
               if yn == "Y":
                   word = input("Enter word: ")
                   output = lookup(word)
               else:
                   return("Goodbye!")
                
               return("Goodbye!")
           if yn == "N":
               print( "Word not found. Please try again.")
               yn = input("Do you want to search another word (Y or N): ")
               if yn == "Y":
                   word = input("Enter word: ")
                   output = lookup(word)
               else:
                   return("Goodbye!")
       return("Goodbye!")
           

print('\n***** WELCOME TO THE PYTHON ENGLISH DICTIONARY *****\n')
word = input("Enter word: ")
output = lookup(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
