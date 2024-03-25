print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay, let's play! Please input all answers as lowercase, even for proper nouns.")

score = 0

answer1 = input("What does CPU stand for? ")
if answer1 == "central processing unit":
    print("Correct!")
    score+=1
else: print("Incorrect!")

answer2 = input("What does GPU stand for? ")
if answer2 == "graphics processing unit":
    print("Correct!")
    score+=1
else: print("Incorrect!")

answer3 = input("What year did the great war begin in Fallout? ")
if answer3 == "2076":
    print("Correct!")
    score+=1
else: print("Incorrect!")

answer4 = input("What does RAM stand for? ")
if answer4 == "random access memory":
    print("Correct!")
    score+=1
else: print("Incorrect!")

answer5 = input("Who is the main antagonist in Borderlands 2? ")
if answer5 == "handsome jack":
    print("Correct!")
    score+=1
else: print("Incorrect!")

answer6 = input("What is the scientific division which both german scientists Edward Richtofen and Ludvig Maxis joined? group 88, division 66, group 935, or alliance 725? ")
if answer6 == "group 935":
    print("Correct!")
    score+=1
else: print("Incorrect!")

answer7 = input("In Der Eisendrache, which of the 4 characters are we there for? Richtofen, Takeo, Dempsey, or Nikolai? ")
if answer7 == "dempsey":
    print("Correct!")
    score+=1
else: print("Incorrect!")

answer8 = input("What was the original name of the Russian city Stalingrad? ")
if answer8 == "leningrad":
    print("Correct!")
    score+=1
else: print("Incorrect!")

answer9 = input("Who is the current leader of the country of Russia? (last name only, also lowercase!) ")
if answer9 == "putin":
    print("Correct!")
    score+=1
else: print("Incorrect!")

answer10 = input("What is the meaning of life? (Don't panic!)) ")
if answer10 == "42":
    print("Correct!")
    score+=1
else: print("Incorrect!")

print(f"Congratulations! You have completed the game! you have {score} points")