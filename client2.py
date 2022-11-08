import pygame
import os
from network import Network
from player import Player

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
MAX_BULLETS = 3
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
SPACE = pygame.transform.scale(pygame.image.load(
        os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

def main():  
    clock = pygame.time.Clock()
    run = True
    n=Network()
    startPos=n.getPos()
    player1=Player(SPACESHIP_WIDTH,SPACESHIP_HEIGHT,'spaceship_yellow.png',90,10,[],1)
    player1.red =pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    player2=Player(SPACESHIP_WIDTH,SPACESHIP_HEIGHT,'spaceship_red.png',270,10,[],2)
    player2.red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(player1.bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        player1.red.x + player1.red.width, player1.red.y + player1.red.height//2 - 2, 10, 5)
                    player1.bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(player2.bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        player2.red.x, player2.red.y + player2.red.height//2 - 2, 10, 5)
                    player2.bullets.append(bullet)
                

            if event.type == player1.HIT:
                player2.health -= 1
                #BULLET_HIT_SOUND.play()
            if event.type == player2.HIT:
                player1.health -= 1

        winner_text = ""
        if player1.health <= 0:
            winner_text = "Player 2 Wins!"

        if player2.health <= 0:
            winner_text = "Player 1 Wins!"
        

        if winner_text != "":
            Player.draw_window(SPACE,WIN,player1,player2)
            Player.draw_winner(WIN,winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        player1.handle_bullets(player2)
        player1.handle_movement_adws(keys_pressed)
        player2.handle_movement_arrow(keys_pressed)
        Player.draw_window(SPACE,WIN,player1,player2)

main()