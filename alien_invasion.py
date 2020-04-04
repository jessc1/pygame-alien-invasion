import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

     # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    instruction_button = Button(ai_settings, screen, "Instructions")

    #Create an instance to store game stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    #make a alien
    aliens = Group()

    #create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, instruction_button, ship, aliens, bullets)
                     
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, instruction_button, play_button)
        
run_game()



"""import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize game and create a scream object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #SET COLOR
    bg_color = (230, 230, 230)
    
    #Make a ship.
    ship = Ship(ai_settings, screen)
    #makek a group to store bullets
    bullets = Group()
     
    #set the background color.
    #bg_color = (128, 128, 128)
    #start the ma in loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
       

        #Get rid of bullets that have disappeared.
        #for bullet in bullets.copy():
         #   if bullet.rect.bottom <= 0:
          #      bullets.remove(bullet)
           # print(len(bullets))
run_game()"""

 
        

