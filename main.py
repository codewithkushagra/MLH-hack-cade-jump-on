import os
import pygame
COIN_SCORE=0
FLOOR=1
PLAYERPOSITIONY =637
EVILPOSITIONY =624
SCORE=0
GAMEOVER=False
COIN_WIDTH,COIN_HEIGHT = 30,30
EVILCHARACTER_WIDTH=100
EVILCHARACTER_HEIGHT=100
CHARACTER_WIDTH=69
CHARACTER_HEIGHT=60
WIDTH,HEIGHT =800,700
BRICK_HEIGHT=20
FPS=60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Jump On")
run=True
CHARACTER_IMAGE=pygame.image.load(os.path.join('Assets','player.png'))
CHARACTER=pygame.transform.scale(CHARACTER_IMAGE,(CHARACTER_WIDTH,CHARACTER_HEIGHT))
EVILCHARACTER_IMAGE=pygame.image.load(os.path.join('Assets','evil.png'))
EVILCHARACTER=pygame.transform.scale(EVILCHARACTER_IMAGE,(EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT))
COIN_IMAGE=pygame.image.load(os.path.join('Assets','coin.png'))
COIN=pygame.transform.scale(COIN_IMAGE,(COIN_WIDTH,COIN_HEIGHT))
BACKGROUND=pygame.image.load(os.path.join('Assets','background.png'))
BRICK_IMAGE=pygame.image.load(os.path.join('Assets','brick.png'))
BRICK=pygame.transform.scale(BRICK_IMAGE,(WIDTH,BRICK_HEIGHT))
BRICKBLOCK_IMAGE=pygame.image.load(os.path.join('Assets','brick-block.png'))
BRICKBLOCK=pygame.transform.scale(BRICKBLOCK_IMAGE,(int(WIDTH/2),80))
TREASURE_IMAGE=pygame.image.load(os.path.join('Assets','treasure.png'))
TREASURE=pygame.transform.scale(TREASURE_IMAGE,(250,150))   

# SCORE_TEXT=pygame.font.FONT

class Evil:

    def __init__(self,motion=True,x=None,y=None,image=0,floor=None):
        self.x=x
        self.y=y
        self.image=image
        self.floor=floor
        self.motion=motion

class Coin:

    def __init__(self,x,y,collected,image):
        self.x=x
        self.y=y
        self.collected=collected
        self.image=image


def moveEvilX(evil,motion):


    if evil.x<700 and motion:
        evil.x+= 2
    elif evil.x<380 and evil.floor==4:
        evil.image=pygame.transform.flip(evil.image,True,False)
        motion=True
    elif evil.x<0:
        evil.image=pygame.transform.flip(evil.image,True,False)
        motion=True
    else:
        if evil.x==700:
            evil.image=pygame.transform.flip(evil.image,True,False)
        evil.x-= 2
        motion=False
    return evil,motion

def moveRight(player):
    if player.y==477:
        if player.x<340:
            player.x=player.x+2
    else:
        if player.x<700:
            player.x=player.x+2
    return player.x

def moveLeft(player):
    if player.x>0:
        player.x=player.x-2
    return player.x


def jump(player,injump,count_jump):
        if count_jump<23:
            player-=4
            count_jump+=1
            injump=True
        else:
            count_jump+=1
            player+=4
        if count_jump==46:
            injump=False
            count_jump=0
        return player,injump,count_jump


def updatePosition(player,PLAYERPOSITIONY,injump,count_jump):
    if player==PLAYERPOSITIONY-(4*20) and count_jump>23:
        PLAYERPOSITIONY=PLAYERPOSITIONY-(4*20)
        global SCORE
        SCORE+=10
        global FLOOR
        FLOOR+=1
        return PLAYERPOSITIONY,PLAYERPOSITIONY,False,0
    else:
        return player,PLAYERPOSITIONY,injump,count_jump

def checkCoin(coinList,player):
        xlim=[]
        for i in range(player.x+5,player.x+30):
            xlim.append(i)
        for coin in coinList:
            if coin.x in xlim and coin.y ==player.y:
                coin.collected=True
                coin.image=None
                global COIN_SCORE
                COIN_SCORE+=1
    
def checkGame(evillist,player):
    if FLOOR<7:
        evil=evillist[FLOOR-1]
        if evil.x!=None:
            if((evil.x-50==player.x or evil.x+50==player.x or evil.x-51==player.x or evil.x+51==player.x or evil.x-52==player.x or evil.x+52==player.x) and (evil.y+13==player.y or evil.y+14==player.y or evil.y+12==player.y or evil.y+15==player.y or evil.y+11==player.y)):
                global GAMEOVER
                GAMEOVER =True
    return
                

def drawWindow(evillist,player,coinList):             #coins at 492
    if not GAMEOVER:
        WIN.blit(BACKGROUND,(-80,0))
        l=692
        for i in range(7):
            if(i==3):
                WIN.blit(BRICKBLOCK,(WIDTH/2,l))
            else:
                WIN.blit(BRICK,(0,l))
            l-=80
        for coin in coinList:
            if not coin.collected:
                WIN.blit(coin.image,(coin.x,coin.y))
        WIN.blit(TREASURE,(-60,110))
        for i in range(6):
            if i != 2:
                x=evillist[i].x
                y=evillist[i].y
                WIN.blit(evillist[i].image,(x,y))
        
        WIN.blit(CHARACTER,(player.x,player.y))
    else:
        global run
        WIN.fill((225,225,219))
        pygame.display.update()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                    
    pygame.display.update()



def main(PLAYERPOSITIONY):
#    listevil=[pygame.Rect(0,EVILPOSITIONY,EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT),pygame.Rect(40,EVILPOSITIONY+80,EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT)]
    evillist=[]
    for i in range(6):
        if i != 2:
            evil=Evil(True,100*i,EVILPOSITIONY-(i*80),EVILCHARACTER,i+1)
            evillist.append(evil)
        else:
            evil=Evil()
            evillist.append(evil)
    coinList=[]
    for i in range(1,6):
        coin=Coin(i*60,401,False,COIN)
        coinList.append(coin)
##    evil=pygame.Rect(0,EVILPOSITIONY,EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT)
    player=pygame.Rect(350,PLAYERPOSITIONY,CHARACTER_WIDTH,CHARACTER_HEIGHT)
    clock= pygame.time.Clock()
    count_jump=0
    injump=False
    infall=False
    global run
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        checkGame(evillist,player)
        drawWindow(evillist,player,coinList)
        if FLOOR==3 or FLOOR==4:
            checkCoin(coinList,player)
        keys_pressed=pygame.key.get_pressed()
        
        

        if player.y>=80:
            if player.y==397 and player.x<340:
                pass
            elif player.y==397 and player.x>340:    
                player.y,PLAYERPOSITIONY,injump,count_jump=updatePosition(player.y,PLAYERPOSITIONY,injump,count_jump)
            else:
                player.y,PLAYERPOSITIONY,injump,count_jump=updatePosition(player.y,PLAYERPOSITIONY,injump,count_jump)
                

        if keys_pressed[pygame.K_RIGHT]:
            player.x=moveRight(player)
        elif keys_pressed[pygame.K_LEFT]:
            player.x=moveLeft(player)

        if (player.y==557 and player.x<340) or player.y!=557:
            if (keys_pressed[pygame.K_UP] or injump):
                player.y,injump,count_jump=jump(player.y,injump,count_jump)
            
        i=0
        for evil in evillist:
            if i!=2:
                evil,evil.motion=moveEvilX(evil,evil.motion)
            i+=1
    pygame.quit()

if __name__ == "__main__":
    main(PLAYERPOSITIONY)
