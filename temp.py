import sys, pygame
import random
pygame.init()

size = width, height = 1001, 701
speed = [5, 5]
black = 0, 0, 0
squareSide = 20

screen = pygame.display.set_mode(size)
ball = pygame.image.load("intro_ball.png")
ballrect = ball.get_rect()

#pygame.draw.line(screen,(255,255,255),(0,20),(100,20))
nv = width // squareSide + 1
nh = height // squareSide + 1
x = random.randint(0, nv)
y = random.randint(0, nh)
while 1:
    for event in pygame.event.get():
        print(event)
        print(event.type)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
            elif event.key == pygame.K_RIGHT:
                x += 1
            elif event.key == pygame.K_UP:
                y -= 1
            elif event.key == pygame.K_DOWN:
                y += 1
    #    a=5
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)


    for i in range(0, nv):
        pygame.draw.line(screen, (255, 255, 255), (i*squareSide, 0), (i*squareSide, height))
    for j in range(0, nh):
        pygame.draw.line(screen, (255, 255, 255), (0, j*squareSide), (width, j*squareSide))

    pygame.draw.rect(screen, (0,0,255), (x*squareSide+1,y*squareSide+1,squareSide-2,squareSide-2))
    screen.blit(ball, ballrect)
    pygame.display.flip()
