import pygame
import random
import os
pygame.mixer.init() # to add music in game

pygame.init()


#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)


#create window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#Background image
bgimg=pygame.image.load("img.jpeg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

#game title
pygame.display.set_caption("Snake with MAAZ")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((233, 210, 229))
        text_screen("Welcome to MAAZ creation",black,230,250)
        text_screen("Press space bar to Play", black, 240, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(30)


#Create game loop
def gameloop():
    # Game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0, screen_width / 2)  # generate random food with in console or window
    food_y = random.randint(0, screen_width / 2)
    score = 0

    fps = 30  # fps means frame per second.. fps is use to define how many times we need the frame...and the things which are written inside the while block are nothing but frame

    clock = pygame.time.Clock()  # synatax to define clock .. due to the clock only our snake will move in x and y axis#
    snk_list = []
    snk_length = 1
    # cheack if highscore file exists
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    font = pygame.font.SysFont(None, 55)  # syntax to declear the font on the game screen
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            text_screen("Game Over ! Press Enter to continue" , red , 80 , 250)
            text_screen("Thank You from :-MAAZ", red, 80, 300)

            for event in pygame.event.get():#All event which we will do in our game
                if event.type==pygame.QUIT: # this if condition to close our running game on window
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():#All event which we will do in our game
                if event.type==pygame.QUIT: # this if condition to close our running game on window
                    exit_game=True

                if event.type == pygame.KEYDOWN: #this if condition is to know which key get pressed
                    if event.key == pygame.K_RIGHT:
                        velocity_x=4
                        velocity_y=0

                    if event.key == pygame.K_LEFT:
                        velocity_x=-4
                        velocity_y=0

                    if event.key == pygame.K_UP:
                        velocity_y=-4
                        velocity_x=0

                    if event.key == pygame.K_DOWN:
                        velocity_y=4
                        velocity_x=0

                    if event.key == pygame.K_q: # this if condituon is use to cheat ... if we will press "q" while playing game we can increase our score with cheation

                        score+=10

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                #print("score:-",score*10)
                food_x = random.randint(0, screen_width / 2)
                food_y = random.randint(0, screen_width / 2)
                snk_length+=4
                if score>int(highscore):
                    highscore = score

            gameWindow.fill(white) # to fill the color of window
            gameWindow.blit(bgimg, (0,0))
            text_screen("score:-" + str(score) + "  HighScore:"+str(highscore), (240,240,150), 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
            #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size]) # synatx to draw snake's head on the screen
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

if __name__ == "__main__":
    welcome()
