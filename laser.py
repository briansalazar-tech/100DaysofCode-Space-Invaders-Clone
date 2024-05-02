from turtle import Turtle
from random import randint

class PlayerLaser(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("triangle")
        self.color("#CC6CE7")
        self.setheading(90)
        self.shapesize(stretch_wid=.20, stretch_len=1)
        self.goto(0, -520)
        self.cannon_pos = (0,-400)
        self.shot_fired = False


    def fire_cannon(self): 
        if self.shot_fired == True: # Ensures laser is not firable while on screen
            pass
        else:
            self.goto(self.cannon_pos)
            self.shot_fired = True


class AlienLaser(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("triangle")
        self.color("white")
        self.setheading(270)
        self.shapesize(stretch_wid=.20, stretch_len=1)
        self.goto(1000, 520) # Spawns off screen
        self.cannon_pos = (0,400)
        self.rand_fire = 0
        self.shot_fired = False
        self.laser_in_play = False
    
    
    def position_laser(self):
        """
        Alien lasers go off screen once a condition is met. Position_laser moves the laser to the cannon's position and fires the laser from that position.
        Position laser is only called when a condition is met to minimize the number of objects on screen.
        """
        self.cannon_pos = self.cannon_pos
        self.goto(self.cannon_pos)


    def fire_cannon(self, cannon_pos):
        """
        Fire_cannon sets the laser's position and fires the laser when randint selects the random number that is specified. 
        Regardless of condition to fire the cannon, a cannon's position is constantly polled and is passed when shot_fired condition is met to make sure the 
        laser fires from the cannon's position.
        """
        self.cannon_pos = cannon_pos
        if self.shot_fired == False:
            
            self.rand_fire = randint(0,1000) # Lower number to make odds of a laser being fired higher increasing difficulty.
            if self.rand_fire == 3:
                self.position_laser()

        if self.rand_fire == 3:  
            self.shot_fired = True # In main, when condition is met, shot_fired is changed back to False


