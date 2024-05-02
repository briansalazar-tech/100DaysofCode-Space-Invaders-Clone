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

Text in progress :)
