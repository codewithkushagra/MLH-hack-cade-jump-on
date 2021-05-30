import os
import pygame
from pygame.constants import K_UP

pygame.font.init()


NAV=200
COIN_SCORE=0
GAMESTATUS="Playing"
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
BRICKBLOCKLVL1=pygame.transform.scale(BRICKBLOCK_IMAGE,(int(WIDTH/2),80))
BRICKBLOCKLVL2=pygame.transform.scale(BRICKBLOCK_IMAGE,(int(WIDTH/3),80))
TREASURE_IMAGE=pygame.image.load(os.path.join('Assets','treasure.png'))
TREASURE=pygame.transform.scale(TREASURE_IMAGE,(250,150))
BLUE=(255,255,255)
FONT = pygame.font.SysFont(pygame.font.get_default_font(), 40)
MENUFONT = pygame.font.SysFont(pygame.font.get_default_font(), 80)

def LEVEL(level,PLAYERPOSITIONY):

    if level==1:
        # SCORE_TEXT=pygame.font.FONT




        def LEVEL2(PLAYERPOSITIONY):
            
    ##---------------------------------------------------LEVEL 2-------------------------------------------------
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



            def getByFloor(evillist,floor):
                    evilOnfloor=[]
                    for evil in evillist:
                        if evil.floor==floor:
                            evilOnfloor.append(evil)
                    return evilOnfloor


            def moveEvilX(evil,motion):
                if evil.floor!=7:
                    if evil.x<730 and motion:
                        evil.x+= 2
                    elif evil.x<-20:
                        evil.image=pygame.transform.flip(evil.image,True,False)
                        motion=True
                    else:
                        if evil.x==730:
                            evil.image=pygame.transform.flip(evil.image,True,False)
                        evil.x-= 2
                        motion=False
                else:
                    if evil.x<480 and motion:
                        evil.x+=2
                    elif evil.x<-20:
                        evil.image=pygame.transform.flip(evil.image,True,False)
                        motion=True
                    else:
                        if evil.x==480:
                            evil.image=pygame.transform.flip(evil.image,True,False)
                        evil.x-= 2
                        motion=False
                return evil,motion

            def moveRight(player):
                if player.y==157:
                    if player.x<480:
                        player.x=player.x+2
                else:
                    if player.x<740:
                        player.x=player.x+2
                return player.x

            def moveLeft(player):
                if player.x>-10:
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
                        if coin.x in xlim and coin.y ==player.y+13:
                            coin.image=None
                            if not coin.collected:
                                global COIN_SCORE
                                COIN_SCORE+=1
                            coin.collected=True
                
            def checkGame(evillist,player,coinList):
                global GAMEOVER
                global GAMESTATUS
                if FLOOR<8:
                    evilOnfloor=getByFloor(evillist,FLOOR)
                    for evil in evilOnfloor:
                        if evil.x!=None:
                            if((evil.x-50==player.x or evil.x+50==player.x or evil.x-51==player.x or evil.x+51==player.x or evil.x-52==player.x or evil.x+52==player.x) and (evil.y+13==player.y or evil.y+14==player.y or evil.y+12==player.y or evil.y+15==player.y or evil.y+11==player.y)):
                                GAMEOVER =True
                                GAMESTATUS="You Lost"
                                drawWindow(evillist,player,coinList)
                elif FLOOR==8:
                    if player.x==670:
                        GAMESTATUS="You Won"
                        GAMEOVER =True
                return
                            


            def startGame(PLAYERPOSITIONY):
                global FLOOR
                global SCORE
                evillist=[]  #(motion, x, y, char,floor)
                evillist.append(Evil(True,350,EVILPOSITIONY,EVILCHARACTER,1))
                evillist.append(Evil(False,250,EVILPOSITIONY-80,pygame.transform.flip(EVILCHARACTER,True,False),2))
                evillist.append(Evil(True,650,EVILPOSITIONY-160,EVILCHARACTER,3))
                evillist.append(Evil(False,200,EVILPOSITIONY-160,pygame.transform.flip(EVILCHARACTER,True,False),3))
                evillist.append(Evil(True,500,EVILPOSITIONY-240,EVILCHARACTER,4))
                evillist.append(Evil(False,700,EVILPOSITIONY-320,pygame.transform.flip(EVILCHARACTER,True,False),5))
                evillist.append(Evil(True,400,EVILPOSITIONY-320,EVILCHARACTER,5))
                evillist.append(Evil(True,0,EVILPOSITIONY-480,EVILCHARACTER,7))
                evillist.append(Evil(False,300,EVILPOSITIONY-480,pygame.transform.flip(EVILCHARACTER,True,False),7))
                
                coinList=[]
                for i in range(1,6):
                    for j in range(1,6,2):
                        coin=Coin(i*60,730-(j*80),False,COIN)
                        coinList.append(coin)
            ##    evil=pygame.Rect(0,EVILPOSITIONY,EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT)
                player=pygame.Rect(740,PLAYERPOSITIONY,CHARACTER_WIDTH,CHARACTER_HEIGHT)
                clock= pygame.time.Clock()
                count_jump=0
                injump=False
                global FLOOR
                global run
                while run:
                    clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run=False
                            pygame.quit()
                            quit()
                            
                    checkGame(evillist,player,coinList)
                    drawWindow(evillist,player,coinList)
                    if FLOOR==1 or FLOOR==3 or FLOOR==5 or FLOOR==8:
                        checkCoin(coinList,player)
                    keys_pressed=pygame.key.get_pressed()
                    

                    if player.y>=70:
                        if player.y==77 and player.x<480:
                            pass
                        elif player.y==77 and player.x>480:    
                            player.y,PLAYERPOSITIONY,injump,count_jump=updatePosition(player.y,PLAYERPOSITIONY,injump,count_jump)
                        else:
                            player.y,PLAYERPOSITIONY,injump,count_jump=updatePosition(player.y,PLAYERPOSITIONY,injump,count_jump)
                            
                    if keys_pressed[pygame.K_RIGHT]:
                        player.x=moveRight(player)
                    elif keys_pressed[pygame.K_LEFT]:
                        player.x=moveLeft(player)


                    if player.y!=237 or (player.y==237 and player.x<480):
                        if (keys_pressed[pygame.K_UP] or injump):
                            player.y,injump,count_jump=jump(player.y,injump,count_jump)
                    if player.y==237 and player.x>480 and injump==True:
                        SCORE+=10
                        FLOOR+=1
                        injump=False
                        PLAYERPOSITIONY=237
                        count_jump=0


                    if player.y==77 and player.x<=480 and keys_pressed[pygame.K_LEFT]:
                            count_jump=20
                            injump=True
                            player.y,injump,count_jump=jump(player.y,injump,count_jump)
                            PLAYERPOSITIONY=157
                            FLOOR-=1

                    for evil in evillist:
                        evil,evil.motion=moveEvilX(evil,evil.motion)



            def drawWindow(evillist,player,coinList):
                global GAMEOVER        #coins at 492
                global COIN_SCORE
                global FLOOR
                global PLAYERPOSITIONY
                global EVILPOSITIONY
                global SCORE
                global GAMEOVER
                if not GAMEOVER:
                    WIN.blit(BACKGROUND,(-80,0))
                    score_text=FONT.render("SCORE: "+str(SCORE),1,(0,0,0))
                    WIN.blit(score_text,(WIDTH-score_text.get_width()-10,10))
                    WIN.blit(COIN,(10,6))
                    xp_text=FONT.render("x"+str(COIN_SCORE),1,(0,0,0))
                    WIN.blit(xp_text,(40,10))
                    l=692
                    for i in range(8):          #placing of bricks
                        if(i==7):
                            WIN.blit(BRICKBLOCKLVL2,(800-WIDTH/3,l))
                        else:
                            WIN.blit(BRICK,(0,l))
                        l-=80            
                    for coin in coinList:        #placing of coins
                        if not coin.collected:
                            WIN.blit(coin.image,(coin.x,coin.y))
                    WIN.blit(TREASURE,(600,30))
                    for evil in evillist:             #Placing of evil
                        x=evil.x
                        y=evil.y
                        WIN.blit(evil.image,(x,y))
                    
                    WIN.blit(CHARACTER,(player.x,player.y))
                else:
                    global run
                    WIN.fill((225,225,29))
                    
                    pygame.draw.rect(WIN,(255,255,255),pygame.Rect(150,280,500,200))
                    status=MENUFONT.render(GAMESTATUS,1,(0,0,0))
                    WIN.blit(status,(220,300))
                    score_text=FONT.render("SCORE: "+str(SCORE),1,(0,0,0))
                    WIN.blit(score_text,(220,400))
                    WIN.blit(COIN,(400,396))
                    xp_text=FONT.render("x"+str(COIN_SCORE),1,(0,0,0))
                    WIN.blit(xp_text,(430,400))
                    pressenter=FONT.render("Press enter to continue.....",1,(0,0,0))
                    WIN.blit(pressenter,(220,430))
                    pygame.display.update()
                    while run:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                run=False
                                quit()
                        
                        keys_pressed=pygame.key.get_pressed()
                        if keys_pressed[pygame.K_RETURN]:
                            
                            COIN_SCORE=0
                            FLOOR=1
                            PLAYERPOSITIONY =637
                            EVILPOSITIONY =624
                            SCORE=0
                            GAMEOVER=False
                            LEVEL(1,PLAYERPOSITIONY)
                        elif keys_pressed[pygame.K_ESCAPE]:
                            pygame.quit()
                            run=False
                            quit()

                pygame.display.update()



                


            def menuPage(PLAYERPOSITIONY):
                global run
                global NAV
                while run:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run=False


                    WIN.fill((225,225,29))
                    pygame.draw.rect(WIN,(255,255,255),pygame.Rect(300,NAV,300,50))
                    play=MENUFONT.render("PLAY",1,(0,0,0))
                    WIN.blit(play,(320,200))
                    
                    play=MENUFONT.render("QUIT",1,(0,0,0))
                    WIN.blit(play,(320,300))
                    keys_pressed=pygame.key.get_pressed()
                    if keys_pressed[pygame.K_UP]:  
                        NAV=200
                    if keys_pressed[pygame.K_DOWN]:    
                        NAV=300
                    if keys_pressed[pygame.K_RETURN]:
                        if(NAV==200):
                            startGame(PLAYERPOSITIONY)
                        else:
                            pygame.quit()
                            quit()
                    pygame.display.update()     


            def main(PLAYERPOSITIONY):
                menuPage(PLAYERPOSITIONY)
        
            main(PLAYERPOSITIONY)



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

            if evil.x<730 and motion:
                evil.x+= 2
            elif evil.x<380 and evil.floor==4:
                evil.image=pygame.transform.flip(evil.image,True,False)
                motion=True
            elif evil.x<-20:
                evil.image=pygame.transform.flip(evil.image,True,False)
                motion=True
            else:
                if evil.x==730:
                    evil.image=pygame.transform.flip(evil.image,True,False)
                evil.x-= 2
                motion=False
            return evil,motion

        def moveRight(player):
            if player.y==477:
                if player.x<340:
                    player.x=player.x+2
            else:
                if player.x<740:
                    player.x=player.x+2
            return player.x

        def moveLeft(player):
            if player.x>-10:
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
                        coin.image=None
                        if not coin.collected:
                            global COIN_SCORE
                            COIN_SCORE+=1
                        coin.collected=True
            
        def checkGame(evillist,player,coinList):
            global GAMEOVER
            global GAMESTATUS
            if FLOOR<7:
                evil=evillist[FLOOR-1]
                if evil.x!=None:
                    if((evil.x-50==player.x or evil.x+50==player.x or evil.x-51==player.x or evil.x+51==player.x or evil.x-52==player.x or evil.x+52==player.x) and (evil.y+13==player.y or evil.y+14==player.y or evil.y+12==player.y or evil.y+15==player.y or evil.y+11==player.y)):
                        GAMEOVER =True
                        GAMESTATUS="You Lost"
                        drawWindow(evillist,player,coinList)
            elif FLOOR==7:
                if player.x==50:
                    GAMESTATUS="You Won"
                    GAMEOVER =True
            return


        def startGame(PLAYERPOSITIONY):
            #    listevil=[pygame.Rect(0,EVILPOSITIONY,EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT),pygame.Rect(40,EVILPOSITIONY+80,EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT)]
            evillist=[]  #(motion, x, y, char,floor)
            evillist.append(Evil(True,350,EVILPOSITIONY,EVILCHARACTER,1))
            evillist.append(Evil(False,250,EVILPOSITIONY-80,pygame.transform.flip(EVILCHARACTER,True,False),2))
            evillist.append(Evil())
            evillist.append(Evil(True,500,EVILPOSITIONY-240,EVILCHARACTER,4))
            evillist.append(Evil(False,700,EVILPOSITIONY-320,pygame.transform.flip(EVILCHARACTER,True,False),5))
            evillist.append(Evil(True,340,EVILPOSITIONY-400,EVILCHARACTER,6))

            coinList=[]
            for i in range(1,6):
                coin=Coin(i*60,401,False,COIN)
                coinList.append(coin)
        ##    evil=pygame.Rect(0,EVILPOSITIONY,EVILCHARACTER_WIDTH,EVILCHARACTER_HEIGHT)
            player=pygame.Rect(640,PLAYERPOSITIONY,CHARACTER_WIDTH,CHARACTER_HEIGHT)
            clock= pygame.time.Clock()
            count_jump=0
            injump=False
            global FLOOR
            global SCORE
            global run
            while run:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run=False
                        pygame.quit()
                        quit()
                        
                checkGame(evillist,player,coinList)
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

                if player.y!=557 or (player.y==557 and player.x<340):
                    if (keys_pressed[pygame.K_UP] or injump):
                        player.y,injump,count_jump=jump(player.y,injump,count_jump)
                if player.y==557 and player.x>340 and injump==True:
                    SCORE+=10
                    FLOOR+=1
                    injump=False
                    PLAYERPOSITIONY=557
                    count_jump=0


                if player.y==397 and player.x==344 and keys_pressed[pygame.K_LEFT]:
                        count_jump=20
                        injump=True
                        player.y,injump,count_jump=jump(player.y,injump,count_jump)
                        PLAYERPOSITIONY=477
                        FLOOR-=1

                i=0
                for evil in evillist:
                    if i!=2:
                        evil,evil.motion=moveEvilX(evil,evil.motion)
                    i+=1



        def drawWindow(evillist,player,coinList):     
            global GAMEOVER        #coins at 492
            global COIN_SCORE
            global FLOOR
            global PLAYERPOSITIONY
            global EVILPOSITIONY
            global SCORE
            global GAMEOVER


            if not GAMEOVER:
                WIN.blit(BACKGROUND,(-80,0))
                score_text=FONT.render("SCORE: "+str(SCORE),1,(0,0,0))
                WIN.blit(score_text,(WIDTH-score_text.get_width()-10,10))
                WIN.blit(COIN,(10,6))
                xp_text=FONT.render("x"+str(COIN_SCORE),1,(0,0,0))
                WIN.blit(xp_text,(40,10))
                l=692
                for i in range(7):
                    if(i==3):
                        WIN.blit(BRICKBLOCKLVL1,(WIDTH/2,l))
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
                WIN.fill((225,225,29))
                
                pygame.draw.rect(WIN,(255,255,255),pygame.Rect(150,280,500,200))
                status=MENUFONT.render(GAMESTATUS,1,(0,0,0))
                WIN.blit(status,(220,300))
                score_text=FONT.render("SCORE: "+str(SCORE),1,(0,0,0))
                WIN.blit(score_text,(220,400))
                WIN.blit(COIN,(400,396))
                xp_text=FONT.render("x"+str(COIN_SCORE),1,(0,0,0))
                WIN.blit(xp_text,(430,400))
                pressenter=FONT.render("Press enter to continue.....",1,(0,0,0))
                WIN.blit(pressenter,(220,430))
                pygame.display.update()
                while run:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            run=False
                            quit()
                    
                    keys_pressed=pygame.key.get_pressed()
                    if keys_pressed[pygame.K_RETURN]:
                        
                        COIN_SCORE=0
                        FLOOR=1
                        PLAYERPOSITIONY =637
                        EVILPOSITIONY =624
                        SCORE=0
                        GAMEOVER=False
                        LEVEL2(PLAYERPOSITIONY)
                    elif keys_pressed[pygame.K_ESCAPE]:
                        pygame.quit()
                        run=False
                        quit()

            pygame.display.update()



            


        def menuPage(PLAYERPOSITIONY):
            global run
            global NAV
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run=False


                WIN.fill((225,225,29))
                pygame.draw.rect(WIN,(255,255,255),pygame.Rect(300,NAV,300,50))
                play=MENUFONT.render("PLAY",1,(0,0,0))
                WIN.blit(play,(320,200))
                
                play=MENUFONT.render("QUIT",1,(0,0,0))
                WIN.blit(play,(320,300))
                keys_pressed=pygame.key.get_pressed()
                if keys_pressed[pygame.K_UP]:  
                    NAV=200
                if keys_pressed[pygame.K_DOWN]:    
                    NAV=300
                if keys_pressed[pygame.K_RETURN]:
                    if(NAV==200):
                        startGame(PLAYERPOSITIONY)
                    else:
                        pygame.quit()
                        quit()
                pygame.display.update()     


        def main(PLAYERPOSITIONY):
            menuPage(PLAYERPOSITIONY)
    
        main(PLAYERPOSITIONY)





if __name__ == "__main__":
    LEVEL(1,PLAYERPOSITIONY)
