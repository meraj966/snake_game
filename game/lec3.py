import pygame
pygame.init()  # this line will initialize the pgame module
gameWindow = pygame.display.set_mode((1200,500))  # syntax to create the display of the game window
pygame.display.set_caption("My First Game") # syntax to set the caption on the game display

#Game specific variable
exit_game=False
game_over=False

#Create game loop
while not exit_game:
    for event in pygame.event.get():#All event which we will do in our game
        if event.type==pygame.QUIT: # this if condition to close our running game on window
            exit_game=True

        if event.type == pygame.KEYDOWN: #this if condition is to know which key get pressed
            if event.key == pygame.K_RIGHT:
                print("you have pressed right arrow key")


pygame.quit() #to quit game
quit() # to quit program