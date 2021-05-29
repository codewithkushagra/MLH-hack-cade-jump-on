import os
import pygame


PLAYERPOSITIONY =630
EVILPOSITIONY =625
SCORE=0
GAMEOVER=False
COIN_WIDTH,COIN_HEIGHT = 30,30
EVILCHARACTER_WIDTH=100
EVILCHARACTER_HEIGHT=100
CHARACTER_WIDTH=80
CHARACTER_HEIGHT=70
WIDTH,HEIGHT =800,700
FPS=60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Jump On")

CHARACTER_IMAGE=pygame.image.load(os.path.join('Assets','player.png'))
CHARACTER=pygame.transform.scale(CHARACTER_IMAGE,(CHARACTER_WIDTH,CHARACTER_HEIGHT))
EVILCHARACTER_IMAGE=pygame.image.load(os.path.join('Assets','evil.png'))
EVILCHARACTER=pygame.transform.scale(EVILCHARACTER_IMAGE,(EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT))
COIN_IMAGE=pygame.image.load(os.path.join('Assets','coin.png'))
COIN=pygame.transform.scale(COIN_IMAGE,(COIN_WIDTH,COIN_HEIGHT))
# SCORE_TEXT=pygame.font.FONT

def moveEvilX(evil,motion):
    global EVILCHARACTER
    if evil<700 and motion:
        evil+= 1
    elif evil<0:
        EVILCHARACTER=pygame.transform.flip(EVILCHARACTER,True,False)
        motion=True
    else:
        if evil==700:
            EVILCHARACTER=pygame.transform.flip(EVILCHARACTER,True,False)
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
        if count_jump<30:
            player-=4
            count_jump+=1
            injump=True
        else:
            count_jump+=1
            player+=4
        if count_jump==60:
            injump=False
            count_jump=0
        return player,injump,count_jump


def updatePosition(player,PLAYERPOSITIONY,injump,count_jump):
    if player==PLAYERPOSITIONY-(4*20) and count_jump>30:
        PLAYERPOSITIONY=PLAYERPOSITIONY-(4*20)
        global SCORE
        SCORE+=10
        return PLAYERPOSITIONY,PLAYERPOSITIONY,False,0
    else:
        return player,PLAYERPOSITIONY,injump,count_jump


def checkGame(evil,player):
    if((evil.x-62==player.x or evil.x+62==player.x) and evil.y+5==player.y):
        global GAMEOVER
        GAMEOVER =True


def drawWindow(evil,player):
    if not GAMEOVER:
        WIN.fill((255,255,255))
        WIN.blit(COIN,(0,0))
        WIN.blit(EVILCHARACTER,(evil.x,evil.y))
        WIN.blit(CHARACTER,(player.x,player.y))
    else:
        WIN.fill((255,255,100))
    pygame.display.update()



def main(PLAYERPOSITIONY):
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
        checkGame(evil,player)
        drawWindow(evil,player)
        print(SCORE)
        keys_pressed=pygame.key.get_pressed()
        
        

        player.y,PLAYERPOSITIONY,injump,count_jump=updatePosition(player.y,PLAYERPOSITIONY,injump,count_jump)

        if keys_pressed[pygame.K_RIGHT]:
            player.x=moveRight(player.x)
        elif keys_pressed[pygame.K_LEFT]:
            player.x=moveLeft(player.x)

        if keys_pressed[pygame.K_UP] or injump:
            player.y,injump,count_jump=jump(player.y,injump,count_jump)

        evil.x,motion=moveEvilX(evil.x,motion)

    pygame.quit()

if __name__ == "__main__":
    main(PLAYERPOSITIONY)