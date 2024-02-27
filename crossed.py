print()
print("\033[32m" "Animal Crossing" "\033[0m")
print("")
print("\033[32m" "Looking for a villager and can't put your finger on what their name"
" is? Answer the questions below and find out!" "\033[0m")
print("")
species = input("What species is your villager? ").lower()
print()
#SPECIAL
if species == "special":
  print("Samantha: Tangy!")
  print("Cameron: Katt!")
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
      yn = input("Yes or No? ").lower()
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
#BULL
if species == "bull":
  # BULL - ORANGE
    bullColor = input("What is the color of this Villager? ").lower()
    if bullColor == "orange":
      print()
      print("\033[33m" "Is the Villager you're looking for named Angus?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
  # BULL - YELLOW
    if bullColor == "yellow":
      print()
      print("\033[33m" "Is the Villager you're looking for named Coach?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
  # BULL - BLUE
    if bullColor == "blue":
      print()
      print("\033[34m" "Is the Villager you're looking for named Stu?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
  # BULL - BROWN
    if bullColor == "brown":
      print()
      print("\033[33m" "Is the Villager you're looking for named Vic?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# BEAR
if species == "bear":
  bearColor = input("What is the color of this bear? ").lower()
  # BEAR - GREEN
  if bearColor == "green":
      print()
      print("\033[32m" "Is the Villager you're looking for named Charlise?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
  # BEAR - YELLOW
  if bearColor == "yellow":
      print()
      print("\033[33m" "Is the Villager you're looking for named Nate?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
  # BEAR - PURPLE
  if bearColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Megan?""\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
  # BEAR - PINK
  if bearColor == "pink":
    print()
  bearGender = input("Is the Villager you're looking for a" "\033[34m" " boy "
      "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl"
      "\033[30m""\033[37m""? ""\033[0m").lower()
  if bearGender == "boy":
      print()
      print("\033[31m" "Is the Villager you're looking for named Chow?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
      if bearGender == "girl":
        print()
        print("\033[31m" "Is the Villager you're looking for named Chow?""\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("ADD CHARACTER INFO PAGE")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
  # BEAR - WHITE
  if bearColor == "white":
      print()
      bearBangs = input("Is the color of this bears bangs pink or blonde? ").lower()
      if bearBangs == "pink":
        print()
        print("\033[31m" "Is the Villager you're looking for named Pinky?""\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("ADD CHARACTER INFO PAGE")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
      if bearBangs == "blonde":
        print()
        print("\033[33m" "Is the Villager you're looking for named Tutu?""\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("ADD CHARACTER INFO PAGE")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
  # BEAR - BROWN
  if bearColor == "brown":
      print()
  bearGender = input("Is the Villager you're looking for a" "\033[34m" " boy "
      "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl"
      "\033[30m""\033[37m""? ""\033[0m").lower()
  if bearGender == "girl":
        print()
        print("\033[33m" "Is the Villager you're looking for named Paula?""\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("ADD CHARACTER INFO PAGE")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
  if bearGender == "boy":
        print()
        bearEyebrows = input("Does this Villager have thick eyebrows? ").lower()
        if bearEyebrows == "no":
          print()
          print("\033[33m" "Is the Villager you're looking for named Ike?""\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("ADD CHARACTER INFO PAGE")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
        if bearEyebrows == "yes":
          print()
          bearShade = input("Is this Villager lighter or darker?").lower()
          if bearShade == "lighter":
            print()
            print("\033[33m" "Is the Villager you're looking for named Teddy?""\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("ADD CHARACTER INFO PAGE")
            if yn == "no":
              print()
              print("Sounds like a you problem.")
          if bearShade == "darker":
            print()
            print("\033[33m" "Is the Villager you're looking for named Grizzly?"
                  "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("ADD CHARACTER INFO PAGE")
            if yn == "no":
              print()
              print("Sounds like a you problem.")
  # BEAR - BLUE
  if bearColor == "blue":
    print()
    bearHairColor = input("Is the facial hair of this Villager brown or blonde? Or"
                          " neither? ").lower()
    if bearHairColor == "brown":
      print()
      print("\033[34m" "Is the Villager you're looking for named Beardo ?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if bearHairColor == "blonde":
      print()
      print("\033[34m" "Is the Villager you're looking for named Groucho?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if bearHairColor == "neither":
      print()
      print("\033[34m" "Is the Villager you're looking for named Curt?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# WOLF
if species == "wolf":
  wolfColor = input("What is the color of this Villager? ").lower()
#ORANGE WOLF
  if wolfColor == "orange":
    print()
    print("\033[33m" "Is the Villager you're looking for named Cheif?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# PINK WOLF
  if wolfColor == "pink":
    print()
    wolfBangs = input("Does this Villager have bangs? ").lower()
    if wolfBangs == "yes":
      print()
      print("\033[31m" "Is the Villager you're looking for named Audie?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if wolfBangs == "no":
      print()
      print("\033[31m" "Is the Villager you're looking for named Freya?"
            "\033[0m")
      print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# PURPLE WOLF
  if wolfColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Lobo?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# GRAY WOLF
  if wolfColor == "grey":
    print()
    wolfAge = input("Does this Villager look old or young? ").lower()
    if wolfAge == "young":
     print()
     print("\033[34m" "Is the Villager you're looking for named Fang?"
            "\033[0m")
     print()
     yn = input("Yes or No? ").lower()
     if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
     if yn == "no":
        print()
        print("Sounds like a you problem.")
    if wolfAge == "old":
     print()
     print("\033[34m" "Is the Villager you're looking for named Dobie?"
            "\033[0m")
     print()
     yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# BROWN WOLF
  if wolfColor == "brown":
    print()
    wolfGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if wolfGender == "boy":
      print()
      print("\033[30m" "Is the Villager you're looking for named Kyle?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if wolfGender == "girl":
      print()
      print("\033[30m" "Is the Villager you're looking for named Vivian?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# BLUE WOLF
  if wolfColor == "blue":
    print()
    wolfGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if wolfGender == "boy":
      print()
      print("\033[34m" "Is the Villager you're looking for named Wolfgang?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if wolfGender == "girl":
      print()
      cuteOrSleek = input("Is this Vllager cute or more sleek? ").lower()
      if cuteOrSleek == "cute":
        print()
        print("\033[34m" "Is the Villager you're looking for named Skyle?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
      if cuteOrSleek == "sleek":
        print()
        print("\033[34m" "Is the Villager you're looking for named W?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("ADD CHARACTER INFO PAGE")
      if yn == "no":
        print()
        print("Sounds like a you problem.")