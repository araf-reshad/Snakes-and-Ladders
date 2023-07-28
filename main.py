# Importing the turtle module
from turtle import *
from turtle import _CFG  # this dictionary to be imported separately
from random import randint 

# Resizes the default canvas size to prevent scrollbars
_CFG["canvwidth"] = 1
_CFG["canvheight"] = 1

# Creates a window with the size 570 by 550 to fit the Snake and Ladders board
setup(570, 550)

# Title
title("Snakes and Ladders")

# Display the Snakes and Ladders board
Screen().bgpic('snakes_and_ladder.gif')

# Keep track of which square the Player and Computer are on respectively. Both start the game at square 0
player_pos = [0, 0]

# 0th index represents human player, 1st index is the computer player, 2nd index is an invisble turtle used to create delay
players_list = [Turtle(), Turtle(), Turtle()] 

# Initialize the players' speed, shape, colour and starting location
players_list[0].speed(1)
players_list[1].speed(1)
players_list[0].hideturtle()
players_list[1].hideturtle()
players_list[2].hideturtle()
players_list[0].penup()
players_list[1].penup() 
players_list[2].penup()
players_list[0].shape("turtle")
players_list[1].shape("turtle")
players_list[0].color("purple")
players_list[1].color("cyan")
players_list[0].goto(-280, -215)
players_list[1].goto(-280, -245)
players_list[0].showturtle()
players_list[1].showturtle()

""" This function uses an invisble turtle to create a delay """
def delay():
  
  players_list[2].circle(50)

""" This function moves the specified turtle to the location indicated by the die
player_id specifies which turtle to move (the Player (0) or the Computer (1) )
current_pos is the starting square of the current player
end_pos is destination square calculated by adding the result of the die to current_pos """
def move_forward(player_id, current_pos, end_pos):
  
    player = players_list[player_id]
  
    # Players must reach exactly square 100 to win, otherwise their turn is skipped
  
    if end_pos > 100:
      print("Uh oh, it is impossible to go more than 100! This turn is skipped!\n")
      return

    while current_pos != end_pos:
              
        if (current_pos % 10 == 0 or current_pos % 10 == 1):
            # Squares 0 and 1 are special cases 
            if current_pos == 0 or current_pos ==1:
                pass
              
            # Turn left at squares 10 and 11, 30 and 31, 50 and 51, etc   
            elif (current_pos // 10) % 2 == 1:
                player.left(90)
              
            # Turn right at squares 20 and 21, 40 and 41, 60 and 61, etc    
            else:                                       
                player.right(90)
              
        # Move the player and update their position
        player.forward(50)
        current_pos += 1

""" This function moves the player to a specified square in a straight line. 
It is used to simulate the Snakes and the Ladders. 
player_id specifies which turtle to move (the Player (0) or the Computer (1) )
end_pos specifies which square to move to """
def move_to(player_id, end_pos):
  
  player = players_list[player_id]

  # Print a helpful message indicating whether a Ladder or Snake has been encountered
  if(end_pos > player_pos[player_id]):
    print("Wow a ladder! Very helpful!!\n")
    
  else:
    print("Oh no a snake! Down you go!!\n")

  delay()

  # Calculate the location of squares 10, 30, 50, etc on the grid
  if end_pos//10%2==1 and end_pos%10==0:
    x_pos = 9
    y_pos = end_pos//10 - 1

  # Calculate the location of squares 11-19, 31-39, 51-59, etc on the grid
  elif end_pos//10%2==1 and end_pos%10!=0:
    x_pos = 10 - end_pos%10
    y_pos = end_pos//10
    
  # Calculate the location of squares 20, 40, 60, etc on the grid
  elif (end_pos//10%2==0 and end_pos%10 == 0): 
    x_pos = 0
    y_pos = end_pos//10 - 1

  # Calculate the location of squares 21-29, 41-49, 61-69, etc on the grid
  else:
    x_pos = end_pos%10 - 1
    y_pos = end_pos//10

  # Once we know the location of the squares on the grid, we can express it as pixels
  x_pos = -230 + x_pos*50 
  y_pos = -230 + y_pos*50

  # Adjust the postions of the player to avoid overlapping 
  if player_id == 0:
    y_pos += 15
    
  else :
    y_pos -= 15

  # Move the player to the final position
  player.goto(x_pos, y_pos)

  # Make the player face the correct direction
  if end_pos == 1:
    player.setheading(0)
    
  elif (end_pos//10%2==0 and end_pos%10!=0) or (end_pos//10%2==1 and end_pos%10==0):
    player.setheading(0)
    
  elif end_pos%10==1:
    player.setheading(90)
    
  else:
    player.setheading(180)

  # Update the player's final position
  player_pos[player_id] = end_pos

# Print the instructions the the game
print("""Welcome Dear Player to Snakes and Ladders!

The rules of this game are very simple: 

Every turn, both you and your opponent will roll a 6 sided die 
to see how many squares each of you will advance.

First to reach square 100 wins!

But do be careful of the Snakes! They can gobble you up 
and send you all the way back near the start! 

Try to get to the Ladders instead! They can send you up 
and closer to the finish line!


One more catch: 

You need to reach EXACTLY the 100th square to win, 
and not a single square more. 

For example, if you are at the 99th square and you roll a 2 on your die, 
you should advance to the 101th square.

However, that is out of bounds so your turn will be skipped! 
Next turn if you roll a 1, you will reach the 100th square exactly.
Then its your victory :) 


That's all. Good luck, brave player.

""")
input("Press Enter to start the game ") 

print("-----------------------------------------\n")

# The Player (human) goes first, the Computer goes second
current_player = 0 

# Continue the game loop until a winner is decided 
while player_pos[0]!=100 and player_pos[1]!=100:
  
  delay() 

  # The Player is prompted to roll the dice
  if current_player==0:
    print("Player's (Purple) Turn\n")
    input("Please press Enter to roll the dice ")

  # The Computer rolls the dice automatically after a short delay
  else:
    delay()
    print("Computer's (Cyan) Turn\n")
    print("The computer is rolling the dice! ")
  
  # Die is rolled
  step = randint(1,6)
  
  print("\nThe die rolled", step, "!!\n")

  # Move the player forward
  move_forward(current_player, player_pos[current_player], player_pos[current_player] + step)

  # Update the position if the player did not attempt to go beyond sqaure 100 
  if player_pos[current_player] + step <= 100:
    player_pos[current_player] += step

  # Simulate the Snakes and the Ladders
  if player_pos[current_player]==1:
    move_to(current_player, 38)
    
  elif player_pos[current_player]==4:
    move_to(current_player, 14)

  elif player_pos[current_player]==9:
    move_to(current_player, 31)
    
  elif player_pos[current_player]==17:
    move_to(current_player, 7)

  elif player_pos[current_player]==21:
    move_to(current_player, 42)
    
  elif player_pos[current_player]==28:
    move_to(current_player, 84)
    
  elif player_pos[current_player]==51:
    move_to(current_player, 67)
    
  elif player_pos[current_player]==54:
    move_to(current_player, 34)
    
  elif player_pos[current_player]==62:
    move_to(current_player, 19)
    
  elif player_pos[current_player]==64:
    move_to(current_player, 60)
    
  elif player_pos[current_player]==71:
    move_to(current_player, 91)
    
  elif player_pos[current_player]==80:
    move_to(current_player, 99)
    
  elif player_pos[current_player]==87:
    move_to(current_player, 24)
    
  elif player_pos[current_player]==93:
    move_to(current_player, 73)
    
  elif player_pos[current_player]==95:
    move_to(current_player, 75)
    
  elif player_pos[current_player]==98:
    move_to(current_player, 79)

  # Print a message saying the final position of the current  player
  if(current_player==0):
    print("Player ", end = "")
    
  else:
    print("Computer ", end="")
    
  print("is at square", player_pos[current_player], "\n")
  
  print("-----------------------------------------\n")

  # Alternate between players
  current_player=(current_player+1)%2

#Display winning message 
if(player_pos[0]==100):
  print("Winner winner chicken dinner! Player has won the round!")
  
else:
  print("Uh oh the computer won! Better luck next time!")

print("\nThanks for playing ^-^")

done()
move