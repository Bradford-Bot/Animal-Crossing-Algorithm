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
# ANTEATER
if species == "anteater":
  # ANTEATER - YELLOW
  anteaterColor = input("What is the main color of this Villager? ").lower()
  if anteaterColor == "yellow":
      print()
      print("\033[33m" "Is the Villager you're looking for named Anabelle?" "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
  # ANTEATER - GREEN
  if anteaterColor == "green":
      print()
      print("\033[32m" "Is the Villager you're looking for named Pango?" "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
  # ANTEATER - WHITE
  if anteaterColor == "white":
      print()
      # ANTEATER - SECONDARY COLOR
      antColorTwo = input("Is the secondary color of your Villager" 
      " cyan or black? ").lower()
      # ANTEATER - SECONDARY COLOR (CYAN)
      if antColorTwo == "cyan":
        print()
        print("\033[36m" "Is the Villager you're looking for named Zoe?" "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("ADD CHARACTER INFO PAGE")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
      # ANTEATER - SECONDARY COLOR (BLACK)
      if antColorTwo == "black":
        print()
        anteaterBOG = input("Is the Villager you're looking for a" "\033[34m" " boy " 
                            "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                            "\033[30m""\033[37m""? ""\033[0m").lower()
        # ANTEATER - SECONDARY COLOR (BLACK/BOY)
        if anteaterBOG == "boy":
          print()
          print("\033[30m" "Is the Villager you're looking for named Antonio?" 
                "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("ADD CHARACTER INFO PAGE")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
        # ANTEATER - SECONDARY COLOR (BLACK/GIRL)
        if anteaterBOG == "girl":
          print()
          print("\033[30m" "Is the Villager you're looking for named Annalisa?" 
                "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("ADD CHARACTER INFO PAGE")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
  # ANEATER - ORANGE
  if anteaterColor == "orange":
    print()
    anteaterTraits = input("Does this villager have bangs or eyebrows? ").lower()
    if anteaterTraits == "bangs":
      print()
      print("\033[33m" "Is the Villager you're looking for named Olaf?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if anteaterTraits == "eyebrows":
      print()
      print("\033[33m" "Is the Villager you're looking for named Cyrano?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
  # ANTEATER - PINK
  if anteaterColor == "pink":
    print()
    print("\033[35m" "Is the Villager you're looking for named Snooty?""\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("ADD CHARACTER INFO PAGE")
    if yn == "no":
      print()
      print("Sounds like a you problem.")
