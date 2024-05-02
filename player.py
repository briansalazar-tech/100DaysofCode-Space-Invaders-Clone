from turtle import Turtle

# From Left to Right (8HP to 1HP)
BUNKER_HEALTH = ["#00AAFF", "#10B000", "#17FF00", "#63FF54", "#91FE86", "#B0FDA8", "#CDFFC8", "#E7E7E7", "black"]

class Cannon(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("#29ff07")
        self.setheading(90)
        self.shapesize(stretch_len=1, stretch_wid=2, outline=0)
        self.goto(0, -400)


    def go_left(self):
        if self.xcor() > -410:
            new_x = self.xcor() - 10
            self.goto(new_x, self.ycor())


    def go_right(self):
        if self.xcor() < 400:
                new_x = self.xcor() + 10
                self.goto(new_x, self.ycor())


    def reset_cannon(self):
        self.goto(0, -400)
        

class Bunker(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.color_index = 0 # Value increases when hp value goes down
        self.color(BUNKER_HEALTH[self.color_index])
        self.hp = 8
        self.shapesize(stretch_len=3, stretch_wid=4, outline=4)

    
    def bunker_hit(self):
        """Bunker is hit. HP subtracts 1 while color_index value increases by 1. The new color index is passed to set the updated bunker color depicting the bunker has been damaged."""
        if self.hp == 1: # Moves bunker off screen after 8th hit
            self.backward(1000)

        if self.hp > 0:
            self.hp -= 1
            self.color_index += 1
            self.color(BUNKER_HEALTH[self.color_index])


def bunkers():
    """Creates and returns a list composing of four bunkers."""
    starting_x = -280
    bunkers = []

    for bunker in range(4):
        bunker = Bunker()
        bunkers.append(bunker)

    for bunker in bunkers:
        bunker.goto(starting_x, -300)
        starting_x += 185 # Spacing for bunkers
    
    return bunkers