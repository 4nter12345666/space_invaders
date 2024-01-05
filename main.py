import pygame
pygame.init()
v=False
w=1280
e=720
y=680
x=640
n=11
m=5
qq=n*m
r=130   #x
t=40    #y
FPS=60
speed=5   #speed of the ship
speed_2=1.9   #speed of the paz
speed_3=9.8888888888888888888888812  #speed of the buller
a=x
s=y
buller=pygame.rect.Rect(a, s, 5, 10)
sc=pygame.display.set_mode((w, e))
pygame.display.set_caption(" ")
q=True
clock=pygame.time.Clock()
ship=pygame.image.load("images/ship1.png").convert_alpha()
ship=pygame.transform.scale(ship, (ship.get_width()//10, ship.get_height()//10))

paz=pygame.image.load("images/parazit_1.png").convert()
paz=pygame.transform.scale(paz, (paz.get_width()*0.7, paz.get_height()*0.7))

paz2=pygame.image.load("images/par2.png").convert_alpha()
paz2=pygame.transform.scale(paz2, (paz2.get_width()*0.7, paz2.get_height()*0.7))
right=left=False
pazr=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pazrdead=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(qq):
    pazr[i] = paz.get_rect()
shipr = ship.get_rect(center=(x, y))
#paz2r=paz2.get_qwerty
while q:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            q=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                v=True
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

    #dvizhenie korablya
    if left:
        x -= speed
    if right:
        x += speed

    #dvizhenie buller po garizontali if ne vistrel
    if not v:
        if left:
            a = x
            #s = y
        if right:
            a = x
            #s = y

    #dvizhenie buller po vertikali
    if v:
        s=s-speed_3



    r=r+speed_2 #dvizhenie parazitov

    pygame.draw.rect(sc, (0, 0, 0), buller)  # zakrashibaem ctaruyu poziciyu of buller
    buller.center = (a, s) #zadaem new koordinati bulleru
    pygame.draw.rect(sc, (255, 255, 255), buller) #ricuem buller v novom mecte

    #pygame.draw.rect(sc, (0, 0, 0), (x-50, y-50, 500, 500) )
    pygame.draw.rect(sc, (0, 0, 0), shipr)
    shipr = ship.get_rect(center=(x, y))
    sc.blit(ship, shipr)

    plyf = buller.collidelist(pazr)
    print(plyf)
    if plyf!=-1 and not pazrdead[plyf]:
        v=False
        s=y
        a=x
        pazrdead[plyf]=True


    for i in range(qq):
        str = i // 11
        stl = i % 11
        pygame.draw.rect(sc, (0, 0, 0), pazr[i])   #черный квадрат
        pazr[i] = paz.get_rect(center=(r + stl * 100, t+str*80))

        if pazrdead[i]:
            pass
        elif str<1:
            sc.blit(paz2, pazr[i])
        elif str>=1:
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

        #vozvrat bullera ecli kocnulca kraya
    if s<=10:
        v=False
        a=x
        s=y