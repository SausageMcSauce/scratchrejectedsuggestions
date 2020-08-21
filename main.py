from tolorslist import tolorslist

searchopt = input("Search by number (n) or keyword? (k)")

if searchopt in ["N", "n"]:
  selection = input("What number are you searching for?")
  if selection in tolorslist:
    print("\n", tolorslist[selection])
    print("Copy and past into forum post.")
  else:
    print("Either this rejected suggestion does not exist or it has not been implemented yet. Rerun this program to try again.")
elif searchopt in ["K", "k"]:
  print("Searching rejected suggestions by keywork has not been implemented yet.")
else:
  print("Invalid option. Rerun the program to try again.")