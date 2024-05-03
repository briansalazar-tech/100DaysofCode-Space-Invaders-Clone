# 100DaysofCode-Space-Invaders-Clone
Day 95 of the 100 Days of Code course. Day 95's goal was to create a clone of the Space Invaders video game.

The program is split up into to five different files. If you want to see some screenshots of the program, there are a few saved under the screenshots folder.
- Aliens.py
- Laser.py
- Main.py
- Player.py
- Scoreboard.py
- Highscore.txt

The aliens.py file contains the alien class which is used to create an alien object as well as control the aliens movement. Additionally, the file has a function to spawn a red alien which has different behavior from the standard white aliens as well as functions that create five rows of 10 aliens. Those rows are managed by populating five separate lists which are then passed into a master list in main.py.

Laser.py has two separate classes for the Laser object. One for the player, and a separate one for the aliens laser. This probably could have been condensed down to a single class since both of the laser classes perform the same functionality but I chose to create one for the player and aliens. Additionally, the Alien class has an additional method to position the laser at an aliens position inside of the class. This method is used by the white aliens. I also chose to assign one laser to each row of aliens (five total) so that the laser would be fired from an alien inside of a row for each row.

The player.py file contains the Cannon class which is controlled by the player. The cannon class has methods to control its movement and reset it to its starting position if it is hit by an alien. Additionally, the file contains the Bunker class which is used to create the player’s bunkers. The class tracks the bunker’s health and when a bunker is hit, its color changes to signify that it has been damaged! Four total bunkers are generated and populated into a list using a function. The main reason I chose to go with four large bunker objects instead of bunkers composed of smaller bricks, is that the game would move very slowly if I were to compose the bunkers of multiple small bricks. 

Scoreboard.py is responsible for making the screen look pretty as well as keeping track of the score, high score, and player's lives. If the player’s current score is higher than the high score, then the high score file is overwritten. The high score is tracked and saved in highscore.txt and is opened when the game is launched.

Tying everything together is main.py. Main contains the variables and functions used to set up the game. The setup_aliens function creates a level and increases the difficulty every time it is called, and levels calls setup_aliens every time a level is cleared. All the objects are called from the various files that make up the game and are rendered on screen. Additionally, main contains the logic that makes the game function. This logic includes setting up the aliens on screen, moving them, firing lasers, and all the fun of the game. Once a player has zero lives the game ends otherwise, nine rounds of aliens spawn and continue until the game is over.

