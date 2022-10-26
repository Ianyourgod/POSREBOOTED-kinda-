# import pygame module in this program
import pygame
pygame.init()


S_SIZE = (500,500)
screen = pygame.display.set_mode(S_SIZE,pygame.RESIZABLE)

pygame.display.set_caption('Console 60')


font = pygame.font.Font('freesansbold.ttf', 32)

class cursor:
    def __init__(self,x,y,size) -> None:
        self.rect = pygame.Rect(x,y,size,size*4)
        self.timer = 60
        self.show = True
    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.show = not self.show
            self.timer = 60
clock = pygame.time.Clock()
c = cursor(0,0,10)
while True:
    screen.fill((30,30,30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    c.update()
    if c.show:
        pygame.draw.rect(screen,(180,180,180),c.rect)
    clock.tick(60)
    pygame.display.set_caption(f"Console {round(clock.get_fps()*10)/10}")
    pygame.display.update()
