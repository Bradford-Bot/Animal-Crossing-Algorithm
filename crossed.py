print("\033[32m" "Animal Crossing" "\033[0m")
print("")
print("\033[32m" "Looking for a villager and can't put your finger on what their name"
" is? Answer the questions below and find out!" "\033[0m")
print("")
species = input("What species is your villager? ").lower()
print()
# ALLIGATOR
if species == "alligator":
  gatorColor = input("What is the main color of this Villager? ").lower()
  print()
  #ALLIGATOR - YELLOW
  if gatorColor == "yellow":
    gatorPattern = input("Is the pattern on this Villager camo or circles? ").lower()
    #ALLIGATOR - CAMO
    if gatorPattern == "camo":
      print()
      print("\033[33m" "Is the Villager you're looking for named Sly?" "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    #ALLIGATOR - CIRCLES
    if gatorPattern == "circles":
      print()
      print("\033[33m" "Is the Villager you're looking for named Alfonso?" "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
  #ALLIGATOR - BLUE
  if gatorColor == "blue":
    print("\033[36m" "Is the Villager you're looking for named Alli?" "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("ADD CHARACTER INFO PAGE")
    if yn == "no":
      print()
      print("Sounds like a you problem.")
  #ALLIGATOR - GREEN
  if gatorColor == "green":
    gatorTraits = input("Does this Villager look happy or angry? ").lower()
    #ALLIGATOR - HAPPY
    if gatorTraits == "happy":
      print()
      print("\033[32m""Is the Villager you're looking for named Boots?""\033[0m")
      print()
      yn = input("Yes or No? ")
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sucks for you.")
    #ALLIGATOR - ANGRY
    if gatorTraits == "angry":
      print()
      print("\033[32m""Is the Villager you're looking for named Drago?""\033[0m")
      print()
      yn = input("Yes or No? ")
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sucks for you.")
  #ALLIGATOR - PURPLE
  if gatorColor == "purple":
    print("\033[35m" "Is the Villager you're looking for named Del?" "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("ADD CHARACTER INFO PAGE")
    if yn == "no":
      print()
      print("Sounds like a you problem.")
  # ALLIGATOR - PINK
  if gatorColor == "pink":
    print("\033[31m" "Is the Villager you're looking for named Gayle?" "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("ADD CHARACTER INFO PAGE")
    if yn == "no":
      print()
      print("Sounds like a you problem.")
  # ALLIGATOR - BROWN
  if gatorColor == "brown":
    print("\033[33m" "Is the Villager you're looking for named Rosewell?" "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("ADD CHARACTER INFO PAGE")
    if yn == "no":
      print()
      print("Sounds like a you problem.")
