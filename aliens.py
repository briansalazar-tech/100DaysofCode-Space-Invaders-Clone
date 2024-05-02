from turtle import Turtle
from random import choice

class Alien(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(270)
        self.shapesize(stretch_len=1, stretch_wid=2, outline=0)
        self.color("white")
        self.y_move = -40 # Shifts alien twards floor when wall is hit
        self.x_move = 0.50 # Movement speed for red alien

    def move_x(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())
    

    def move_y(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)


def spawn_red_alien():
    """The red alien does not exist in a row list. spawn red alien is called at random and only moves left to right at a consistant speed."""
    starting_x = choice([-430, 430])
    starting_y = 300
    alien = Alien()
    alien.shape("turtle")
    alien.color("red")
    alien.goto(starting_x,starting_y)

    return alien


def row_1(y_coordinate, spawn_speed):
    """Creates the first row of aliens that are populated on screen. Aliens are added to the row1 list. y_coordinate and spawn_speed are passed from main.py and is modified each time a level is complete to make the following level harder."""
    starting_x = -360
    starting_y = y_coordinate - 40
    row1 = []

    for alien in range(10):
        alien = Alien()
        alien.x_move = spawn_speed
        alien.shape("triangle")
        row1.append(alien)

    for alien in row1:
        alien.goto(starting_x, starting_y)
        starting_x += 80

    return row1


def row_2(y_coordinate, spawn_speed):
    """Creates the second row of aliens that are populated on screen. Aliens are added to the row2 list. y_coordinate and spawn_speed are passed from main.py and is modified each time a level is complete to make the following level harder."""
    starting_x = -360
    starting_y = y_coordinate - 80
    row2 = []
    
    for alien in range(10):
        alien = Alien()
        alien.x_move = spawn_speed
        alien.shape("circle")
        row2.append(alien)

    for alien in row2:
        alien.goto(starting_x, starting_y)
        starting_x += 80

    return row2


def row_3(y_coordinate, spawn_speed):
    """Creates the third row of aliens that are populated on screen. Aliens are added to the row3 list. y_coordinate and spawn_speed are passed from main.py and is modified each time a level is complete to make the following level harder."""
    starting_x = -360
    starting_y = y_coordinate - 120
    row3 = []
    
    for alien in range(10):
        alien = Alien()
        alien.x_move = spawn_speed
        alien.shape("circle")
        row3.append(alien)

    for alien in row3:
        alien.goto(starting_x, starting_y)
        starting_x += 80

    return row3


def row_4(y_coordinate, spawn_speed):
    """Creates the forth row of aliens that are populated on screen. Aliens are added to the row4 list. y_coordinate and spawn_speed are passed from main.py and is modified each time a level is complete to make the following level harder."""
    starting_x = -360
    starting_y = y_coordinate - 160
    row4 = []
    
    for alien in range(10):
        alien = Alien()
        alien.x_move = spawn_speed
        alien.shape("turtle")
        row4.append(alien)

    for alien in row4:
        alien.goto(starting_x, starting_y)
        starting_x += 80

    return row4


def row_5(y_coordinate, spawn_speed):
    """Creates the fith row of aliens that are populated on screen. Aliens are added to the row5 list. y_coordinate and spawn_speed are passed from main.py and is modified each time a level is complete to make the following level harder."""
    starting_x = -360
    starting_y = y_coordinate - 200
    row5 = []
    
    for alien in range(10):
        alien = Alien()
        alien.x_move = spawn_speed
        alien.shape("turtle")
        row5.append(alien)

    for alien in row5:
        alien.goto(starting_x, starting_y)
        starting_x += 80

    return row5
