name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
  "You are lost on a dirt road, it has come to an end and you can go left or right. Which way will you choose? ").lower()

if answer == "left":
  answer = input("You come to a river, you can walk around it or swim across? Type 'walk' to walk around, or 'swim' to swim across ")
  
  if answer == "swim":
    print("You swim across and are eaten by a Hippo!")
  elif answer == "walk":
    print("You walked for many miles, ran out of water, and died of thirst.")    
  else:
    print("Not a valid option. You are hit by a bolt of lightning and die.")
    
    
  
elif answer == "right":
  answer = input("You come to a bridge. It looks risky. Do you want to cross it or head back (cross/back)? ")
  
  if answer == "cross":
    answer = input("You make your way across the shaky bridge, you almost slip and fall into the ravine! but you make it through safely. You encounter a stranger at the other side of the bridge. Do you talk to them (yes/no)? ")
    
    if answer == "yes":
      print("The stranger says he is a magical leprechaun and he hands you a pot of gold! Hooray you win!!")
    elif answer == "no":
      print("You ignore the stranger, and they are offended and they blast you with a fireball and you die. You lose.")
    
  elif answer == "back":
    print("You walked for many miles, ran out of water, and died of thirst. You lose.")    
  else:
    print("Not a valid option. You are hit by a bolt of lightning and die. You lose.")
  
else:
  print("Not a valid option. You are hit by a bolt of lightning and die.")