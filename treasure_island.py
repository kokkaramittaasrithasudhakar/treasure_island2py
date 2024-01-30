#project3:  Treasure island

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



#Write your code below this line 👇
print("You are at a crossroads. To the left is a dark forest, to the right is a beautiful beach.")

direction = input("Which way do you want to go? Left or Right? ").lower()

if direction == "left":
  print("You walk into the forest and find a river. You can either swim across or wait for a boat.")

  river = input("Do you want to swim or wait? ").lower()
  if river == "wait":
    print("You wait for a boat and cross the river safely. You come to a castle with three doors. One is red, one is yellow, and one is blue.")

    door = input("Which door do you want to open? Red, Yellow, or Blue? ").lower()
    if door == "red":
      print("You open the red door and are engulfed in flames. Game Over.")
    elif door == "yellow":
      print("You open the yellow door and find the treasure! You win!")
    elif door == "blue":
      print("You open the blue door and are attacked by a pack of wolves. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")#3rd else choose color beyond red/yellow/blue

  else:
    print("You try to swim across the river but are attacked by a trout. Game Over.")#2nd else if choosen to swim

else:
  print("You walk along the beach and are attacked by a shark. Game Over.")#1st else if took right


