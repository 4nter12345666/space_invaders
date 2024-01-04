import pygame
pygame.init()
w=1280
e=720
y=680
x=640
n=11
r=130   #x
t=40    #y
FPS=60
speed=5
speed_2=5
sc=pygame.display.set_mode((w, e))
pygame.display.set_caption(" ")
q=True
clock=pygame.time.Clock()
ship=pygame.image.load("images/ship1.png")
ship=pygame.transform.scale(ship, (ship.get_width()//10, ship.get_height()//10))

paz=pygame.image.load("images/parazit_1.png")
paz=pygame.transform.scale(paz, (paz.get_width()*0.7, paz.get_height()*0.7))

right=left=False
pazr=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(n):
    pazr[i] = paz.get_rect(center=(r+i*100, t))
shipr = ship.get_rect(center=(x, y))

while q:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            q=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left=True
                print(f"lkjgf{x} ")
            elif event.key == pygame.K_RIGHT:
                right=True
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                q = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            elif event.key == pygame.K_RIGHT:
                right = False
    if left:
        x -= speed
    if right:
        x += speed
    r=r+speed_2

    #pygame.draw.rect(sc, (0, 0, 0), (x-50, y-50, 500, 500) )
    pygame.draw.rect(sc, (0, 0, 0), shipr)

    shipr = ship.get_rect(center=(x, y))
    sc.blit(ship, shipr)

    for i in range(n):
        pygame.draw.rect(sc, (0, 0, 0), pazr[i])
        pazr[i] = paz.get_rect(center=(r + i * 100, t))
        sc.blit(paz, pazr[i])
    pygame.display.update()
    clock.tick(FPS)

#    if r==w:
 #       speed_2=-5
#    elif r==0:
#        speed_2=5
    if pazr[n-1].right>=w or pazr[0].left<=0:
        speed_2 = -speed_2

    #if pazr[0].colliderect(buller):

        #