# turtle game using package 'turtle' !

#  Import relevant modules
import random
import turtle
import time

# Setting up a nice screen for our game !
screen = turtle.Screen()
screen.bgcolor('Grey')  # background a light blue color .


# We want 2 players in this game and whoever goes to the other side first , wins !

# Player one - basic setup.
player_one = turtle.Turtle()
# Color of the player one
player_one.color('Black')
# make this player a turtle .
player_one.shape('turtle')


#player two - basic setup
player_two = player_one.clone()
# color of player two
player_two.color('red')

# let's position our players
player_one.penup()
player_one.goto(-300,200)
player_two.penup()
player_two.goto(-300,-200)

#now let's draw a finish line!
player_one.goto(300,-250)
player_one.left(90)
player_one.pendown()
player_one.color('blue')
player_one.forward(500)
player_one.write('Finish',font=24)
# Allows player one to return to its starting position
player_one.penup()
player_one.color('white')
player_one.goto(-300,200)
player_one.right(90)


#Now we need to make sure that both players have their pens down
player_one.pendown()
player_two.pendown()


# Let's create value for the die
die = [1,2,3,4,5,6]

# let's create the game !

for i in range(30):
    if player_one.pos() >= (300,250):
        print("Player one wins the race.")
        break
    elif player_two.pos() >= (300,-250):
        print("Player one wins the race.")
        break

    else:
        die_roll = random.choice(die)
        player_one.forward(30*die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_two.forward(30*die_roll2)
        time.sleep(1)



turtle.done()       # This keeps the turtle drawing on the screen .


