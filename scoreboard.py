from turtle import Turtle

class Floor_Line(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#29ff07")
        self.penup()
        self.goto(-600, -425)
        self.pendown()
        self.goto(600, -425)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.score = 0
        self.high_score = 0
        self.highscore()


    def update_highscore(self):
        """Checks to see if the current score is higher than the high score. If score is higher, txt file and attribute are updated."""
        if self.score > self.high_score:
            with open("./highscore.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
            self.highscore()


    def highscore(self):
        """Opens the highscore.txt file when the program is launched and sets high_score attribute."""
        with open("./highscore.txt") as file:
            highscore = file.read()
            self.high_score = int(highscore)
            self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the text that is dispalyed in the GUI interface."""
        self.clear()
        self.goto(0, 450)
        self.write(f"Score: {self.score}\t\tHigh-Score: {self.high_score}", align="center", font=("Courier",20, "bold"))
        self.goto(-370, -490)
        self.write(f"Lives\n  {self.lives}", align="center", font=("Courier",20, "bold"))
        self.goto(135, -480)
        self.write("100 Days of Code: Space Invaders", align="center", font=("Courier",20, "bold"))


    def add_points(self, alien_shape, alien_color):
        """Point values for when an alien is destroyed. Score attribute is updated and screen text is refreshed."""
        points = 0
        
        if alien_shape == "turtle" and alien_color == ('red', 'red'):
            points = 100
        
        if alien_shape == "triangle" and alien_color == ('white', 'white'):
            points = 30

        if alien_shape == "circle" and alien_color == ('white', 'white'):
            points = 20

        if alien_shape == "turtle" and alien_color == ('white', 'white'):
            points = 10
        
        self.score += points
        self.update_scoreboard()
        self.update_highscore()


    def game_over(self):
        """Try again"""
        self.lives = 0
        self.update_scoreboard()
        self.goto(0,0)
        self.pencolor("red")
        self.write("Game Over", align="center", font=("Courier", 50, "bold"))


    def life_lost(self):
        """Live value is reduced by one when condition is met while lives are > 0. Screen text is refreshed after update."""
        if self.lives != 0:
            self.lives -= 1
            self.update_scoreboard()


# Onscreen Live Object
class Player_Ships(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#29ff07")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=1, stretch_wid=2, outline=0)


def life_spaceships():
    """Populates the spaceship objects that represent the players remaining lives on screen."""
    starting_x = -295
    spaceships = []

    for ship in range(2):
        ship = Player_Ships()
        spaceships.append(ship)

    for ship in spaceships:
        ship.goto(starting_x, -470)
        starting_x += 80

    return spaceships