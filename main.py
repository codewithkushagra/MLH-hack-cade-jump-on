import os
import pygame

CHARACTER_WIDTH=80
CHARACTER_HEIGHT=70
WIDTH,HEIGHT =800,900
FPS=60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Jump On")

CHARACTER_IMAGE=pygame.image.load(os.path.join('Assets','player.png'))
CHARACTER=pygame.transform.scale(CHARACTER_IMAGE,(80,70))

def draw_window(player):
    WIN.fill((255,255,255))
    WIN.blit(CHARACTER,(player.x,player.y))
    pygame.display.update()


def main(CHARACTER):
    player=pygame.Rect(0,830,CHARACTER_WIDTH,CHARACTER_HEIGHT)
    clock= pygame.time.Clock()
    motion=True
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

        draw_window(player)
        if player.x<700 and motion:
            player.x+= 1
        elif player.x<0:
            motion=True
        else:
            player.x-= 1
            motion=False

        
    pygame.quit()

if __name__ == "__main__":
    main(CHARACTER)