print()
print("\033[31m" "PLEASE BE ADVISED" "\033[0m")
print()
print("\033[31m" "COLORS ARE BASED OFF ON MAJORITY PRESENTED" "\033[0m")
print()
print("\033[31m" "TAN IS EQUAL TO BROWN" "\033[0m")
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
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
      print("Refresh the page and rethink your answers.")
#ALLIGATOR - GREEN
  if gatorColor == "green":
    gatorTraits = input("Does this Villager look happy or angry? ").lower()
    if gatorTraits == "happy":
      print()
      print("\033[32m""Is the Villager you're looking for named Boots?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
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
      print("Refresh the page and rethink your answers.")
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
      print("Refresh the page and rethink your answers.")
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
      print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
 # ANTEATER - BROWN
  if anteaterColor == "brown":
      print()
      print("\033[33m" "Is the Villager you're looking for named Antonio?" "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Antonio")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# ANTEATER - WHITE
  if anteaterColor == "white":
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
            print("Refresh the page and rethink your answers.")
# ANTEATER - ORANGE
  if anteaterColor == "orange":
      print()
      print("\033[33m" "Is the Villager you're looking for named Olaf?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Olaf")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# ANTEATER - BLUE
  if anteaterColor == "blue":
    anteaterGender = input("Is the Villager you're looking for a" "\033[34m" " boy "
      "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl"
      "\033[30m""\033[37m""? ""\033[0m").lower()
    if anteaterGender == "boy":
      print()
      print("\033[34m" "Is the Villager you're looking for named Cyrano?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cyrano")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if anteaterGender == "girl":
      print()
      print("\033[34m" "Is the Villager you're looking for named Zoe?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Zoe")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# ANTEATER - PINK
  if anteaterColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Snooty?""\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Snooty_(villager)")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")

# BIRD
if species == "bird":
   birdColor = input("What is the main color of this Villager? ").lower()
# BIRD - YELLOW
   if birdColor == "yellow":
      print()
      print("\033[33m" "Is the Villager you're looking for named Twiggy?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Twiggy")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# BIRD - PINK
   if birdColor == "pink":
      print()
      print("\033[31m" "Is the Villager you're looking for named Midge?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Midge")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# BIRD - RED
   if birdColor == "red":
      print()
      print("\033[31m" "Is the Villager you're looking for named Lucha?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Lucha")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# BIRD - PURPLE
   if birdColor == "purple":
      print()
      print("\033[35m" "Is the Villager you're looking for named Jacques?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Jacques")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# BIRD - green
   if birdColor == "green":
      print()
      aot = input("Does this Villager look annoyed or tired? ").lower()
      if aot == "annoyed":
        print()
        print("\033[32m" "Is the Villager you're looking for named Admiral?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Admiral")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if aot == "tired":
        print()
        print("\033[32m" "Is the Villager you're looking for named Jitters?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Jitters")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# BIRD - WHITE
   if birdColor == "white":
     print()
     birdGender = input("Is the Villager you're looking for a" "\033[34m" " boy "
      "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl"
      "\033[30m""\033[37m""? ""\033[0m").lower()
     if birdGender == "boy":
        print()
        print("\033[37m" "Is the Villager you're looking for named Jacob?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Jacob")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
     if birdGender == "girl":
        print()
        print("\033[37m" "Is the Villager you're looking for named Piper?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Piper")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# BIRD - BLUE
   if birdColor == "blue":
     print()
     birdGender = input("Is the Villager you're looking for a" "\033[34m" " boy "
      "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl"
      "\033[30m""\033[37m""? ""\033[0m").lower()
     if birdGender == "girl":
        print()
        print("\033[34m" "Is the Villager you're looking for named Robin?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Robin")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
     if birdGender == "boy":
        print()
        be = input("Does this Villager have an expressive face? ").lower()
        if be == "no":
          print()
          print("\033[34m" "Is the Villager you're looking for named Ace?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Ace")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if be == "yes":
          print()
          print("\033[34m" "Is the Villager you're looking for named Jay?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Jay")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
# BIRD - BROWN
   if birdColor == "brown":
      print()
      bbe = input("Does this Villager have thick eyebrows? ").lower()
      print()
      if bbe == "yes":
          print()
          print("\033[33m" "Is the Villager you're looking for named Anchovy?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Anchovy")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
      if bbe == "no":
         bse = input("Does this Villager have sunken in eyes? ").lower()
         if bse == "yes":
          print()
          print("\033[33m" "Is the Villager you're looking for named Sparro?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Sparro")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
         if bse == "no":
          print()
          print("\033[33m" "Is the Villager you're looking for named Peck?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Peck")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")

#BULL
if species == "bull":
# BULL - ORANGE
    bullColor = input("What is the main color of this Villager? ").lower()
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
# BULL - GRAY
    if bullColor == "gray":
      print()
      print("\033[30m" "Is the Villager you're looking for named Rodeo?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rodeo")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# Bull - BLUE
    if bullColor == "blue":
      print()
      bullPattern = input("Does this Villager have a pattern on their horns? ").lower()
      if bullPattern == "yes":
        print()
        print("\033[34m" "Is the Villager you're looking for named Stu?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Stu")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if bullPattern == "no":
        print()
        print("\033[34m" "Is the Villager you're looking for named T-Bone?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/T-Bone")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")

# BEAR
if species == "bear":
  bearColor = input("What is the color of this Villager? ").lower()
  print()
# BEAR - GREEN
  if bearColor == "green":
      print("\033[32m" "Is the Villager you're looking for named Charlise?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Charlise")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# BEAR - orange
  if bearColor == "orange":
      print("\033[33m" "Is the Villager you're looking for named Nate?""\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Nate")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# BEAR - PURPLE
  if bearColor == "purple":
    print("\033[35m" "Is the Villager you're looking for named Megan?""\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Megan")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# BEAR - PINK
  if bearColor == "pink":
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
        print("https://animalcrossing.fandom.com/wiki/Chow")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if bearGender == "girl":
        print()
        print("\033[31m" "Is the Villager you're looking for named Ursala?""\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Ursala")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# BEAR - WHITE
  if bearColor == "white":
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
          print("Refresh the page and rethink your answers.")
      if bearBangs == "blonde":
        print()
        print("\033[37m" "Is the Villager you're looking for named Tutu?""\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Tutu")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# BEAR - BROWN
  if bearColor == "brown":
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
          print("Refresh the page and rethink your answers.")
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
            print("Refresh the page and rethink your answers.")
        if bearEyebrows == "yes":
          print()
          bearShade = input("Is this Villager lighter or darker? ").lower()
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
              print("Refresh the page and rethink your answers.")
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
              print("Refresh the page and rethink your answers.")
# BEAR - BLUE
  if bearColor == "blue":
     bfh = input("Does this Villager have facial hair? ").lower()
     print()
     if bfh == "yes":
      print("\033[34m" "Is the Villager you're looking for named Beardo?"
                  "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Beardo")
      if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
     if bfh == "no":
        ba = input("Does this Villager look angry? ").lower()
        print()
        if ba == "no":
          lbb = input("Is this Villager light blue? ").lower()
          if lbb == "no":
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
              print("Refresh the page and rethink your answers.")
          if lbb == "yes":
            print()
            print("\033[34m" "Is the Villager you're looking for named Klaus?"
                  "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Klaus")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
        if ba == "yes":
          print("\033[34m" "Is the Villager you're looking for named Curt?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Curt")
          if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
# CAT
if species == "cat":
   catColor = input("What is the main color of this Villager? ").lower()
# CAT - ORANGE
   if catColor == "orange":
     print()
     cl = input("Does this VIllager have a leaf on its head? ").lower()
     if cl == "no":
      print()
      print("\033[33m" "Is the Villager you're looking for named Tabby?"
                  "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tabby")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
     if cl == "yes":
      print()
      print("\033[33m" "Is the Villager you're looking for named Tangy?"
                  "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tangy")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CAT - GREEN
   if catColor == "green":
    print()
    print("\033[32m" "Is the Villager you're looking for named Stinky?"
                  "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Stinky")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# CAT - YELLOW
   if catColor == "yellow":
    print()
    print("\033[33m" "Is the Villager you're looking for named Ankha?"
                  "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Ankha")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# CAT - PURPLE
   if catColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Bob?"
                  "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Bob")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# CAT - BLACK
   if catColor == "black":
    print()
    print("\033[30m" "Is the Villager you're looking for named Kiki?"
                  "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Kiki")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# CAT - GRAY
   if catColor == "gray":
    print()
    cubGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if cubGender == "girl":
      print()
      print("\033[30m" "Is the Villager you're looking for named Lolly?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Lolly")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if cubGender == "boy":
      print()
      print("\033[30m" "Is the Villager you're looking for named Raymond?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Raymond")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CAT - BLUE
   if catColor == "blue":
    print()
    catGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if catGender == "girl":
      print()
      print("\033[34m" "Is the Villager you're looking for named Rosie?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rosie")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if catGender == "boy":
      print()
      ccp = input("Does this Villager have circular pupils? ").lower()
      if ccp == "yes":
        print()
        print("\033[34m" "Is the Villager you're looking for named Tom?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Tom")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if ccp == "no":
        print()
        print("\033[34m" "Is the Villager you're looking for named Moe?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Moe")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# CAT - BROWN
   if catColor == "brown":
    print()
    catGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
        "\033[30m""\033[37m""? ""\033[0m").lower()
    if catGender == "boy":
      print()
      print("\033[33m" "Is the Villager you're looking for named Rudy?"
                  "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rudy")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if catGender == "girl":
      print()
      ct = input("Is this Villager tan? ").lower()
      if ct == "yes":
        print()
        cb = input("Does this Villager only has just bangs? ").lower()
        if cb == "yes":
          print()
          print("\033[33m" "Is the Villager you're looking for named Merry?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Merry")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if cb == "no":
          print()
          print("\033[33m" "Is the Villager you're looking for named Felicity?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Felicity")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
      if ct == "no":
        print()
        cmu = input("Does this Villager have on pink eyeshadow? ").lower()
        if cmu == "yes":
          print()
          print("\033[33m" "Is the Villager you're looking for named Kitty?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Kitty")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if cmu == "no":
          print()
          print("\033[33m" "Is the Villager you're looking for named Katt?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Katt")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
# CAT - WHITE
   if catColor == "white":
    print()
    catGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if catGender == "boy":
      print()
      cr = input("Does this Villager have red lines on its face? ").lower()
      if cr == "yes":
        print()
        print("\033[31m" "Is the Villager you're looking for named Kabuki?"
                  "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Kabuki")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if cr == "no":
        print()
        cbl = input("Does this Villager have a black forehead? ").lower()
        if cbl == "yes":
          print()
          print("\033[37m" "Is the Villager you're looking for named Punchy?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Punchy")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if cbl == "no":
          print()
          print("\033[37m" "Is the Villager you're looking for named Kid Cat?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Kid_Cat")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
    if catGender == "girl":
      print()
      cmk = input("Is this Villager wearing makeup? ").lower()
      print()
      if cmk == "yes":
        cbh = input("Does this Villager have blonde hair? ").lower()
        if cbh == "yes":
          print()
          print("\033[33m" "Is the Villager you're looking for named Monique?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Monique")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if cbh == "no":
          print()
          print("\033[37m" "Is the Villager you're looking for named Olivia?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Olivia")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
      if cmk == "no":
        bfc = input("Is there a blue circle on this Villagers face? ").lower()
        print()
        if bfc == "yes":
          print("\033[34m" "Is the Villager you're looking for named Mitzi?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Mitzi")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if bfc == "no":
          print("\033[37m" "Is the Villager you're looking for named Purrl?"
                  "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Purrl")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
# CUB
if species == "cub":
  cubColor = input("What is the main color of this Villager? ").lower()
# CUB - PINK
  if cubColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Vladimir?"
                  "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Vladimir")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# CUB - PURPLE
  if cubColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Judy?"
                  "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Judy")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# CUB - red
  if cubColor == "red":
    print()
    print("\033[31m" "Is the Villager you're looking for named Cheri?"
                  "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Cheri")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# CUB - green
  if cubColor == "green":
    print()
    print("\033[32m" "Is the Villager you're looking for named Murphy?"
                  "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
      print()
      print("https://animalcrossing.fandom.com/wiki/Murphy")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# CUB - GRAY
  if cubColor == "gray":
    print()
    cubGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if cubGender == "girl":
      print()
      print("\033[30m" "Is the Villager you're looking for named Olive?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Olive")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if cubGender == "boy":
      print()
      print("\033[30m" "Is the Villager you're looking for named Barold?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Barold")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CUB - YELLOW
  if cubColor == "yellow":
    print()
    cubGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if cubGender == "girl":
      print()
      print("\033[33m" "Is the Villager you're looking for named Tammy?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tammy")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if cubGender == "boy":
      print()
      print("\033[33m" "Is the Villager you're looking for named Marty?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Marty")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CUB - orange
  if cubColor == "orange":
    print()
    obp = input("Does this Villager look like a stuffed animal? ").lower()
    if obp == "yes":
      print()
      print("\033[33m" "Is the Villager you're looking for named Stitches?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Stitches")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if obp == "no":
      print()
      print("\033[33m" "Is the Villager you're looking for named Pudge?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Pudge")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CUB - BLUE
  if cubColor == "blue":
    print()
    cubGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if cubGender == "girl":
      print()
      print("\033[34m" "Is the Villager you're looking for named Bluebear?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Bluebear")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if cubGender == "boy":
      print()
      bds = input("Does this Villager have a dark spot of blue on its face? ").lower()
      if bds == "yes":
        print()
        print("\033[34m" "Is the Villager you're looking for named Kody?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Kody")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if bds == "no":
        print()
        print("\033[34m" "Is the Villager you're looking for named Poncho?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Poncho")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# CUB - BROWN
  if cubColor == "brown":
    print()
    ce = input("Does this Villager have blue eyes? ").lower()
    if ce == "yes":
        print()
        print("\033[33m" "Is the Villager you're looking for named June?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/June")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if ce == "no":
        print()
        print("\033[33m" "Is the Villager you're looking for named Maple?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Maple")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# CUB - WHITE
  if cubColor == "white":
    print()
    cubGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if cubGender == "boy":
      print()
      print("\033[37m" "Is the Villager you're looking for named Chester?"
                  "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Chester")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if cubGender == "girl":
      print()
      print("\033[37m" "Is the Villager you're looking for named Pekoe?"
                  "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Pekoe")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")

# CHICKEN 
if species == "chicken":
   chickenColor = input("What is the main color of this Villager? ").lower()
# CHICKEN - BROWN
   if chickenColor == "brown":
    print()
    print("\033[33m" "Is the Villager you're looking for named Plucky?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Plucky")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CHICKEN - BLUE
   if chickenColor == "blue":
    print()
    print("\033[34m" "Is the Villager you're looking for named Ken?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Ken")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CHICKEN - YELLOW
   if chickenColor == "yellow":
    print()
    print("\033[33m" "Is the Villager you're looking for named Egbert?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Egbert")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CHICKEN - ORANGE
   if chickenColor == "orange":
    print()
    print("\033[33m" "Is the Villager you're looking for named Broffina?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Broffina")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CHICKEN - RED
   if chickenColor == "red":
    print()
    print("\033[31m" "Is the Villager you're looking for named Benedict?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Benedict")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CHICKEN - PURPLE
   if chickenColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Becky?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Becky")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# CHICKEN - WHITE
   if chickenColor == "white":
    print()
    chickenGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if chickenGender == "girl":
      print()
      print("\033[37m" "Is the Villager you're looking for named Ava?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Ava")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if chickenGender == "boy":
      print()
      hc = input("Does this Villager wear a helmet? ").lower()
      if hc == "yes":
        print()
        print("\033[37m" "Is the Villager you're looking for named Knox?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Knox")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if hc == "no":
        print()
        print("\033[37m" "Is the Villager you're looking for named Goose?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Goose")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")

# COW
if species == "cow":
  cowColor = input("What is the main color of this Villager? ").lower()
# COW - WHITE
  if cowColor == "white":
    print()
    print("\033[37m" "Is the Villager you're looking for named Tipper?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tipper")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# COW - BLUE
  if cowColor == "blue":
    print()
    print("\033[34m" "Is the Villager you're looking for named Naomi?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Naomi")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# COW - PINK
  if cowColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Norma?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Norma")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# COW - BROWN
  if cowColor == "brown":
    print()
    print("\033[33m" "Is the Villager you're looking for named Patty?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Patty")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")

# Eagle
if species == "eagle":
# EAGLE - RED
  eagleColor = input("What is the main color of this Villager? ").lower()
  if eagleColor == "red":
    print()
    print("\033[31m" "Is the Villager you're looking for named Amelia?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Amelia")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# EAGLE - PURPLE
  if eagleColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Quinn?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Quinn")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# EAGLE - GRAY
  if eagleColor == "gray":
    print()
    print("\033[30m" "Is the Villager you're looking for named Avery?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Avery")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# EAGLE - BROWN
  if eagleColor == "brown":
    print()
    print("\033[33m" "Is the Villager you're looking for named Buzz?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Buzz")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# EAGLE - GREEN
  if eagleColor == "green":
    print()
    print("\033[32m" "Is the Villager you're looking for named Frank?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Frank")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# EAGLE - YELLOW
  if eagleColor == "yellow":
    print()
    print("\033[33m" "Is the Villager you're looking for named Keaton?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Keaton")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# EAGLE - WHITe
  if eagleColor == "white":
    print()
    eagleGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if eagleGender == "girl":
      print()
      print("\033[32m" "Is the Villager you're looking for named Celia?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Celia")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if eagleGender == "boy":
      print()
      print("\033[37m" "Is the Villager you're looking for named Apollo?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Apollo")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# EAGLE - BLUE
  if eagleColor == "blue":
    print()
    sob = input("Does this Villager have several shades of blue on them? ").lower()
    if sob == "yes":
      print()
      print("\033[34m" "Is the Villager you're looking for named Pierce?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Pierce")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if sob == "no":
      print()
      print("\033[34m" "Is the Villager you're looking for named Sterling?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Sterling")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")

# DOG 
if species == "dog":
  dogColor = input("What is the main color of this Villager? ").lower()
# DOG - PINK
  if dogColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Cookie?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cookie")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# DOG - RED
  if dogColor == "red":
    print()
    print("\033[31m" "Is the Villager you're looking for named Cherry?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cherry")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# DOG - Orange
  if dogColor == "orange":
    print()
    print("\033[33m" "Is the Villager you're looking for named Biskit?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Biskit")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# DOG - YELLOW
  if dogColor == "yellow":
    print()
    dogGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    print()
    if dogGender == "girl":
      bte = input("Does this Villager have blue tipped ears? ").lower()
      if bte == "yes":
        print()
        print("\033[33m" "Is the Villager you're looking for named Daisy?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Daisy")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if bte == "no":
        print()
        print("\033[33m" "Is the Villager you're looking for named Goldie?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Goldie")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if dogGender == "boy":
      rl = input("Does this Villager have red lips? ").lower()
      if rl == "yes":
        print("\033[33m" "Is the Villager you're looking for named Benjamin?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Benjamin")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if rl == "no":
        print()
        print("\033[33m" "Is the Villager you're looking for named Frett?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Frett")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# DOG - WHITE
  if dogColor == "white":
    print()
    dogGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if dogGender == "girl":
        print()
        print("\033[37m" "Is the Villager you're looking for named Portia?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Portia")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if dogGender == "boy":
      print()
      ge = input("Does this Villager have one glowing yellow eye? ").lower()
      if ge == "yes":
        print()
        print("\033[37m" "Is the Villager you're looking for named Lucky?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Lucky")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if ge == "no":
        print()
        ghd = input("Does this Villager have a green scalp? ").lower()
        if ghd == "yes":
          print()
          print("\033[32m" "Is the Villager you're looking for named Marcel?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Marcel")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if ghd == "no":
          print()
          bs = input("Does this Villager have a brown spot over its eye? ").lower()
          if bs == "yes":
            print()
            print("\033[33m" "Is the Villager you're looking for named Bones?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Bones")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
          if bs == "no":
            print()
            print("\033[37m" "Is the Villager you're looking for named Walker?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Walker")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
# DOG - BROWN
  if dogColor == "brown":
    print()
    dogGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if dogGender == "girl":
      print()
      df = input("Does this Villager have freckles? ").lower()
      if df == "yes":
            print()
            print("\033[33m" "Is the Villager you're looking for named Bea?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Bea")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
      if df == "no":
            print()
            print("\033[33m" "Is the Villager you're looking for named Maddie?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Maddie")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
    if dogGender == "boy":
      print()
      sd = input("Does this Villager have hair covering its face? ").lower()
      if sd == "yes":
            print()
            print("\033[33m" "Is the Villager you're looking for named Shep?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Shep")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
      if sd == "no":
        print()
        rd = input("Does this Villager look like a rottweiler? ").lower()
        if rd == "yes":
            print()
            print("\033[33m" "Is the Villager you're looking for named Butch?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Butch")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
        if rd == "no":
            print()
            print("\033[33m" "Is the Villager you're looking for named Mac?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Mac")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")

# DUCK
if species == "duck":
  duckColor = input("What is the main color of this Villager? ").lower()
  print()
# DUCK - RED
  if duckColor == "red":
    duckGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if duckGender == "girl":
      print()
      print("\033[31m" "Is the Villager you're looking for named Ketchup?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Ketchup")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if duckGender == "boy":
      print()
      print("\033[31m" "Is the Villager you're looking for named Bill?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Bill")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# DUCK - PINK
  if duckColor == "pink":
    we = input("Are the eyes of this Villager set wide apart? ").lower()
    if we == "yes":
      print()
      print("\033[31m" "Is the Villager you're looking for named Freckles?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Freckles")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if we == "no":
      print()
      print("\033[31m" "Is the Villager you're looking for named Miranda?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Miranda")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# DUCK - WHITE
  if duckColor == "white":
    dhc = input("Does this Vilager have purple hair? ").lower()
    if dhc == "yes":
      print()
      print("\033[35m" "Is the Villager you're looking for named Gloria?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Gloria")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if dhc == "no":
      print()
      print("\033[37m" "Is the Villager you're looking for named Pompom?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Pompom")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# DUCK - BLUE 
  if duckColor == "blue":
    duckGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    print()
    if duckGender == "girl":
      print("\033[34m" "Is the Villager you're looking for named Pate?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Pate")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if duckGender == "boy":
      print("\033[34m" "Is the Villager you're looking for named Derwin?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Derwin")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# DUCK - YELLOW
  if duckColor == "yellow":
    duckGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if duckGender == "girl":
      print()
      print("\033[35m" "Is the Villager you're looking for named Maelle?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Maelle")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if duckGender == "boy":
      print()
      print("\033[33m" "Is the Villager you're looking for named Joey?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Joey")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# DUCK - PURPLE 
  if duckColor == "purple":
      print("\033[32m" "Is the Villager you're looking for named Mallary?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Mallary")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# DUCK - BROWN
  if duckColor == "brown":
    duckGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if duckGender == "girl":
      print()
      print("\033[33m" "Is the Villager you're looking for named Molly?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Molly")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if duckGender == "boy":
      print()
      print("\033[33m" "Is the Villager you're looking for named Weber?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Weber")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# DUCK - GREEN
  if duckColor == "green":
    duckGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if duckGender == "girl":
      print()
      print("\033[32m" "Is the Villager you're looking for named Deena?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Deena")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if duckGender == "boy":
       print()
       dbh = input("Does this Villager have blonde hair? ").lower()
       if dbh == "yes":
        print()
        print("\033[32m" "Is the Villager you're looking for named Quillson?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Quillson")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
       if dbh == "no":
         print()
         db = input("Does this Villager have bandages on its head? ").lower()
         if db == "yes":
            print()
            print("\033[32m" "Is the Villager you're looking for named Scoot?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Scoot")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
         if db == "no":
            print()
            print("\033[32m" "Is the Villager you're looking for named Drake?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Drake")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")

# DEER
if species == "deer":
  deerColor = input("What is the main color of this Villager? ").lower()
  # DEER - WHITE
  if deerColor == "white":
    print()
    deerGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
    "\033[30m""\033[37m""? ""\033[0m").lower()
    if deerGender == "boy":
      print()
      print("\033[37m" "Is the Villager you're looking for named Zell?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Zell")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if deerGender == "girl":
       print()
       dgh = input("Does this Villager have horns? ").lower()
       if dgh == "yes":
        print()
        print("\033[37m" "Is the Villager you're looking for named Shino?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Shino")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
       if dgh == "no":
          print()
          dhc = input("Does this Villager have green hair? ").lower()
          if dhc == "yes":
            print()
            print("\033[32m" "Is the Villager you're looking for named Chelsea?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Chelsea")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
          if dhc == "no":
            print()
            print("\033[37m" "Is the Villager you're looking for named Diana?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Diana")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
# DEER - BLUE
  if deerColor == "blue":
   print()
   fop = input("Does this Villager have freckles or lines on it's face? ").lower()
   if fop == "freckles":
    print()
    print("\033[34m" "Is the Villager you're looking for named Bam?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
     print()
     print("https://animalcrossing.fandom.com/wiki/Bam")
    if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
   if fop == "lines":
    print()
    print("\033[34m" "Is the Villager you're looking for named Bruce?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
     print()
     print("https://animalcrossing.fandom.com/wiki/Bruce")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# DEER - PINK
  if deerColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Fuchsia?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
     print()
     print("https://animalcrossing.fandom.com/wiki/Fuchsia")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# DEER - ORANGE
  if deerColor == "orange":
    print()
    print("\033[33m" "Is the Villager you're looking for named Lopez?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
     print()
     print("https://animalcrossing.fandom.com/wiki/Lopez")
    if yn == "no":
      print()
      print("Refresh the page and rethink your answers.")
# DEER - BROWN
  if deerColor == "brown":
     print()
     deerGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
     if deerGender == "boy":
        print()
        hoa = input("Does this Villager have horns or antlers? ").lower()
        if hoa == "horns":
          print("\033[32m" "Is the Villager you're looking for named Beau?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Beau")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if hoa == "antlers":
          print()
          print("\033[33m" "Is the Villager you're looking for named Erik?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Erik")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
     if deerGender == "girl":
        print()
        dls = input("Does this Villager have lipstick on? ").lower()
        if dls == "no":
          print()
          print("\033[33m" "Is the Villager you're looking for named Fauna?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Fauna")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if dls == "yes":
          print()
          print("\033[33m" "Is the Villager you're looking for named Deirdre?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Deirdre")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")

#Elephant
if species == "elephant":
  elephantColor = input("What is the color if this Villager? ").lower()
# Elephant - GREEN
  if elephantColor == "green":
    print()
    print("\033[32m" "Is the Villager you're looking for named Opal?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Opal")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# Elephant - YELLOW
  if elephantColor == "yellow":
      print()
      print("\033[33m" "Is the Villager you're looking for named Eloise?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Eloise")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# Elephant - RED
  if elephantColor == "red":
      print()
      print("\033[31m" "Is the Villager you're looking for named Cyd?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cyd")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# Elephant - PINK
  if elephantColor == "pink":
      print()
      print("\033[31m" "Is the Villager you're looking for named Paolo?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Paolo")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
 # Elephant - GRAY       
  if elephantColor == "gray":
      print()
      print("\033[30m" "Is the Villager you're looking for named Big Top?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Big_Top")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# ELEPHANT - BROWN
  if elephantColor == "brown":
      print()
      elephantGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
      if elephantGender == "boy":
        print()
        print("\033[33m" "Is the Villager you're looking for named Tucker?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Tucker")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if elephantGender == "girl":
        print()
        print("\033[33m" "Is the Villager you're looking for named Ellie ?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Ellie")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
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
          print("Refresh the page and rethink your answers.")
    if elephantGender == "boy":
      print()
      elephantDOL = input("Is this Villager a lighter or darker blue? ").lower()
      print()
      if elephantDOL == "darker":
        print("\033[34m" "Is the Villager you're looking for named Axel?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Axel")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if elephantDOL == "lighter":
        print("\033[34m" "Is the Villager you're looking for named Dizzy?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Dizzy")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# ELEPHANT - WHITE
  if elephantColor == "white":
    print()
    elephantStripe = input("Does this Villager have red and yellow stripes on them? ").lower()
    if elephantStripe == "no":
      print()
      print("\033[37m" "Is the Villager you're looking for named Tia?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tia")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if elephantStripe == "yes":
      print()
      print("\033[37m" "Is the Villager you're looking for named Margie?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Margie")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")

# FROG
if species == "frog":
   frogColor = input("What is the main color of this Villager? ").lower()
# FROG - RED
   if frogColor == "red":
    print()
    print("\033[31m" "Is the Villager you're looking for named Drift?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Drift")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# FROG - PINK
   if frogColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Puddles?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Puddles")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# FROG - GRAY
   if frogColor == "gray":
    print()
    rf = input("Is this Villager a robot? ").lower()
    if rf == "no":
      print()
      print("\033[37m" "Is the Villager you're looking for named Huck?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Huck")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if rf == "yes":
      print()
      print("\033[37m" "Is the Villager you're looking for named Ribbot?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Ribbot")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# FROG - BLUE
   if frogColor == "blue":
    print()
    print("\033[32m" "Is the Villager you're looking for named Jeremiah?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Jeremiah")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# FROG - yellow
   if frogColor == "yellow":
    print()
    print("\033[33m" "Is the Villager you're looking for named Consteau?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Consteau")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# FROG - orange
   if frogColor == "orange":
    print()
    fm = input("Does this Villager have a moustache? ").lower()
    if fm == "yes":
      print()
      print("\033[33m" "Is the Villager you're looking for named Croque?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Croque")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if fm == "no":
      print()
      print("\033[33m" "Is the Villager you're looking for named Walt Jr.?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Wart_Jr.")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# FROG - brown
   if frogColor == "brown":
      print()
      print("\033[33m" "Is the Villager you're looking for named Raddle?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Raddle")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# FROG - GREEN
   if frogColor == "green":
    print()
    frogGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" 
                      "\033[31m"" girl""\033[30m""\033[37m""? ""\033[0m").lower()
    if frogGender == "girl":
      print()
      fls = input("Is this Villager wearing lipstick? ").lower()
      if fls == "no":
        print()
        print("\033[32m" "Is the Villager you're looking for named Lily?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Lily")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if fls == "yes":
        print()
        print("\033[32m" "Is the Villager you're looking for named Jambette?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Jambette")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if frogGender == "boy":
      print()
      fc = input("Is there camo on this Villager? ").lower()
      if fc == "yes":
        print()
        print("\033[32m" "Is the Villager you're looking for named Camofrog?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Camofrog")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if fc == "no":
        print()
        yf = input("Does this Villager have yellow on it's face? ").lower()
        if yf == "yes":
          print("\033[33m" "Is the Villager you're looking for named Henry?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Henry")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if yf == "no":
          print()
          fs = input("Does this Villager have black spots on it's face? ").lower()
          if fs == "yes":
            print()
            print("\033[32m" "Is the Villager you're looking for named Frobert?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Frobert")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
          if fs == "no":
           print()
           fsg = input("Is this Villager just green? ").lower()
           if fsg == "no":
            print()
            print("\033[32m" "Is the Villager you're looking for named Prince?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Prince")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
           if fsg == "yes":
            print()
            print("\033[32m" "Is the Villager you're looking for named Tad?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Tad")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
# FROG - PURPLE
   if frogColor == "purple":
     print()
     sb = input("Does this Villager have long purple sideburns? ").lower()
     if sb == "yes":
            print()
            print("\033[35m" "Is the Villager you're looking for named Diva?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Diva")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
     if sb == "no":
            print()
            print("\033[37m" "Is the Villager you're looking for named Gigi?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Gigi")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")

# GOAT
if species == "goat":
  goatColor = input("What is the main color of this Villager? ").lower()
# GOAT - PINK
  if goatColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Velma?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Velma")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# GOAT - BLUE
  if goatColor == "blue":
    print()
    print("\033[34m" "Is the Villager you're looking for named Sherb?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Sherb")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# GOAT - WHITE
  if goatColor == "white":
    print()
    print("\033[37m" "Is the Villager you're looking for named Chevre?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Chevre")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# GOAT - GREEN
  if goatColor == "green":
    print()
    print("\033[32m" "Is the Villager you're looking for named Gruff?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Gruff")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# GOAT - PURPLE
  if goatColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Kidd?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Kidd")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# GOAT - BLACK
  if goatColor == "black":
    print()
    print("\033[30m" "Is the Villager you're looking for named Nan?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Nan")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# GOAT - BROWN
  if goatColor == "brown":
      print()
      goatColor = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" 
                      "\033[31m"" girl""\033[30m""\033[37m""? ""\033[0m").lower()
      if goatColor == "boy":
          print()
          print("\033[33m" "Is the Villager you're looking for named Billy?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Billy")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
      if goatColor == "girl":
          print()
          print("\033[33m" "Is the Villager you're looking for named Pashmina?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Pashmina")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")

# GORILLA
if species == "gorilla":
  gorillaColor = input("What is the main color of this Villager? ").lower()
# GORILLA - ORANGE
  if gorillaColor == "orange":
    print()
    print("\033[33m" "Is the Villager you're looking for named Cesar?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cesar")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# GORILLA - GREEN
  if gorillaColor == "green":
    print()
    print("\033[32m" "Is the Villager you're looking for named Al?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Al")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# GORILLA - PINK
  if gorillaColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Rilla?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rilla")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# GORILLA - BLUE
  if gorillaColor == "blue":
    print()
    teg = input("Does this Villager have tired eyes? ").lower()
    if teg == "yes":
      print()
      print("\033[34m" "Is the Villager you're looking for named Hans?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Hans")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if teg == "no":
      print()
      print("\033[34m" "Is the Villager you're looking for named Peewee?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Peewee")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# GORILLA - BROWN
  if gorillaColor == "brown":
    print()
    gorillaGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" 
                      "\033[31m"" girl""\033[30m""\033[37m""? ""\033[0m").lower()
    if gorillaGender == "girl":
      print()
      pop = input("Does this Villager have pink or purple fur? ").lower()
      if pop == "pink":
        print()
        print("\033[31m" "Is the Villager you're looking for named Rocket?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Rocket")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if pop == "purple":
        print()
        print("\033[35m" "Is the Villager you're looking for named Violet?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Violet")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if gorillaGender == "boy":
      print()
      mm = input("Does this Villager look like a Mandrill monkey? ").lower()
      if mm == "yes":
        print()
        print("\033[33m" "Is the Villager you're looking for named Boone?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Boone")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if mm == "no":
        print()
        rrs = input("Does this Villager have red appearing fur? ").lower()
        if rrs == "yes":
          print()
          print("\033[31m" "Is the Villager you're looking for named Boyd?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Boyd")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if rrs == "no":
          print()
          print("\033[33m" "Is the Villager you're looking for named Louie?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Louie")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")

# HAMSTER
if species == "hamster":
  hamsterColor = input("What is the main color of this Villager? ").lower()
  print()
# HAMSTER - RED
  if hamsterColor == "red":
    print("\033[31m" "Is the Villager you're looking for named Apple?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Apple")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HAMSTER - WHITE
  if hamsterColor == "white":
    print("\033[37m" "Is the Villager you're looking for named Flurry?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Flurry")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HAMSTER - BROWN
  if hamsterColor == "brown":
    pfh = input("Does this Villager have patterns all over its face? ").lower()
    if pfh == "yes":
      print()
      print("\033[33m" "Is the Villager you're looking for named Clay?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Clay")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if pfh == "no":
      print()
      print("\033[33m" "Is the Villager you're looking for named Hamlet?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Hamlet")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HAMSTER - ORANGE
  if hamsterColor == "orange":
    print("\033[33m" "Is the Villager you're looking for named Soleil?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Soleil")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HAMSTER - BLUE
  if hamsterColor == "blue":
    print("\033[34m" "Is the Villager you're looking for named Rodney?" "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rodney")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HAMSTER - BLACK
  if hamsterColor == "black":
    hs = input("Does this Villager look sad? ").lower()
    if hs == "no":
      print()
      print("\033[30m" "Is the Villager you're looking for named Hamphrey?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Hamphrey")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if hs == "yes":
      print()
      print("\033[30m" "Is the Villager you're looking for named Marlo?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Marlo")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HAMSTER - YELLOW
  if hamsterColor == "yellow":
      print("\033[33m" "Is the Villager you're looking for named Graham?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Graham")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")

# HIPPO
if species == "hippo":
  hippoColor = input("What is the main color of this Villager? ").lower()
# HIPPO - BLUE
  if hippoColor == "blue":
    print()
    print("\033[34m" "Is the Villager you're looking for named Bertha?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Bertha")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HIPPO - PINK
  if hippoColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Bitty?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Bitty")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HIPPO - YELLOW
  if hippoColor == "yellow":
    print()
    print("\033[33m" "Is the Villager you're looking for named Harry?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Harry")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HIPPO - BROWN
  if hippoColor == "brown":
    print()
    hippoGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" 
                      "\033[31m"" girl""\033[30m""\033[37m""? ""\033[0m").lower()
    if hippoGender == "boy":
          print()
          print("\033[33m" "Is the Villager you're looking for named Biff?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Biff")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
    if hippoGender == "girl":
          print()
          print("\033[33m" "Is the Villager you're looking for named Bubbles?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Bubbles")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
# HIPPO - GREEN
  if hippoColor == "green":
     print()
     hippoHair = input("Does this Villager have hair? ").lower()
     if hippoHair == "yes":
        print()
        print("\033[32m" "Is the Villager you're looking for named Hippeux?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Hippeux")
        if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
     if hippoHair == "no":
        print()
        print("\033[32m" "Is the Villager you're looking for named Rocco?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Rocco")
        if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")

# HORSE
if species == "horse":
  horseColor = input("What is the main color of this Villager? ").lower()
# HORSE - PINK
  if horseColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Peaches?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Peaches")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HORSE - BLACK
  if horseColor == "black":
    print()
    print("\033[30m" "Is the Villager you're looking for named Roscoe?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Roscoe")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HORSE - PURPLE
  if horseColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Cleo?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cleo")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HORSE - GREEN
  if horseColor == "green":
    print()
    horseGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if horseGender == "boy":
          print()
          print("\033[32m" "Is the Villager you're looking for named Buck?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Buck")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
    if horseGender == "girl":
          print()
          print("\033[32m" "Is the Villager you're looking for named Winnie?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Winnie")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
# HORSE - YELLOW
  if horseColor == "yellow":
    print()
    print("\033[33m" "Is the Villager you're looking for named Clyde?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Clyde")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# HORSE - WHITE
  if horseColor == "white":
    print()
    horseGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if horseGender == "boy":
        print()
        horseBangs = input("Does this Villager have blonde hair? ").lower()
        if horseBangs == "yes":
          print()
          print("\033[37m" "Is the Villager you're looking for named Colton?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Colton")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if horseBangs == "no":
          print()
          print("\033[37m" "Is the Villager you're looking for named Papi?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Papi")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
    if horseGender == "girl":
        print()
        print("\033[37m" "Is the Villager you're looking for named Savannah?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Savannah")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# HORSE - BROWN
  if horseColor == "brown":
    print()
    horseGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if horseGender == "boy":
          print()
          print("\033[33m" "Is the Villager you're looking for named Elmer?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Elmer")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
    if horseGender == "girl":
      print()
      phh = input("Does this Villager have pink hair? ").lower()
      if phh == "yes":
          print()
          print("\033[33m" "Is the Villager you're looking for named Annalise?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Annalise")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
      if phh == "no":
        print()
        girlHorseColor = input("Is this Villager a lighter or darker brown? ").lower()
        if girlHorseColor == "lighter":
          print()
          print("\033[33m" "Is the Villager you're looking for named Victoria?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Victoria")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if girlHorseColor == "darker":
          print()
          print("\033[33m" "Is the Villager you're looking for named Reneigh?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Reneigh")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
# HORSE - BLUE 
  if horseColor == "blue":
     print()
     horseHair = input("Is the Villager you're looking for have blonde hair? ").lower()
     if horseHair == "yes":
        print()
        print("\033[34m" "Is the Villager you're looking for named Ed?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Ed")
        if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
     if horseHair == "no":
        print()
        print("\033[34m" "Is the Villager you're looking for named Julian?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Julian")
        if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")

# Kangaroo
if species == "kangaroo":
  kangarooColor = input("What is the main color of this Villager? ").lower()
# KANGAROO - WHITE
  if kangarooColor == "white":
    print()
    print("\033[37m" "Is the Villager you're looking for named Astrid?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Astrid")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KANGAROO - PINK
  if kangarooColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Marcie?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Marcie")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KANGAROO - BLACK
  if kangarooColor == "black":
    print()
    print("\033[30m" "Is the Villager you're looking for named Mathilda?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Mathilda")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KANGAROO - BLUE
  if kangarooColor == "blue":
    print()
    print("\033[34m" "Is the Villager you're looking for named Rooney?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rooney")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KANGAROO - PURPLE
  if kangarooColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Sylvia?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Sylvia")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KANGAROO - GRAY
  if kangarooColor == "gray":
    print()
    print("\033[30m" "Is the Villager you're looking for named Walt?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Walt")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KANGAROO - BROWN
  if kangarooColor == "brown":
    print()
    print("\033[33m" "Is the Villager you're looking for named Kitt?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Kitt")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KANGAROO - ORANGE
  if kangarooColor == "orange":
    print()
    print("\033[33m" "Is the Villager you're looking for named Carrie?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Carrie")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")

# Koala
if species == "koala":
  koalaColor = input("What is the main color of this Villager? ").lower()
# KOALA - BLUE
  if koalaColor == "blue":
      print()
      print("\033[34m" "Is the Villager you're looking for named Yuka?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Yuka")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KOALA - PURPLE
  if koalaColor == "purple":
      print()
      print("\033[35m" "Is the Villager you're looking for named Sydney?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Sydney")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KOALA - GREEN
  if koalaColor == "green":
      print()
      print("\033[32m" "Is the Villager you're looking for named Lyman?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Lyman")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KOALA - GRAY
  if koalaColor == "gray":
      print()
      print("\033[30m" "Is the Villager you're looking for named Gonzo?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Gonzo")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KOALA - white
  if koalaColor == "white":
      print()
      print("\033[37m" "Is the Villager you're looking for named Eugene?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Eugene")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# KOALA - ORANGE
  if koalaColor == "orange":
        print()
        print("\033[33m" "Is the Villager you're looking for named Canberra?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Canberra")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# KOALA - YELLOW
  if koalaColor == "yellow":
        print()
        print("\033[33m" "Is the Villager you're looking for named Alice?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Alice")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# KOALA - BROWN
  if koalaColor == "brown":
    print()
    koalaGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
        "\033[30m""\033[37m""? ""\033[0m").lower()
    if koalaGender == "boy":
      print()
      print("\033[33m" "Is the Villager you're looking for named Ozzie?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Ozzie")
      if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if koalaGender == "girl":
      print()
      kc = input("Is there orange on this Villager? ").lower()
      if kc == "yes":
        print()
        print("\033[33m" "Is the Villager you're looking for named Faith?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Faith")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if kc == "no":
        print()
        print("\033[33m" "Is the Villager you're looking for named Melba?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Melba")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")

# LION
if species == "lion":
  lionColor = input("What is the main color of this Villager? ").lower()
# LION - YELLOW
  if lionColor == "yellow":
    print()
    ls = input("Does this Villager have a scar on its face? ").lower()
    if ls == "no":
      print()
      print("\033[33m" "Is the Villager you're looking for named Mott?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Mott")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if ls == "yes":
      print()
      print("\033[33m" "Is the Villager you're looking for named Elvis?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Elvis")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# LION - orange
  if lionColor == "orange":
    print()
    lm = input("Is the mane of this Villager brown? ").lower()
    if lm == "yes":
      print()
      print("\033[33m" "Is the Villager you're looking for named Rex?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rex")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if lm == "no":
      print()
      print("\033[33m" "Is the Villager you're looking for named Rory?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rory")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# LION  BROWN
  if lionColor == "brown":
    print()
    lm = input("Is the mane of this Villager green? ").lower()
    print()
    if lm == "yes":
      print("\033[32m" "Is the Villager you're looking for named Leopold?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Leopold")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if lm == "no":
      lmt = input("Is the mane of this Villager golden? ").lower()
      if lmt == "no":
        print()
        print("\033[33m" "Is the Villager you're looking for named Lionel?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Lionel")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if lmt == "yes":
        print()
        print("\033[33m" "Is the Villager you're looking for named Bud?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Bud")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")

# MONKEY
if species == "monkey":
     monkeyColor = input("What is the main color of this Villager? ").lower()
# MONKEY - PINK
     if monkeyColor == "pink":
      print()
      print("\033[31m" "Is the Villager you're looking for named Nana?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Nana")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
#MONKEY - YELLOW
     if monkeyColor == "yellow":
      print()
      print("\033[33m" "Is the Villager you're looking for named Tammi?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tammi")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
#MONKEY - orange
     if monkeyColor == "orange":
      print()
      print("\033[33m" "Is the Villager you're looking for named Tiansheng?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Tiansheng")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
#MONKEY - GRAY
     if monkeyColor == "gray":
       print()
       monkeyGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
        "\033[30m""\033[37m""? ""\033[0m").lower()
       if monkeyGender == "boy":
        print()
        print("\033[30m" "Is the Villager you're looking for named Monty?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Monty")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
       if monkeyGender == "girl":
        print()
        print("\033[30m" "Is the Villager you're looking for named Shari?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Shari")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# MONKEY - BROWN
     if monkeyColor == "brown":
       print()
       monkeyGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
        "\033[30m""\033[37m""? ""\033[0m").lower()
       if monkeyGender == "girl":
        print()
        print("\033[33m" "Is the Villager you're looking for named Elise?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Elise")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
       if monkeyGender == "boy":
        print()
        mrf = input("Does this Villager have red on it's face? ").lower()
        if mrf == "yes":
           print()
           print("\033[31m" "Is the Villager you're looking for named Simon?"
            "\033[0m")
           print()
           yn = input("Yes or No? ").lower()
           if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Simon")
           if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
        if mrf == "no":
          print()
          mwf = input("Does this Villager have white fur? ").lower()
          if mwf == "yes":
           print()
           print("\033[37m" "Is the Villager you're looking for named Deli?"
            "\033[0m")
           print()
           yn = input("Yes or No? ").lower()
           if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Deli")
           if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
          if mwf == "no":
           print()
           print("\033[33m" "Is the Villager you're looking for named Flip?"
            "\033[0m")
           print()
           yn = input("Yes or No? ").lower()
           if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Flip")
           if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")

# MOUSE
if species == "mouse":
  mouseColor = input("What is the color of the Villager? ").lower()
# MOUSE - PURPLE
  if mouseColor == "purple":
    print()
    print("\033[35m" "Is the Villager you're looking for named Rod?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rod")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# MOUSE - GRAY
  if mouseColor == "gray":
    mouseGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if mouseGender == "girl":
      print()
      print("\033[30m" "Is the Villager you're looking for named Penelope?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Penelope")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if mouseGender == "boy":
      print()
      print("\033[30m" "Is the Villager you're looking for named Samson?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Samson")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# MOUSE - YELLOW
  if mouseColor == "yellow":
    print()
    print("\033[33m" "Is the Villager you're looking for named Chadder?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Chadder")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# MOUSE - PINK
  if mouseColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Candi?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Candi")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# MOUSE - ORANGE
  if mouseColor == "orange":
    print()
    mouseGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if mouseGender == "girl":
      print()
      print("\033[33m" "Is the Villager you're looking for named Bettina?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Bettina")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if mouseGender == "boy":
      print()
      print("\033[33m" "Is the Villager you're looking for named Limberg?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Limberg")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# MOUSE - GREEN
  if mouseColor == "green":
    print()
    print("\033[32m" "Is the Villager you're looking for named Anicotti?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Anicotti")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# MOUSE - WHITE
  if mouseColor == "white":
    print()
    rabi = input("Are the insides of this Villars ears red and blue? ").lower()
    if rabi == "yes":
      print()
      print("\033[37m" "Is the Villager you're looking for named Petri?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Petri")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if rabi == "no":
      print()
      bi = input("Are the insides of this Villagers ears blue? ").lower()
      if bi == "yes":
        print()
        print("\033[34m" "Is the Villager you're looking for named Dora?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Dora")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if bi == "no":
        print()
        ghm = input("Does this Villager have green hair? ").lower()
        print()
        if ghm == "yes":
          print("\033[32m" "Is the Villager you're looking for named Bree?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Bree")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if ghm == "no":
          print("\033[37m" "Is the Villager you're looking for named Bella?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Bella")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
# MOUSE - BLUE
  if mouseColor == "blue":
    print()
    mouseGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
      "\033[30m""\033[37m""? ""\033[0m").lower()
    if mouseGender == "girl":
      print()
      print("\033[34m" "Is the Villager you're looking for named Greta?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Greta")
      if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
    if mouseGender == "boy":
      print()
      mh = input("Does this Villager have purple hair? ").lower()
      if mh == "yes":
        print()
        print("\033[34m" "Is the Villager you're looking for named Rizzo?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Rizzo")
        if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
      if mh == "no":
        print()
        mb = input("Does this Villager have brown bangs? ").lower()
        if mb == "yes":
          print()
          print("\033[34m" "Is the Villager you're looking for named Broccolo?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Broccolo")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if mb == "no":
          print()
          print("\033[34m" "Is the Villager you're looking for named Moose?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Moose")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")

# OCTOPUS
if species == "octopus":
  octopusColor =input("What is the main color of this Villager? ").lower()
# OCTOPUS - GRAY
  if octopusColor == "gray":
    print()
    print("\033[30m" "Is the Villager you're looking for named Cephalobot?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cephalobot")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# OCTOPUS - PINK
  if octopusColor == "pink":
    print()
    print("\033[31m" "Is the Villager you're looking for named Marina?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Marina")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# OCTOPUS - RED
  if octopusColor == "red":
    print()
    print("\033[31m" "Is the Villager you're looking for named Octavian?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Octavian")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# OCTOPUS - BROWN
  if octopusColor == "brown":
    print()
    print("\033[33m" "Is the Villager you're looking for named Zucker?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Zucker")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")

# Ostrich
if species == "ostrich":
  ostrichColor = input("What is the main color of this Villager? ").lower()
# Ostrich - RED
  if ostrichColor == "red":
      print()
      print("\033[31m" "Is the Villager you're looking for named Rio?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Rio")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# Ostrich - BLACK
  if ostrichColor == "black":
      print()
      print("\033[30m" "Is the Villager you're looking for named Gladys?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Gladys")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# Ostrich - PINK
  if ostrichColor == "pink":
      print()
      print("\033[31m" "Is the Villager you're looking for named Flora?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Flora")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# Ostrich - PURPLE
  if ostrichColor == "purple":
      print()
      ostrichGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
      if ostrichGender == "boy":
        print()
        print("\033[35m" "Is the Villager you're looking for named Phil?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Phil")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if ostrichGender == "girl":
        print()
        print("\033[35m" "Is the Villager you're looking for named Queenie?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Queenie")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# Ostrich - WHITE
  if ostrichColor == "white":
    print()
    ostrichGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if ostrichGender == "boy":
        print()
        print("\033[37m" "Is the Villager you're looking for named Cranston?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Cranston")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if ostrichGender == "girl":
        print()
        print("\033[37m" "Is the Villager you're looking for named Blanche?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Blanche")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# Ostrich - GREEN
  if ostrichColor == "green":
    print()
    ostrichGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if ostrichGender == "boy":
        print()
        print("\033[32m" "Is the Villager you're looking for named Sprocket?" "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Sprocket")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if ostrichGender == "girl":
        print()
        print("\033[32m" "Is the Villager you're looking for named Julia?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Julia")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# Ostrich - ORANGE
  if ostrichColor == "orange":
    print()
    ostrichVibe = input("Does this Villager look sleepy or fierce? ").lower()
    if ostrichVibe == "sleepy":
        print()
        print("\033[33m" "Is the Villager you're looking for named Sandy?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Sandy")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if ostrichVibe == "fierce":
        print()
        print("\033[33m" "Is the Villager you're looking for named Phoebe?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Phoebe")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")

# penguin
if species == "penguin":
  penguinColor = input("What is the main color of this Villager? ").lower()
# PENGUIN - GREEN
  if penguinColor == "green":
        print()
        print("\033[32m" "Is the Villager you're looking for named Boomer?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Boomer")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PENGUIN - PINK
  if penguinColor == "pink":
        print()
        print("\033[31m" "Is the Villager you're looking for named Puck?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Puck")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PENGUIN - PURPLE
  if penguinColor == "purple":
     print()
     nom = input("Is the bangs of this Villager neat or messy? ").lower()
     if nom == "messy":
        print()
        print("\033[35m" "Is the Villager you're looking for named Flo?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Flo")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
     if nom == "neat":
        print()
        print("\033[35m" "Is the Villager you're looking for named Gwen?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Gwen")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PENGUIN - BLACK
  if penguinColor == "black":
     print()
     pew = input("Does this Villager have yellow eyebrows? ").lower()
     if pew == "yes":
        print()
        print("\033[30m" "Is the Villager you're looking for named Hopper?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Hopper")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
     if pew == "no":
        print()
        print("\033[30m" "Is the Villager you're looking for named Cube?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Cube")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PENGUIN - WHITE
  if penguinColor == "white":
     print()
     penguinGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
     if penguinGender == "girl":
        print()
        pbob = input("Is this Villager's second color blue or black? ").lower()
        if pbob == "black":
          print()
          print("\033[30m" "Is the Villager you're looking for named Aurora?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Aurora")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if pbob == "blue":
          print()
          print("\033[34m" "Is the Villager you're looking for named Sprinkle?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Sprinkle")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
     if penguinGender == "boy":
        print()
        bof = input("Does this Villager have a patch of faded black on it's face? ").lower()
        if bof == "yes":
          print()
          print("\033[30m" "Is the Villager you're looking for named Wade?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Wade")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if bof == "no":
          print()
          print("\033[37m" "Is the Villager you're looking for named Iggly?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Iggly")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
# PENGUIN - BLUE
  if penguinColor == "blue":
    print()
    penguinGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if penguinGender == "girl":
          print()
          print("\033[34m" "Is the Villager you're looking for named Friga?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Friga")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
    if penguinGender == "boy":
       print()
       sep = input("Does this Villager have pink eyelids and looks tired? ").lower()
       print()
       if sep == "yes":
          print("\033[34m" "Is the Villager you're looking for named Tex?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Tex")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
       if sep == "no":
        bope = input("Does this Villager have big eyes? ").lower()
        if bope == "no":
          print()
          print("\033[34m" "Is the Villager you're looking for named Chabwick?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Chabwick")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if bope == "yes":
          print()
          print("\033[34m" "Is the Villager you're looking for named Roald?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Roald")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
      
# PIG
if species == "pig":
  pigColor = input("What is the main color of this Villager? ").lower()
# PIG - BLACK
  if pigColor == "black":
        print()
        print("\033[30m" "Is the Villager you're looking for named Agnes?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Agnes")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PIG - GREEN
  if pigColor == "green":
        print()
        print("\033[32m" "Is the Villager you're looking for named Cobb?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Cobb")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PIG - RED
  if pigColor == "red":
        print()
        print("\033[31m" "Is the Villager you're looking for named Rasher?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Rasher")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PIG - ORANGE
  if pigColor == "orange":
     print()
     pigGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
     if pigGender == "boy":
        print()
        print("\033[33m" "Is the Villager you're looking for named Kevin?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Kevin")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
     if pigGender == "girl":
        print()
        pbh = input("Does this Villager have blonde hair? ").lower()
        if pbh == "no":
          print()
          print("\033[33m" "Is the Villager you're looking for named Maggie?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Maggie")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if pbh == "yes":
          print()
          print("\033[33m" "Is the Villager you're looking for named Pancetti?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Pancetti")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
# PIG - PURPLE
  if pigColor == "purple":
        print()
        print("\033[35m" "Is the Villager you're looking for named Boris?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Boris")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PIG - BLUE
  if pigColor == "blue":
        print()
        print("\033[34m" "Is the Villager you're looking for named Hugh?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Hugh")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PIG - BROWN
  if pigColor == "brown":
   print()
   pigGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
   if pigGender == "girl":
    print()
    print("\033[33m" "Is the Villager you're looking for named Peggy?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Peggy")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
   if pigGender == "boy":
      print()
      pigGrin = input("Does this Villager have a grin on their face? ").lower()
      if pigGrin == "yes":
        print()
        print("\033[33m" "Is the Villager you're looking for named Spork?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Spork")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if pigGrin == "no":
        print()
        print("\033[33m" "Is the Villager you're looking for named Chops?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Chops")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PIG - WHITE
  if pigColor == "white":
        print()
        print("\033[37m" "Is the Villager you're looking for named Lucy?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Lucy")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# PIG - PINK
  if pigColor == "pink":
     print()
     pigGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
     if pigGender == "boy":
      print()
      print("\033[31m" "Is the Villager you're looking for named Curly?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Curly")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
     if pigGender == "girl":
        print()
        bbc = input("Does this Villager have a brown bowl cut? ").lower()
        if bbc == "yes":
          print()
          print("\033[31m" "Is the Villager you're looking for named Truffles?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Truffles")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if bbc == "no":
          print()
          print("\033[31m" "Is the Villager you're looking for named Gala?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Gala")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")

# RABBIT
if species == "rabbit":
  rabbitColor = input("What is the main color of this Villager? ").lower()
  print()
# RABBIT - RED
  if rabbitColor == "red":
    print()
    print("\033[31m" "Is the Villager you're looking for named Bunnie?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Bunnie")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# RABBIT - GREEN
  if rabbitColor == "green":
    print("\033[32m" "Is the Villager you're looking for named Sasha?"
            "\033[0m")
    print()
    yn = input("Yes or No? ").lower()
    if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Sasha")
    if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# RABBIT - WHITE
  if rabbitColor == "white":
    rabbitGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    print()
    if rabbitGender == "boy":
        print("\033[37m" "Is the Villager you're looking for named Genji?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Genji")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if rabbitGender == "girl":
      rer = input("Does this Villager have red eyes? ").lower()
      print()
      if rer == "yes":
        print("\033[37m" "Is the Villager you're looking for named Ruby?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Ruby")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if rer == "no":
        rwm = input("Does this Villager wear makeup? ").lower()
        print()
        if rwm == "yes":
          print("\033[37m" "Is the Villager you're looking for named Tiffany?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Tiffany")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if rwm == "no": 
          bhr = input("Does this Villager have brown hair? ").lower()
          print()
          if bhr == "yes":
            print("\033[33m" "Is the Villager you're looking for named Gabi?"
            "\033[0m")          
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Gabi")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
          if bhr == "no":
           br = input("Does this Villager have black ears? ").lower()
           if br == "yes":
              print()
              print("\033[37m" "Is the Villager you're looking for named Dotty?"
              "\033[0m")
              print()
              yn = input("Yes or No? ").lower()
              if yn == "yes":
                print()
                print("https://animalcrossing.fandom.com/wiki/Dotty")
              if yn == "no":
                print()
                print("Refresh the page and rethink your answers.")
           if br == "no":
            bhc = input("Is the headpiece on this Villager pink or blue? ").lower()
            print()
            if bhc == "pink":
              print()
              print("\033[31m" "Is the Villager you're looking for named Chrissy?"
              "\033[0m")
              print()
              yn = input("Yes or No? ").lower()
              if yn == "yes":
                print()
                print("https://animalcrossing.fandom.com/wiki/Chrissy")
              if yn == "no":
                print()
                print("Refresh the page and rethink your answers.")
            if bhc == "blue":
              print("\033[34m" "Is the Villager you're looking for named Francine?"
              "\033[0m")
              print()
              yn = input("Yes or No? ").lower()
              if yn == "yes":
                print()
                print("https://animalcrossing.fandom.com/wiki/Francine")
              if yn == "no":
                print()
                print("Refresh the page and rethink your answers.")
# RABBIT - PINK
  if rabbitColor == "pink":
     print("\033[31m" "Is the Villager you're looking for named Snake?"
            "\033[0m")
     print()
     yn = input("Yes or No? ").lower()
     if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Sanke")
     if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# RABBIT - BLUE
  if rabbitColor == "blue":
    rlod = input("Is this Villager a light or dark blue? ").lower()
    print()
    if rlod == "light":
      print("\033[34m" "Is the Villager you're looking for named Hopkins?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Hopkins")
      if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if rlod == "dark":
      print("\033[34m" "Is the Villager you're looking for named Doc?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Doc")
      if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# RABBIT - YELLOW
  if rabbitColor == "yellow":
    rhc = input("Does this Villager have a haircut? ").lower()
    print()
    if rhc == "yes":
       wrhc = input("What is the color of this Villager's hair? Light or dark green? ").lower()
       print()
       if wrhc == "light green":
        print("\033[32m" "Is the Villager you're looking for named Toby?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Toby")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
       if wrhc == "dark green":
        print()
        print("\033[32m" "Is the Villager you're looking for named Pippy?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Pippy")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if rhc == "no":
       print()
       rm = input("Does this rabbit have a moustache? ").lower()
       if rm == "no":
        print()
        print("\033[33m" "Is the Villager you're looking for named Mira?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Mira")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
       if rm == "yes":
        print()
        print("\033[33m" "Is the Villager you're looking for named Gaston?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Gaston")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# RABBIT - BROWN
  if rabbitColor == "brown":
     reye = input("Does this Villager have eyes? ").lower()
     print()
     if reye == "no":
        print("\033[33m" "Is the Villager you're looking for named Coco?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Coco")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
     if reye == "yes":
        rabbitGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
        print()
        if rabbitGender == "girl":
           print()
           grh = input("Does this Villager have blonde hair? ").lower()
           if grh == "yes":
              print()
              print("\033[33m" "Is the Villager you're looking for named Bonbon?"
            "\033[0m")
              print()
              yn = input("Yes or No? ").lower()
              if yn == "yes":
                print()
                print("https://animalcrossing.fandom.com/wiki/Bonbon")
              if yn == "no":
                print()
                print("Refresh the page and rethink your answers.")
           if grh == "no":
              print()
              print("\033[33m" "Is the Villager you're looking for named Carmen?"
            "\033[0m")
              print()
              yn = input("Yes or No? ").lower()
              if yn == "yes":
                print()
                print("https://animalcrossing.fandom.com/wiki/Carmen")
              if yn == "no":
                print()
                print("Refresh the page and rethink your answers.")
        if rabbitGender == "boy":
           rec = input("Does this Villager have blue eyes? ").lower()
           print()
           if rec == "yes":
              print("\033[33m" "Is the Villager you're looking for named Cole?"
            "\033[0m")
              print()
              yn = input("Yes or No? ").lower()
              if yn == "yes":
                print()
                print("https://animalcrossing.fandom.com/wiki/Cole")
              if yn == "no":
                print()
                print("Refresh the page and rethink your answers.")
           if rec == "no":
              unir = input("Does this Villager have a unibrow? ").lower()
              print()
              if unir == "no":
                print("\033[33m" "Is the Villager you're looking for named " "O’Hare?"
            "\033[0m")
                print()
                yn = input("Yes or No? ").lower()
                if yn == "yes":
                  print()
                  print("https://animalcrossing.fandom.com/wiki/O%27Hare")
                if yn == "no":
                  print()
                  print("Refresh the page and rethink your answers.")
              if unir == "yes":
                print("\033[33m" "Is the Villager you're looking for named Claude?"
            "\033[0m")
                print()
                yn = input("Yes or No? ").lower()
                if yn == "yes":
                  print()
                  print("https://animalcrossing.fandom.com/wiki/Claude")
                if yn == "no":
                  print()
                  print("Refresh the page and rethink your answers.")

# RHINO 
if species == "rhino":
  rhinoColor = input("What is the main color of this Villager? ").lower()
  print()
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
 # RHINO - BLUE
  if rhinoColor == "blue":
    rhinoGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if rhinoGender == "boy":
        print()
        bnr = input("Is this Villager a gray blue? ").lower()
        if bnr == "no":
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
            print("Refresh the page and rethink your answers.")
        if bnr == "yes":
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
            print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
# RHINO - PINK
  if rhinoColor == "pink":
      print()
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
        print("Refresh the page and rethink your answers.")
# RHINO - PURPLE
  if rhinoColor == "purple":
      print()
      print("\033[35m" "Is the Villager you're looking for named Renée?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Renée")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")

# SHEEP
if species == "sheep":
  sheepColor = input("What is the color of this Villagers face? ").lower()
# SHEEP - GREEN
  if sheepColor == "green":
      print()
      print("\033[32m" "Is the Villager you're looking for named Cashmere?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Cashmere")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# SHEEP - YELLOW
  if sheepColor == "yellow":
      print()
      print("\033[33m" "Is the Villager you're looking for named Curlos?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Curlos")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# SHEEP - BLUE
  if sheepColor == "blue":
      print()
      print("\033[34m" "Is the Villager you're looking for named Vesta?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Vesta")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# SHEEP - WHITE
  if sheepColor == "white":
    print()
    cs = input("Does this Villager look like a clown? ").lower()
    if cs == "yes":
      print()
      print("\033[37m" "Is the Villager you're looking for named Pietro?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Pietro")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if cs == "no":
      print()
      print("\033[37m" "Is the Villager you're looking for named Muffy?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Muffy")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# SHEEP - BROWN
  if sheepColor == "brown":
    print()
    ow = input("Does this Villager have orange wool? ").lower()
    if ow == "yes":
      print()
      print("\033[33m" "Is the Villager you're looking for named Frita?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Frita")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if ow == "no":
     print()
     yw = input("Does this Villager have yellow wool? ").lower()
     if yw == "no":
      print()
      print("\033[34m" "Is the Villager you're looking for named Baabara?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Baabara")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if yw == "yes":
      print()
      print("\033[33m" "Is the Villager you're looking for named Willow?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Willow")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# SHEEP - ORANGE
  if sheepColor == "orange":
    print()
    bw = input("Does this Villager have bue wool? ").lower()
    print()
    if bw == "yes":
      print("\033[34m" "Is the Villager you're looking for named Wendy?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Wendy")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if bw == "no":
      print("\033[33m" "Is the Villager you're looking for named Timbra?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Timbra")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# SHEEP - PINK
  if sheepColor == "pink":
    print()
    sheepGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if sheepGender == "boy":
      print()
      print("\033[31m" "Is the Villager you're looking for named Dom?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Dom")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if sheepGender == "girl":
      print()
      sbw = input("Does this Villager have blue wool? ").lower()
      if sbw == "yes":
        print()
        print("\033[34m" "Is the Villager you're looking for named Eunice?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Eunice")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if sbw == "no":
        print()
        lpw = input("Does this Villager have light purple wool? ").lower()
        if lpw == "yes":
          print()
          print("\033[35m" "Is the Villager you're looking for named Etoile?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Etoile")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
        if lpw == "no":
          print()
          print("\033[31m" "Is the Villager you're looking for named Stella?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Stella")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")

# Squirrel
if species == "squirrel":
  squirrelColor = input("What is the main color of this Villager? ").lower()
# SQUIRREL - WHITE
  if squirrelColor == "white":
      print()
      print("\033[37m" "Is the Villager you're looking for named Marshall?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Marshall")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# SQUIRREL - BROWN
  if squirrelColor == "brown":
    print()
    squirrelGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if squirrelGender == "boy":
      print()
      print("\033[33m" "Is the Villager you're looking for named Ricky?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Ricky")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if squirrelGender == "girl":
        print()
        squirrelBlush = input("Does this Villager have blush marks on their face? ").lower()
        if squirrelBlush == "yes":
          print()
          squirrelUni = input("Does this Villager have a unibrow? ").lower()
          if squirrelUni == "yes":
            print()
            print("\033[33m" "Is the Villager you're looking for named Hazel?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Hazel")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
          if squirrelUni == "no":
            print()
            print("\033[33m" "Is the Villager you're looking for named Cally?"
            "\033[0m")
            print()
            yn = input("Yes or No? ").lower()
            if yn == "yes":
              print()
              print("https://animalcrossing.fandom.com/wiki/Cally")
            if yn == "no":
              print()
              print("Refresh the page and rethink your answers.")
        if squirrelBlush == "no":
           print()
           squirrelShadow = input("Does this have eyeshadow? ").lower()
           if squirrelShadow == "yes":
              print()
              sst = input("What is the color of this eyeshadow? ").lower()
              if sst == "pink":
                print()
                print("\033[35m" "Is the Villager you're looking for named Pecan?"
            "\033[0m")
                print()
                yn = input("Yes or No? ").lower()
                if yn == "yes":
                  print()
                  print("https://animalcrossing.fandom.com/wiki/Pecan")
                if yn == "no":
                  print()
                  print("Refresh the page and rethink your answers.")
              if sst == "purple":
                print()
                print("\033[31m" "Is the Villager you're looking for named Sally?"
            "\033[0m")
                print()
                yn = input("Yes or No? ").lower()
                if yn == "yes":
                  print()
                  print("https://animalcrossing.fandom.com/wiki/Sally")
                if yn == "no":
                  print()
                  print("Refresh the page and rethink your answers.")
           if squirrelShadow == "no":
              print()
              print("\033[33m" "Is the Villager you're looking for named Sylvana?"
            "\033[0m")
              print()
              yn = input("Yes or No? ").lower()
              if yn == "yes":
                print()
                print("https://animalcrossing.fandom.com/wiki/Sylvana")
              if yn == "no":
                print()
                print("Refresh the page and rethink your answers.")
# SQUIRREL - PINK
  if squirrelColor == "pink":
      print()
      print("\033[31m" "Is the Villager you're looking for named Peanut?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Peanut")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# SQUIRREL - ORANGE
  if squirrelColor == "orange":
      print()
      squirrelGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
      if squirrelGender == "boy":
        print()
        print("\033[33m" "Is the Villager you're looking for named Sheldon?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Sheldon")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
      if squirrelGender == "girl":
        print()
        print("\033[37m" "Is the Villager you're looking for named Caroline?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
         print()
         print("https://animalcrossing.fandom.com/wiki/Caroline")
        if yn == "no":
         print()
         print("Refresh the page and rethink your answers.")
# SQUIRREL - RED
  if squirrelColor == "red":
        print()
        print("\033[31m" "Is the Villager you're looking for named Poppy?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Poppy")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# SQUIRREL - PURPLE
  if squirrelColor == "purple":
        print()
        print("\033[35m" "Is the Villager you're looking for named Static?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Static")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# SQUIRREL - GRAY
  if squirrelColor == "gray":
    dse = input("Does this Villager have droopy eyes? ").lower()
    if dse == "yes":
        print()
        print("\033[37m" "Is the Villager you're looking for named Agent S?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Agent_S")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
    if dse == "no":
        print()
        print("\033[37m" "Is the Villager you're looking for named Blaire?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Blaire")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")
# SQUIRREL - GREEN
  if squirrelColor == "green":
    print()
    fob = input("Does this Villager have freckles? ").lower()
    if fob == "no":
      print()
      print("\033[32m" "Is the Villager you're looking for named Mint?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Mint")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if fob == "yes":
      print()
      print("\033[32m" "Is the Villager you're looking for named Nibbles?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Nibbles")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
# SQUIRREL  - BUE
  if squirrelColor == "blue":
    print()
    squirrelGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if squirrelGender == "boy":
      print()
      print("\033[37m" "Is the Villager you're looking for named Filbert?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Filbert")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if squirrelGender == "girl":
       print()
       orbe = input("Does this Villager have orange or blue eyes? ").lower()
       if orbe == "orange":
          print()
          print("\033[34m" "Is the Villager you're looking for named Tasha?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Tasha")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
       if orbe == "blue":
          print()
          print("\033[37m" "Is the Villager you're looking for named Ione?"
            "\033[0m")
          print()
          yn = input("Yes or No? ").lower()
          if yn == "yes":
            print()
            print("https://animalcrossing.fandom.com/wiki/Ione")
          if yn == "no":
            print()
            print("Refresh the page and rethink your answers.")
  
# TIGER
if species == "tiger":
  tigerColor = input("What is the main color of this Villager? ").lower()
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
# TIGER - WHITE
    print()
  if tigerColor == "white":
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
        print("Refresh the page and rethink your answers.")
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
         print("Refresh the page and rethink your answers.")

# WOLF
if species == "wolf":
  wolfColor = input("What is the main color of this Villager? ").lower()
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
# WOLF - GRAY
  if wolfColor == "gray":
    print()
    wolfAge = input("Does this Villager look old or young? ").lower()
    if wolfAge == "young":
     print()
     print("\033[30m" "Is the Villager you're looking for named Fang?"
            "\033[0m")
     print()
     yn = input("Yes or No? ").lower()
     if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Fang")
     if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
# WOLF - BROWN
  if wolfColor == "brown":
    print()
    wolfGender = input("Is the Villager you're looking for a" "\033[34m" " boy " "\033[30m" "\033[37m""or a""\033[30m" "\033[31m"" girl" 
                       "\033[30m""\033[37m""? ""\033[0m").lower()
    if wolfGender == "boy":
      print()
      print("\033[33m" "Is the Villager you're looking for named Kyle?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Kyle")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
    if wolfGender == "girl":
      print()
      print("\033[33m" "Is the Villager you're looking for named Vivian?"
            "\033[0m")
      print()
      yn = input("Yes or No? ").lower()
      if yn == "yes":
        print()
        print("https://animalcrossing.fandom.com/wiki/Vivian")
      if yn == "no":
        print()
        print("Refresh the page and rethink your answers.")
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
        print("Refresh the page and rethink your answers.")
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
          print("Refresh the page and rethink your answers.")
      if cuteOrSleek == "sleek":
        print()
        print("\033[34m" "Is the Villager you're looking for named Whitney?"
            "\033[0m")
        print()
        yn = input("Yes or No? ").lower()
        if yn == "yes":
          print()
          print("https://animalcrossing.fandom.com/wiki/Whitney")
        if yn == "no":
          print()
          print("Refresh the page and rethink your answers.")