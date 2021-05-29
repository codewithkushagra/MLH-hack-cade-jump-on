import os
import pygame

PLAYERPOSITIONY =830
EVILPOSITIONY =825
EVILCHARACTER_WIDTH=100
EVILCHARACTER_HEIGHT=100
CHARACTER_WIDTH=80
CHARACTER_HEIGHT=70
WIDTH,HEIGHT =800,900
FPS=60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Jump On")

CHARACTER_IMAGE=pygame.image.load(os.path.join('Assets','player.png'))
CHARACTER=pygame.transform.scale(CHARACTER_IMAGE,(CHARACTER_WIDTH,CHARACTER_HEIGHT))
EVILCHARACTER_IMAGE=pygame.image.load(os.path.join('Assets','evil.png'))
EVILCHARACTER=pygame.transform.scale(EVILCHARACTER_IMAGE,(EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT))


def moveEvilX(evil,motion):
    if evil<700 and motion:
        evil+= 1
    elif evil<0:
        motion=True
    else:
        evil-= 1
        motion=False
    return evil,motion

def moveRight(player):
    if player<700:
        player=player+2
    return player

def moveLeft(player):
    if player>0:
        player=player-2
    return player


def jump(player,injump,count_jump):
        if count_jump<40:
            player-=2
            count_jump+=1
            print("plus",count_jump)
            injump=True
        else:
            count_jump+=1
            print("minus",count_jump)
            player+=2
        if count_jump==80:
            injump=False
            count_jump=0
        return player,injump,count_jump


def draw_window(evil,player):
    WIN.fill((255,255,255))
    WIN.blit(EVILCHARACTER,(evil.x,evil.y))
    WIN.blit(CHARACTER,(player.x,player.y))
    pygame.display.update()



def main():
    evil=pygame.Rect(0,EVILPOSITIONY,EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT)
    player=pygame.Rect(350,PLAYERPOSITIONY,CHARACTER_WIDTH,CHARACTER_HEIGHT)
    clock= pygame.time.Clock()
    count_jump=0
    motion=True
    injump=False
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

        draw_window(evil,player)

        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            player.x=moveRight(player.x)
        elif keys_pressed[pygame.K_LEFT]:
            player.x=moveLeft(player.x)
        evil.x,motion=moveEvilX(evil.x,motion)

        if keys_pressed[pygame.K_UP] or injump:
            player.y,injump,count_jump=jump(player.y,injump,count_jump)    
    pygame.quit()

if __name__ == "__main__":
    main()