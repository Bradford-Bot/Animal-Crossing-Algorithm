print()
print("\033[32m" "Animal Crossing Algorithm" "\033[0m")
print("")
print("\033[32m" "Looking for a villager and can't put your finger on what their name"
" is? Answer the questions below and find out!" "\033[0m")
print()

species = input("What species is your villager? ").lower()
print()

#SPECIAL
if species == "special":
  print("Cameron: Katt!")
  print("Mom: Isabell!")
  print("Samantha: Tangy!")

# ALLIGATOR
if species == "alligator":
  gatorColor = input("What is the main color of this Villager? ").lower()
  print()
#ALLIGATOR - YELLOW
  if gatorColor == "yellow":
    gatorPattern = input("Is the pattern on this Villager camo or circles? ").lower()
    if gatorPattern == "camo":
      print()
      print("\033[33m" "Is the Villager you're looking for named Sly?" "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Sly")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if gatorPattern == "circles":
      print()
      print("\033[33m" "Is the Villager you're looking for named Alfonso?" "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Alfonso")
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
      print("https://animalcrossing.fandom.com/wiki/Alli")
    if yn == "no":
      print()
      print("Sounds like a you problem.")
#ALLIGATOR - GREEN
  if gatorColor == "green":
    gatorTraits = input("Does this Villager look happy or angry? ").lower()
    if gatorTraits == "happy":
      print()
      print("\033[32m""Is the Villager you're looking for named Boots?""\033[0m")
      print()
      yn = input("Yes or No? ")
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Boots")
      if yn == "no":
        print()
        print("Sucks for you.")
    if gatorTraits == "angry":
      print()
      print("\033[32m""Is the Villager you're looking for named Drago?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Drago")
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
      print("https://animalcrossing.fandom.com/wiki/Del")
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
      print("https://animalcrossing.fandom.com/wiki/Gayle")
    if yn == "no":
      print()
      print("Sounds like a you problem.")
 # ALLIGATOR - BROWN
  if gatorColor == "brown":
    print("\033[33m" "Is the Villager you're looking for named Roswell?" "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Roswell")
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
        print("https://animalcrossing.fandom.com/wiki/Anabelle")
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
        print("https://animalcrossing.fandom.com/wiki/Pango")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# ANTEATER - WHITE
  if anteaterColor == "white":
      print()
      antColorTwo = input("Is the secondary color of your Villager" 
      " cyan or black? ").lower()
      if antColorTwo == "cyan":
        print()
        print("\033[36m" "Is the Villager you're looking for named Zoe?" "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Zoe")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
      if antColorTwo == "black":
        print()
        anteaterBOG = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                            "\033[30m""\033[37m""? ""\033[0m").lower()
        if anteaterBOG == "boy":
          print()
          print("\033[30m" "Is the Villager you're looking for named Antonio?" 
                "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Antonio")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
        if anteaterBOG == "girl":
          print()
          print("\033[30m" "Is the Villager you're looking for named Annalisa?" 
                "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Annalisa")
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
        print("https://animalcrossing.fandom.com/wiki/Olaf")
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
        print("https://animalcrossing.fandom.com/wiki/Cyrano")
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
      print("https://animalcrossing.fandom.com/wiki/Snooty_(villager)")
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
        print("https://animalcrossing.fandom.com/wiki/Angus")
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
        print("https://animalcrossing.fandom.com/wiki/Coach")
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
        print("https://animalcrossing.fandom.com/wiki/Vic")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# BULL - GRAY
    if bullColor == "gray":
      print()
      print("\033[33m" "Is the Villager you're looking for named Rodeo?"
            "\033[0m")
      print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Rodeo")
    if yn == "no":
      print()
      print("Sounds like a you problem.")
# Bull - BLUE
    if bullColor == "blue":
      print()
      bullPattern = input("Does this Villager have a pattern on their horns? ").lower()
      if bullPattern == "yes":
        print("\033[33m" "Is the Villager you're looking for named T-Bone?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/T-Bone")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
      if bullPattern == "no":
        print("\033[33m" "Is the Villager you're looking for named Stu?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Stu")
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
        print("https://animalcrossing.fandom.com/wiki/Charlise")
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
        print("https://animalcrossing.fandom.com/wiki/Nate")
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
        print("https://animalcrossing.fandom.com/wiki/Megan")
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
          print("https://animalcrossing.fandom.com/wiki/Chow")
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
          print("https://animalcrossing.fandom.com/wiki/Pinky")
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
          print("https://animalcrossing.fandom.com/wiki/Tutu")
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
          print("https://animalcrossing.fandom.com/wiki/Paula")
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
            print("https://animalcrossing.fandom.com/wiki/Ike")
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
              print("https://animalcrossing.fandom.com/wiki/Teddy")
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
              print("https://animalcrossing.fandom.com/wiki/Grizzly")
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
        print("https://animalcrossing.fandom.com/wiki/Beardo")
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
        print("https://animalcrossing.fandom.com/wiki/Groucho")
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
        print("https://animalcrossing.fandom.com/wiki/Curt")
      if yn == "no":
        print()
        print("Sounds like a you problem.")

# COW
if species == "cow":
  cowColor = input("What is the color of this Villager? ").lower()
# COW - WHITE
  if cowColor == "white":
    print("\033[33m" "Is the Villager you're looking for named Tipper?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tipper")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# COW - BLUE
  if cowColor == "blue":
    print("\033[33m" "Is the Villager you're looking for named Naomi?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Naomi")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# COW - PINK
  if cowColor == "pink":
    print("\033[33m" "Is the Villager you're looking for named Norma?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Norma")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# COW - BROWN
  if cowColor == "brown":
    print("\033[33m" "Is the Villager you're looking for named Patty?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Patty")
    if yn == "no":
        print()
        print("Sounds like a you problem.")

#Elephant
# Elephant - GREEN
if species == "elephant":
   elephantColor = input("What is the color if this Villager? ").lower()
   if elephantColor == "green":
    print("\033[33m" "Is the Villager you're looking for named Opal?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Opal")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# Elephant - YELLOW
    if elephantColor == "yellow":
      print("\033[33m" "Is the Villager you're looking for named Eloise?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Eloise")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# Elephant - RED
    if elephantColor == "red":
      print("\033[33m" "Is the Villager you're looking for named Cyd?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cyd")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# Elephant - PINK
    if elephantColor == "pink":
      print("\033[33m" "Is the Villager you're looking for named Paolo?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Paolo")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
 # Elephant - GRAY       
    if elephantColor == "gray":
      print("\033[33m" "Is the Villager you're looking for named Big Top?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Big_Top")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# ELEPHANT - BROWN
    if elephantColor == "brown":
      elephantGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
      if elephantGender == "boy":
        print()
        print("\033[34m" "Is the Villager you're looking for named Tucker?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Tucker")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
      if elephantGender == "girl":
        print()
        print("\033[34m" "Is the Villager you're looking for named Ellie ?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Ellie")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
# ELEPHANT - BLUE
   if elephantColor == "blue":
    print()
    elephantGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if elephantGender == "girl":
        print()
        print("\033[34m" "Is the Villager you're looking for named Chai?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Chai")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
    if elephantGender == "boy":
      print()
      elephantDOL = input("Is this Villager a lighter or darker blue? ").lower()
      if elephantDOL == "darker" "dark":
        print("\033[33m" "Is the Villager you're looking for named Axel?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Axel")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
      if elephantDOL == "light" "ligher":
        print("\033[33m" "Is the Villager you're looking for named Dizzy?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Dizzy")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
# ELEPHANT - WHITE
    if elephantColor == "white":
      print()
    elephantStripe = input("Does this Villager have red and yellow stripes on them? ").lower()
    if elephantStripe == "no":
      print("\033[33m" "Is the Villager you're looking for named Tia?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tia")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if elephantStripe == "yes":
      print("\033[33m" "Is the Villager you're looking for named Margie?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Margie")
      if yn == "no":
        print()
        print("Sounds like a you problem.")

# GOAT
if species == "goat":
  goatColor = input("What is the color of this Villager? ").lower()
# GOAT - PINK
  if goatColor == "pink":
    print("\033[33m" "Is the Villager you're looking for named Velma?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Velma")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# GOAT - BLUE
  if goatColor == "blue":
    print("\033[33m" "Is the Villager you're looking for named Sherb?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Sherb")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# GOAT - WHITE
  if goatColor == "white":
    print("\033[33m" "Is the Villager you're looking for named Chevre?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Chevre")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# GOAT - GREEN
  if goatColor == "green":
    print("\033[33m" "Is the Villager you're looking for named Gruff?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Gruff")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# GOAT - PURPLE
  if goatColor == "purple":
    print("\033[33m" "Is the Villager you're looking for named Kidd?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Kidd")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# GOAT - BLACK
  if goatColor == "black":
    print("\033[33m" "Is the Villager you're looking for named Nan?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Nan")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# GOAT - BROWN]
    if goatColor == "brown":
      goatColor = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" 
                      "\033[31m"" girl""\033[30m""\033[37m""? ""\033[0m").lower()
      if goatColor == "boy":
          print("\033[34m" "Is the Villager you're looking for named Billy?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Billy")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
      if goatColor == "girl":
          print("\033[34m" "Is the Villager you're looking for named Pashmina?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Pashmina")
          if yn == "no":
            print()
            print("Sounds like a you problem.")

# HIPPO
if species == "hippo":
  hippoColor = input("What is the color of this Villager? ").lower()
# HIPPO - BLUE
  if hippoColor == "blue":
    print("\033[33m" "Is the Villager you're looking for named Bertha?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Bertha")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# HIPPO - PINK
  if hippoColor == "pink":
    print("\033[33m" "Is the Villager you're looking for named Bitty?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Bitty")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# HIPPO - YELLOW
  if hippoColor == "yellow":
    print("\033[33m" "Is the Villager you're looking for named Harry?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Harry")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# HIPPO - BROWN
  if hippoColor == "brown":
    hippoGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" 
                      "\033[31m"" girl""\033[30m""\033[37m""? ""\033[0m").lower()
    if hippoGender == "boy":
          print("\033[34m" "Is the Villager you're looking for named Biff?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Biff")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
    if hippoGender == "girl":
          print("\033[34m" "Is the Villager you're looking for named Bubbles?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Bubbles")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
# HIPPO - GREEN
  if hippoColor == "green":
     hippoHair = input("Does this Villager have hair? ").lower()
     if hippoHair == "yes":
        print("\033[34m" "Is the Villager you're looking for named Hippeux?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Hippeux")
        if yn == "no":
            print()
            print("Sounds like a you problem.")
     if hippoHair == "no":
        print("\033[34m" "Is the Villager you're looking for named Rocco?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Rocco")
        if yn == "no":
            print()
            print("Sounds like a you problem.")

# HORSE
if species == "horse":
  horseColor = input("What is the color of this Villager? ").lower()
# HORSE - PINK
  if horseColor == "pink":
    print("\033[33m" "Is the Villager you're looking for named Peaches?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Peaches")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# HORSE - BLACK
  if horseColor == "black":
    print("\033[33m" "Is the Villager you're looking for named Roscoe?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Roscoe")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# HORSE - PURPLE
  if horseColor == "purple":
    print("\033[33m" "Is the Villager you're looking for named Cleo?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cleo")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# HORSE - GREEN
  if horseColor == "green":
    horseGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if horseGender == "boy":
          print("\033[34m" "Is the Villager you're looking for named Buck?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Buck")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
    if horseGender == "girl":
          print("\033[34m" "Is the Villager you're looking for named Winnie?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Winnie")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
# HORSE - YELLOW
  if horseColor == "yellow":
    print("\033[33m" "Is the Villager you're looking for named Clyde?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Clyde")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# HORSE - WHITE
  if horseColor == "white":
    horseGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if horseGender == "boy":
        horseBangs = input("Does this Villager have blonde hair? ").lower()
        if horseBangs == "yes":
          print()
          print("\033[34m" "Is the Villager you're looking for named Colton?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Colton")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
        if horseBangs == "no":
          print()
          print("\033[34m" "Is the Villager you're looking for named Papi?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Papi")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
    if horseGender == "girl":
        print()
        print("\033[34m" "Is the Villager you're looking for named Savannah?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Savannah")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
# HORSE - BROWN
  if horseColor == "brown":
    horseGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if horseGender == "boy":
          print("\033[34m" "Is the Villager you're looking for named Elmer?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Elmer")
          if yn == "no":
            print()
            print("Sounds like a you problem.")
    if horseGender == "girl":
      girlHorseColor = input("Is this Villager a lighter or darker brown? ").lower()
      if girlHorseColor == "lighter" "light":
        print("\033[34m" "Is the Villager you're looking for named Victoria?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Victoria")
        if yn == "no":
            print()
            print("Sounds like a you problem.")
      if girlHorseColor == "darker" "dark":
        print("\033[34m" "Is the Villager you're looking for named Reneigh?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Reneigh")
        if yn == "no":
            print()
            print("Sounds like a you problem.")
# HORSE - BLUE 
  if horseColor == "blue":
     horseHair = input("Does the Villager you're looking for have blonde hair? ").lower()
     if horseHair == "yes":
        print("\033[34m" "Is the Villager you're looking for named Ed?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Ed")
        if yn == "no":
            print()
            print("Sounds like a you problem.")
     if horseHair == "no":
        print("\033[34m" "Is the Villager you're looking for named Julian?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Julian")
        if yn == "no":
            print()
            print("Sounds like a you problem.")

# Kangaroo
if species == "kangaroo":
  kangarooColor = input("What is the color of this Villager? ").lower()
# KANGAROO - WHITE
  if kangarooColor == "white":
    print("\033[33m" "Is the Villager you're looking for named Astrid?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Astrid")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# KANGAROO - PINK
  if kangarooColor == "pink":
    print("\033[33m" "Is the Villager you're looking for named Marcie?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Marcie")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# KANGAROO - BLACK
  if kangarooColor == "black":
    print("\033[33m" "Is the Villager you're looking for named Mathilda?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Mathilda")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# KANGAROO - BLUE
  if kangarooColor == "blue":
    print("\033[33m" "Is the Villager you're looking for named Rooney?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rooney")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# KANGAROO - PURPLE
  if kangarooColor == "purple":
    print("\033[33m" "Is the Villager you're looking for named Sylvia?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Sylvia")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# KANGAROO - GRAY
  if kangarooColor == "gray":
    print("\033[33m" "Is the Villager you're looking for named Walt?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Walt")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# KANGAROO - BROWN
  if kangarooColor == "brown":
    print("\033[33m" "Is the Villager you're looking for named Kitt?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Kitt")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# KANGAROO - ORANGE
  if kangarooColor == "orange":
    print("\033[33m" "Is the Villager you're looking for named Carrie?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Carrie")
    if yn == "no":
        print()
        print("Sounds like a you problem.")

# OCTOPUS
if species == "octopus":
  octopusColor =input("What is the color of this Villager? ")
# OCTOPUS - GRAY
  if octopusColor == "gray":
    print("\033[33m" "Is the Villager you're looking for named Cephalobot?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cephalobot")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# OCTOPUS - PINK
  if octopusColor == "pink":
    print("\033[33m" "Is the Villager you're looking for named Marina?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Marina")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# OCTOPUS - RED
  if octopusColor == "red":
    print("\033[33m" "Is the Villager you're looking for named Octavian?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Octavian")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# OCTOPUS - BROWN
  if octopusColor == "brown":
    print("\033[33m" "Is the Villager you're looking for named Zucker?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Zucker")
    if yn == "no":
        print()
        print("Sounds like a you problem.")

# Ostrich
  if species == "ostrich":
    ostrichColor = input("What is the color of this Villager? ").lower()
# Ostrich - RED
    if ostrichColor == "red":
      print("\033[33m" "Is the Villager you're looking for named Rio?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rio")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# Ostrich - BLACK
    if ostrichColor == "black":
      print("\033[33m" "Is the Villager you're looking for named Gladys?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Gladys")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# Ostrich - PINK
    if ostrichColor == "pink":
      print("\033[33m" "Is the Villager you're looking for named Flora?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Flora")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# Ostrich - PURPLE
    if ostrichColor == "purple":
      ostrichGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
      if ostrichGender == "boy":
        print()
        print("\033[34m" "Is the Villager you're looking for named Phil?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Phil")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
      if ostrichGender == "girl":
        print()
        print("\033[34m" "Is the Villager you're looking for named Queenie?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Queenie")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
# Ostrich - WHITE
  if ostrichColor == "white":
    ostrichGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if ostrichGender == "boy":
        print()
        print("\033[34m" "Is the Villager you're looking for named Cranston?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Cranston")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
    if ostrichGender == "girl":
        print()
        print("\033[34m" "Is the Villager you're looking for named Blanche?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Blanche")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
# Ostrich - GREEN
  if ostrichColor == "green":
    ostrichGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if ostrichGender == "boy":
        print()
        print("\033[34m" "Is the Villager you're looking for named Sprocket?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Sprocket")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
    if ostrichGender == "girl":
        print()
        print("\033[34m" "Is the Villager you're looking for named Julia?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Julia")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
# Ostrich - ORANGE
  if ostrichColor == "orange":
    ostrichVibe = input("Does this Villager look sleepy or fierce? ").lower()
    if ostrichVibe == "sleepy":
        print()
        print("\033[34m" "Is the Villager you're looking for named Sandy?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Sandy")
        if yn == "no":
          print()
          print("Sounds like a you problem.")
    if ostrichVibe == "fierce":
        print()
        print("\033[34m" "Is the Villager you're looking for named Phoebe?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Phoebe")
        if yn == "no":
          print()
          print("Sounds like a you problem.")

# RHINO 
if species == "rhino":
  rhinoColor = input("What is the color of this Villager? ").lower()
  #ORANGE
# RHINO - ORANGE
  if rhinoColor == "orange":
    print("\033[33m" "Is the Villager you're looking for named Spike?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Spike")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# RHINO - WHITE
  if rhinoColor == "white":
    print()
    print("\033[37m" "Is the Villager you're looking for named Rhonda?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rhonda")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# RHINO - GRAY
  if rhinoColor == "gray":
    print()
    print("\033[34m" "Is the Villager you're looking for named Tank?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tank")
    if yn == "no":
        print()
        print("Sounds like a you problem.")  
 # RHINO - BLUE
  if rhinoColor == "blue":
    print()
    rhinoGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if rhinoGender == "boy":
      print()
      print("\033[34m" "Is the Villager you're looking for named Hornsby?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Hornsby")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if rhinoGender == "girl":
      print()
      print("\033[34m" "Is the Villager you're looking for named Azalea?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Azalea")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# RHINO - PINK
  if rhinoColor == "pink":
    print()
    berryRhino = input("Does this Villager have a strawberry on their nose? ").lower()
    if berryRhino == "yes":
      print()
      print("\033[31m" "Is the Villager you're looking for named Merengue?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Merengue")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if berryRhino == "no":
      print()
      print("\033[31m" "Is the Villager you're looking for named Renée?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Renée")
      if yn == "no":
        print()
        print("Sounds like a you problem.")

# TIGER
if species == "tiger":
  tigerColor = input("What is the color of this Villager? ").lower()
# TIGER - ORANGE
  if tigerColor == "orange":
    print()
    tigerUniBrow = input("Does this Villager have a unibrow? ").lower()
    if tigerUniBrow == "yes":
      print()
      print("\033[33m" "Is the Villager you're looking for named Rowan?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rowan")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if tigerUniBrow == "no":
      print()
      print("\033[33m" "Is the Villager you're looking for named Leonardo?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Leonardo")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# TIGER - YELLOW
  if tigerColor == "yellow":
    print()
    print("\033[33m" "Is the Villager you're looking for named Tybalt?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tybalt")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# TIGER - PINK
  if tigerColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Claudia?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Claudia")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# TIGER - BROWN
  if tigerColor == "brown":
    print()
    print("\033[33m" "Is the Villager you're looking for named Bangle?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Bangle")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# TIGER - WHITE
    print()
    tigerGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if tigerGender == "boy":
      print()
      print("\033[37m" "Is the Villager you're looking for named Rolf?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rolf")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
      if tigerGender == "girl":
        print()
        print("\033[37m" "Is the Villager you're looking for named Bianca?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
         print()
         print("https://animalcrossing.fandom.com/wiki/Bianca_(tiger)")
        if yn == "no":
         print()
         print("Sounds like a you problem.")

# WOLF
if species == "wolf":
  wolfColor = input("What is the color of this Villager? ").lower()
# WOLF - ORANGE
  if wolfColor == "orange":
    print()
    print("\033[33m" "Is the Villager you're looking for named Cheif?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Chief")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# WOLF - PINK
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
        print("https://animalcrossing.fandom.com/wiki/Audie")
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
        print("https://animalcrossing.fandom.com/wiki/Freya")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# WOLF - PURPLE
  if wolfColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Lobo?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Lobo")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# WOLF - GRAY
  if wolfColor == "gray":
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
        print("https://animalcrossing.fandom.com/wiki/Fang")
     if yn == "no":
        print()
        print("Sounds like a you problem.")
    if wolfAge == "old":
     print()
     print("\033[30m" "Is the Villager you're looking for named Dobie?"
            "\033[0m")
     print()
     yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Dobie")
    if yn == "no":
        print()
        print("Sounds like a you problem.")
# WOLF - BROWN
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
        print("https://animalcrossing.fandom.com/wiki/Kyle")
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
        print("https://animalcrossing.fandom.com/wiki/Vivian")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
# WOLF - BLUE
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
        print("https://animalcrossing.fandom.com/wiki/Wolfgang")
      if yn == "no":
        print()
        print("Sounds like a you problem.")
    if wolfGender == "girl":
      print()
      cuteOrSleek = input("Is this Vllager cute or more sleek? ").lower()
      if cuteOrSleek == "cute":
        print()
        print("\033[34m" "Is the Villager you're looking for named Skye?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Skye")
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
        print("https://animalcrossing.fandom.com/wiki/Whitney")
      if yn == "no":
        print()
        print("Sounds like a you problem.")