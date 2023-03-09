import pygame
import random
import math
import time
from sys import exit
pygame.init()
pygame.display.set_caption("Powers")
global userscore
timeout = False
oneturn = False
dragging = False
convert = False
count = 0
clicked = ''
screen = pygame.display.set_mode((700,600))
clock = pygame.time.Clock()
screen.fill('#131414')
text = pygame.font.Font('C:/Users/Family/Documents/ClearSans-Medium.ttf',35)
coefficients = [1,2,4,25,49,64]
powers = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
powerxpos = [219, 314, 404, 494, 219, 314, 404, 494, 219, 314, 404, 494, 219, 314, 404, 494 ]
powerypos = [150, 150, 150, 150, 240, 240, 240, 240, 330, 330, 330, 330, 420, 420, 420, 420 ]
powertext = pygame.font.Font('C:/Users/Family/Documents/ClearSans-Medium.ttf',15)
powerblit = powertext.render((str(powers[3])),True,'white')
xs = [190, 285, 380, 475, 190, 285, 380, 475, 190, 285, 380, 475, 190, 285, 380, 475]
ys = [220, 220, 220, 220, 315, 315, 315, 315, 410, 410, 410, 410, 505, 505, 505, 505]
name = pygame.font.Font('C:/Users/Family/Documents/ClearSans-Medium.ttf',40)
thename = name.render(('Powers'),True,('white'))
screen.blit(thename,(245,40))
currentcoefficients = []
for i in range(16):
    choice = random.choice(coefficients)
    currentcoefficients.append(choice)
insert = ''
#print (tiles)


def draw(thecount):
    row = 4
    column = 4
    count = 0
    mouse = pygame.mouse.get_pos()
    mouse_x = mouse[0]
    mouse_y = mouse[1]
    alreadyclicked = False
    keys = pygame.key.get_pressed()
    current = 0
    for i in range(row):
        for j in range (column):
            if currentcoefficients[current] == 0:
                thecount += 1
            if currentcoefficients[current] == 1:
                if powers[current] != 1:
                    thetexts = text.render(('(x)'),True,'white')
                else:
                    thetexts = text.render(('x'),True,'white')


            else:
                if powers[current] != 1:
                    thetexts = text.render('(' + (str((currentcoefficients[current] )) + 'x)'),True,'white')
                else:
                    thetexts = text.render((str((currentcoefficients[current] )) + 'x'),True,'white')
            powerblit = powertext.render((str(powers[current])),True,'white')
            if current != thecount:
                tile = pygame.image.load('C:/Users/Family/Documents/tile.png')
                tile = pygame.transform.scale(tile,(85,85))
                tile_rect = tile.get_rect(midbottom = (xs[current],ys[current]))
            

            else:
                tile = pygame.image.load('C:/Users/Family/Documents/selectedtile.png')
                tile = pygame.transform.scale(tile,(85,85))
                tile_rect = tile.get_rect(midbottom = (xs[current],ys[current]))
                tempstore = current
                if clicked == True:
                    if alreadyclicked == False and currentcoefficients[tempstore] == currentcoefficients[tempstore + 1]:
                        screen.fill('#131414')
                        powers[tempstore + 1]  = powers[tempstore] - powers[tempstore + 1]
                        if powers[tempstore + 1] == 0:
                            currentcoefficients[tempstore+1] = 0
                        thename = name.render(('Powers'),True,('white'))
                        screen.blit(thename,(245,25))
                        pygame.display.update()
                        tile_rect.x += 50
                        thex = tile_rect.x
                        alreadyclicked = True
                      


                        currentcoefficients[tempstore] = 0
                        time.sleep(0.1)

                    
                if convert == True:
                    test = math.sqrt(currentcoefficients[tempstore])
                    thetest = round(test,1)
                    if currentcoefficients[tempstore] != 1 and thetest == int(test):
                        temp = currentcoefficients[tempstore]
                        currentcoefficients[tempstore] = int(math.sqrt(currentcoefficients[tempstore]))
                        thepower = int(math.log(temp,currentcoefficients[tempstore]))
                        powers[tempstore] = thepower
                
                
                    
            if currentcoefficients[current] != 0:
                if currentcoefficients[current] > 10:
                    if powers[current] != 1:
                        tile.blit(thetexts,(4,20))
                    else:
                        tile.blit(thetexts,(12,20))
                elif currentcoefficients[current] == 1:
                    tile.blit(thetexts,(25,17))
                else:
                    if powers[current] != 1:
                        tile.blit(thetexts,(13,20))
                    else:
                        tile.blit(thetexts,(24,20))

                screen.blit(tile,tile_rect)
                if powers[current] != 1:
                    screen.blit(powerblit,(powerxpos[current],powerypos[current]))

            pygame.display.update()
            current +=1

        
draw(count)        
while True:
    zeros = 0
    moves = 0
    thecount = 0
    insertcount = 0
    clicked = False
    inserted = ''
    found = ''
    for i in range(len(currentcoefficients)-1):
        tempcheck = math.sqrt(currentcoefficients[i])
        tempcheck2 = math.sqrt(currentcoefficients[i+1])
        if (currentcoefficients[i] == currentcoefficients[i + 1] or tempcheck == tempcheck2 or tempcheck == currentcoefficients[i+1] or tempcheck2 == currentcoefficients[i]) and currentcoefficients[i] != 0:
            moves += 1
        if i == 0:
            zeros += 1
            if zeros == 15:
                print ('Winner')
                import sys
                sys.exit()
            
    
        
    if moves == 0:
        found = False
        i = 0
        while i != 15 or inserted != True:
            if currentcoefficients[i] == 0:
                currentcoefficients[i] = random.choice(coefficients)
                powers[i] = 1
                inserted = True
                draw(count)
            else:
                if i != 15:
                    i += 1
                else:
                    print ('Game over')
                    import sys
                    sys.exit()
        inserted = ''

    else:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                draw(count)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            count +=1
            if count > 15:
                count = 0
            time.sleep(0.5)
            draw(count)
        
        if keys[pygame.K_LEFT]:
            count -=1
            if count < 0:
                count = 0
            draw(count)
            time.sleep(0.5)

        if keys[pygame.K_UP]:
            count -=4
            if count < 0:
                count += 4
            draw(count)
            time.sleep(0.5)

        if keys[pygame.K_DOWN]:
            count +=4
            if count > 15:
                count -= 4
            draw(count)
            time.sleep(0.5)
        if keys[pygame.K_SPACE]:
            convert = True
            time.sleep(0.5)
            draw(count)
        else:
            convert = False
    pygame.display.update()
    clock.tick(150)