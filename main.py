from tolorslist import tolorslist
from keywordshandle import keyword_handler

searchopt = input("Search by number (n) or keyword? (k) ")

if searchopt.lower() == "n":
  selection = input("What number are you searching for? ")
  if selection in tolorslist:
    print("\n", tolorslist[selection])
    print("Copy and past into forum post.")
  else:
    print("Either this rejected suggestion does not exist or it has not been implemented yet. Rerun this program to try again.")
elif searchopt.lower() == "k":
  selection = input("Enter a keyword ")
  selection = selection.lower()
  print(keyword_handler(selection))
  print("Copy and paste into forum post.")
else:
  print("Invalid option. Rerun the program to try again.")