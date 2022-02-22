print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
name = input("Before we begin, what is your name? ")
game_over = (f"Wow {name}, why did you even come here if you werent ready to go on an adventure?")
game_over1 = (f"Unfortunately {name}, you have fallen into a pitfall and died a painful, lonely death.")
game_over2 = (f"That's a shame {name}, you were unable to swim across the lake.\nMaybe next time you will invest in those swimming lessons your grandmother recommended at the community pool.")
game_over3 = (f"It appears you are colorblind, the corect door was the opposite door. \nGood luck in your next life {name}")
winning = (f"Incredible {name}, You have successfully found the treasure. \nWill you finally feel the warm embrace of accomplishments that your father failed to give you? \nProbably not, but atleast you won.")

greetings = input(f"Greetings {name}, are you ready for an excellent adventure? \"Y\" or \"N?\" \n").lower()
if greetings == "y":
  first_choice = input(f"There are two doors in front of you. \nWould you like to take the door on the \"right\",\nor the door on the \"left\"\n").lower()

  if first_choice == "right":
    second_choice = input(f"Miracously, you survived the first test. Now, against \neverything that should be possible, there is a lake in front of you. Would you like to \"swim\"Or wait for the \"ferry\"?\n").lower()
    
    if second_choice == "ferry":
      third_choice = input(f"I'm impressed {name}, you have successfully navigated the lake. \nYou now find yourself in another room, but this time there are three doors.\nWhich door will you take? The \"green\", The \"yellow\", or the \"blue\" door?\n").lower()

      if third_choice == "yellow":
        print(winning)
      elif third_choice == "blue":
        print(f"Wow, {name}, You made it this far to just lose?")
      else:
        print(game_over3)
    else:
      print(game_over2)
  else:
    print(game_over1)
else:
  print(game_over)