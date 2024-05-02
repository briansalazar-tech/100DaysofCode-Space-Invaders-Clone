from turtle import Screen
from scoreboard import Floor_Line, Scoreboard, life_spaceships
from player import Cannon, bunkers
from laser import PlayerLaser, AlienLaser
from aliens import spawn_red_alien, row_1, row_2, row_3, row_4, row_5
from random import randint, choice

player_cannon_pos = (0, -400)
aliens_destroyed = 0 # Threshold for when next level is called. Only counts white aliens destroyed
level = 0 # Increases based on aliens destroyed

aliens = [] # Populated with lists composing of white aliens. 
white_alien_starting_y = 300
white_alien_speed = 0.15 # Lower value to make movement slower/game easier or increase to make harder
row1_randlaserpos = (1000, 520)
row2_randlaserpos = (1000, 520)
row3_randlaserpos = (1000, 520)
row4_randlaserpos = (1000, 520)
row5_randlaserpos = (1000, 520)

red_alien_in_play = False
red_rand_spawn = 0


def setup_aliens():
    """Sets up aliens when a new level threshold is met. Starting_y value, level and white_alien_speed values are all increased at end of call increasing dificulty."""
    global aliens, white_alien_starting_y, level, white_alien_speed
    aliens = []
    rand_direction = choice([1, -1])
    r1 = row_1(y_coordinate=white_alien_starting_y, spawn_speed=white_alien_speed) # Top most row
    r2 = row_2(y_coordinate=white_alien_starting_y, spawn_speed=white_alien_speed)
    r3 = row_3(y_coordinate=white_alien_starting_y, spawn_speed=white_alien_speed)
    r4 = row_4(y_coordinate=white_alien_starting_y, spawn_speed=white_alien_speed)
    r5 = row_5(y_coordinate=white_alien_starting_y, spawn_speed=white_alien_speed) # Bottom most row
    aliens.append(r1)
    aliens.append(r2)
    aliens.append(r3)
    aliens.append(r4)
    aliens.append(r5)

    # Randomizes the starting direction when setup_alien is called
    for row in aliens:
        for alien in row:
            alien.x_move *= rand_direction

    white_alien_starting_y -= 50
    level += 1
    white_alien_speed += 0.02
    

def levels():
    """Calls the setup_alien function to start a new wave of aliens."""
    # Level 1
    if aliens_destroyed == 0 and level == 0:
        setup_aliens()
    # Level 2
    if aliens_destroyed == 50 and level == 1:
        setup_aliens()
    # Level 3
    if aliens_destroyed == 100 and level == 2:
        setup_aliens()
    # Level 4
    if aliens_destroyed == 150 and level == 3:
        setup_aliens()
    # Level 5
    if aliens_destroyed == 200 and level == 4:
        setup_aliens()
    # Level 6
    if aliens_destroyed == 250 and level == 5:
        setup_aliens()
    # Level 7
    if aliens_destroyed == 300 and level == 6:
        setup_aliens()
    # Level 8
    if aliens_destroyed == 350 and level == 7:
        setup_aliens()
    # Level 8
    if aliens_destroyed == 400 and level == 8:
        setup_aliens()
    # Level 9 - GG
    if aliens_destroyed == 450 and level == 9:
        setup_aliens()


### GAME SETUP ###
# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=860, height=1000)
screen.title("100 Days of Code: Space Invaders")
screen.tracer(0, 0)
screen.listen()
line = Floor_Line()
lives = life_spaceships()

# Scoreboard Setup
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

# Player & Bunker Setup
player_cannon = Cannon()
player_laser = PlayerLaser()
screen.onkeypress(player_cannon.go_left, key="Left")
screen.onkeypress(player_cannon.go_right, key="Right")
screen.onkeypress(player_laser.fire_cannon, key="space")
# screen.onkeypress(scoreboard.game_over, key="x") ## Use for testing
player_bunkers = bunkers()

# White Alien Lasers
row1_laser = AlienLaser()
row2_laser = AlienLaser()
row3_laser = AlienLaser()
row4_laser = AlienLaser()
row5_laser = AlienLaser()

### GAME PLAY ###
game_on = True
while game_on:
    screen.update()
    levels()
    player_laser.cannon_pos = player_cannon.pos()
    
    ## RED ALIEN SPAWN AND MOVEMENT
    # Red alien - Spawn
    if red_alien_in_play == False:
        red_rand_spawn = randint(0, 600) # Increase or decrease to change chances of red alien spawning

    if red_alien_in_play == False and red_rand_spawn == 50:
        red_alien_in_play = True
        red_alien = spawn_red_alien()
        red_alien_laser = AlienLaser()
    
    # Red alien - Movement
    if red_alien_in_play == True:
        if red_alien.xcor() < -440 or red_alien.xcor() > 440:
            red_alien.x_move *= -1

        # Red alien - Fire cannon
        red_alien.move_x()
        red_alien_laser.fire_cannon(cannon_pos=red_alien.pos())
        
        # Allows only for single shot to be fired
        if red_alien_laser.ycor() <= -520:
            red_alien_laser.goto(1000, 520)
            red_alien_laser.shot_fired = False
        
        # Fires shot from aliens's position
        if red_alien_laser.ycor() > -520 and red_alien_laser.shot_fired == True:
            red_alien_laser.forward(2) # Laser movement speed
    
    # Red Alien Laser Hits player - Player loses life, laser reset
    if red_alien_in_play == True and red_alien_laser.distance(player_cannon) < 25:
        player_cannon.reset_cannon()
        if lives != []:
            lives[-1].backward(1000)
            lives.pop()
        scoreboard.life_lost()
        red_alien_laser.goto(red_alien.pos())
    
    ## WHITE ALIEN MOVEMENT & CANNON FIRE
    # White alien - Movement
    for row in aliens:
        for alien in row:
            if alien.xcor() < -400 or alien.xcor() > 400:
                alien.x_move *= -1 # Reverses direction when wall is hit
                alien.move_y() # Shifts alien closer to player

            alien.move_x() # Move left to right

    # White Alien - Fire Cannon - Row 1
    if aliens[0] != []:
        r1rand = choice(aliens[0]) # Selects a random alien from the list
        row1_randlaserpos = r1rand.pos() # Gets the position of the selected alien
        row1_laser.fire_cannon(cannon_pos=row1_randlaserpos) # Rows laser goes to position of selected alien
        
        # Allows only for single shot to be fired
        if row1_laser.ycor() <= -520:
            row1_laser.goto(1000, 520)
            row1_laser.shot_fired = False
        
        # Fires shot from cannon's position
        if row1_laser.ycor() > -520 and row1_laser.shot_fired == True:
            row1_laser.forward(2)
    
    # White Alien - Fire Cannon - Row 2
    if aliens[1] != []:
        r2rand = choice(aliens[0])
        row2_randlaserpos = r2rand.pos()
        row2_laser.fire_cannon(cannon_pos=row2_randlaserpos)
        
        # Allows only for single shot to be fired
        if row2_laser.ycor() <= -520:
            row2_laser.goto(1000, 520)
            row2_laser.shot_fired = False
        
        # Fires shot from cannon's position
        if row2_laser.ycor() > -520 and row2_laser.shot_fired == True:
            row2_laser.forward(2)
    
    # White Alien - Fire Cannon - Row 3
    if aliens[2] != []:
        r3rand = choice(aliens[0])
        row3_randlaserpos = r3rand.pos()
        row3_laser.fire_cannon(cannon_pos=row3_randlaserpos)
        
        # Allows only for single shot to be fired
        if row3_laser.ycor() <= -520:
            row3_laser.goto(1000, 520)
            row3_laser.shot_fired = False
        
        # Fires shot from cannon's position
        if row3_laser.ycor() > -520 and row3_laser.shot_fired == True:
            row3_laser.forward(2)

    # White Alien - Fire Cannon - Row 4
    if aliens[3] != []:
        r4rand = choice(aliens[0])
        row4_randlaserpos = r4rand.pos()
        row4_laser.fire_cannon(cannon_pos=row4_randlaserpos)
        
        # Allows only for single shot to be fired
        if row4_laser.ycor() <= -520:
            row4_laser.goto(1000, 520)
            row4_laser.shot_fired = False
        
        # Fires shot from cannon's position
        if row4_laser.ycor() > -520 and row4_laser.shot_fired == True:
            row4_laser.forward(2)
    
    # White Alien - Fire Cannon - Row 5
    if aliens[4] != []:
        r5rand = choice(aliens[0])
        row5_randlaserpos = r5rand.pos()
        row5_laser.fire_cannon(cannon_pos=row5_randlaserpos)
        
        # Allows only for single shot to be fired
        if row5_laser.ycor() <= -520:
            row5_laser.goto(1000, 520)
            row5_laser.shot_fired = False
        
        # Fires shot from cannon's position
        if row5_laser.ycor() > -520 and row5_laser.shot_fired == True:
            row5_laser.forward(2)
    
    # White Alien - Remove laser from screen if alien list is blank
    if aliens[0] == []:
        row1_laser.goto(1000, 520)
        row1_laser.shot_fired = False
    if aliens[1] == []:
        row2_laser.goto(1000, 520)
        row2_laser.shot_fired = False
    if aliens[2] == []:
        row3_laser.goto(1000, 520)
        row3_laser.shot_fired = False
    if aliens[3] == []:
        row4_laser.goto(1000, 520)
        row4_laser.shot_fired = False
    if aliens[4] == []:
        row5_laser.goto(1000, 520)
        row5_laser.shot_fired = False

    # White Alien - Laser Hits Player - Reset All allien lasers and subtract life
    if row1_laser.distance(player_cannon) < 25 or row2_laser.distance(player_cannon) < 25 or row3_laser.distance(player_cannon) < 25 or row4_laser.distance(player_cannon) < 25 or row5_laser.distance(player_cannon) < 25:
        player_cannon.reset_cannon()
        if lives != []:
            lives[-1].backward(1000)
            lives.pop()
        scoreboard.life_lost()
        row1_laser.goto(1000, 520)
        row1_laser.shot_fired = False
        row2_laser.goto(1000, 520)
        row2_laser.shot_fired = False
        row3_laser.goto(1000, 520)
        row3_laser.shot_fired = False
        row4_laser.goto(1000, 520)
        row4_laser.shot_fired = False
        row5_laser.goto(1000, 520)
        row5_laser.shot_fired = False
    
    ## GAME OVER
    # Alien crosses floor line or hits player
    for row in aliens:
        for alien in row:
            if alien.ycor() <= -430 or alien.distance(player_cannon) < 25:
                game_on = False
                scoreboard.game_over()
    
    # Player has no lives
    if scoreboard.lives == 0:
        game_on = False
        scoreboard.game_over()

    ## BUNKER IS HIT
    for bunker in player_bunkers:
        # Alien hits bunker
        for row in aliens:
            for alien in row:
                if alien.distance(bunker) < 50:
                    bunker.bunker_hit()
        
        # Red Alien laser hits bunker
        if red_alien_in_play == True and red_alien_laser.distance(bunker) < 50:
            red_alien_laser.goto(1000, 520)
            red_alien_laser.shot_fired = False
            bunker.bunker_hit()

        # White Alien laser hits bunker
        if row1_laser.distance(bunker) < 50:
            row1_laser.goto(1000, 520)
            row1_laser.shot_fired = False
            bunker.bunker_hit()
        if row2_laser.distance(bunker) < 50:
            row2_laser.goto(1000, 520)
            row2_laser.shot_fired = False
            bunker.bunker_hit()
        if row3_laser.distance(bunker) < 50:
            row3_laser.goto(1000, 520)
            row3_laser.shot_fired = False
            bunker.bunker_hit()
        if row4_laser.distance(bunker) < 50:
            row4_laser.goto(1000, 520)
            row4_laser.shot_fired = False
            bunker.bunker_hit()
        if row5_laser.distance(bunker) < 50:
            row5_laser.goto(1000, 520)
            row5_laser.shot_fired = False
            bunker.bunker_hit()

        # Player Laser hits bunker
        if player_laser.distance(bunker) < 50:
            player_laser.goto(0, -520)
            player_laser.shot_fired = False
            bunker.bunker_hit()

    ## Player - Destroy red alien
    if red_alien_in_play == True and player_laser.distance(red_alien) < 25:
        red_alien.goto(1000,1000)
        red_alien_laser.goto(1000,1000)
        scoreboard.add_points(alien_shape= red_alien.shape() ,alien_color=red_alien.color())
        player_laser.goto(0, -520)
        player_laser.shot_fired = False
        red_alien_in_play = False

    ## Player - Destroy white alien
    for row in aliens:
        for alien in row:
            if player_laser.distance(alien) < 25:

                alien.goto(1000,1000)
                row.remove(alien)
                aliens_destroyed += 1 
                scoreboard.add_points(alien_shape= alien.shape() ,alien_color=alien.color())
                player_laser.goto(0, -520)
                player_laser.shot_fired = False
    
    ## Player - Allows only for single shot to be fired
    if player_laser.ycor() >= 520:
        player_laser.goto(0, -520)
        player_laser.shot_fired = False
    
    ## Player - Fires shot from cannon's position
    if player_laser.ycor() < 520 and player_laser.shot_fired == True:
        player_laser.forward(10)

screen.exitonclick()