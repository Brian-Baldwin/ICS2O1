# import libraries
import pygame
from pygame.locals import *
import math
import random
import time

#set colours
black = (0,0,0)
white = (255,255,255)
green = (0,128,0)
bright_green = (0,255,0)
repeat = 1

#define function to find distance from centre
def centre(coord):
    square = ((coord[0]-320)**2 + (coord[1]-240)**2)
    dis = math.sqrt(square)
    return dis
while repeat:
    # 2 - Initialize the game
    #sets up the display window
    pygame.init()
    start_ticks = pygame.time.get_ticks()
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    myfont = pygame.font.SysFont('Arial' , 30)
    width, height = 640, 480
    screen=pygame.display.set_mode((width, height))
    keys = [False, False, False, False, False]
    pygame.mixer.init()
    
    #load images
    ring1 = pygame.image.load("resources/images/target11.png")
    ring2 = pygame.image.load("resources/images/target2.png")
    ring3 = pygame.image.load("resources/images/target3.png")
    ring4 = pygame.image.load("resources/images/target4.png")
    ring5 = pygame.image.load("resources/images/target5.png")
    ring6 = pygame.image.load("resources/images/target6.png")
    ring7 = pygame.image.load("resources/images/target7.png")
    ring8 = pygame.image.load("resources/images/target8.png")
    ring9 = pygame.image.load("resources/images/target9.png")
    ring10 = pygame.image.load("resources/images/target10.png")
    undrawn = pygame.image.load("resources/images/undrawn.png")
    back = pygame.image.load("resources/images/back.png")
    crosshair = pygame.image.load("resources/images/crosshair.png")
    
    #title screen
    title = 1
    while title:
        screen.fill(white)
        position = pygame.mouse.get_pos()
        
        #draw title and start button
        title = myfont.render("Python Archery", True, (255,0,0))
        screen.blit(title, (240,60))
        pygame.draw.rect(screen, green, (240,320,160,40))
        textsurface = myfont.render('Start', True, white)
        screen.blit(textsurface, (295,320))
        
        # instructions
        smallfont = pygame.font.SysFont('Arial' , 18)
        instruct1 = smallfont.render("Hold SPACE to draw the bow", True, black)
        screen.blit(instruct1, (220,400))
        instruct2 = smallfont.render("Use WASD to move the crosshair", True, black)
        screen.blit(instruct2, (210,420))
        instruct3 = smallfont.render("Release SPACE to shoot", True, black)
        screen.blit(instruct3, (230,440))
        
        #draw bow
        screen.blit(undrawn, (280,100))
    
        #check if mouse is on button and starts game on click
        if 400 > position[0] > 240 and 360 > position[1] > 320:
            pygame.draw.rect(screen, bright_green,(240,320,160,40))
            textsurface = myfont.render('Start', True, white)
            screen.blit(textsurface, (295,320))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and 400 > position[0] > 240 and 360 > position[1] > 320:
                title = 0
        pygame.display.flip()
        
    #game setup
    roundnum = 1
    
    #function for a single shot
    def shot(roundNum):
        colis1 = False
        colis2 = False
        colis3 = False
        colis4 = False
        colis5 = False
        colis6 = False
        colis7 = False
        colis8 = False
        colis9 = False
        colis10 = False
        #more game setup
        running = 1
        exitcode = 0
        score = 0
        playerpos = (400,300)
        position = (320,240)
        crosspos = [200,300]
        aim = [0,0]
        accel = 0.01
        speed = [0,0,0,0]
        shots = 3
        aim1 = [0,0,0,0]
        drawn = 0
        while running:
            #fill screen with black
            screen.fill(0)
            screen.blit(back, (0,0))
            #set acceleration randomly based on round number
            if roundNum == 1:
                accel = 0.01
            elif roundNum == 2:
                accel = random.uniform(0.03, 0.05)
            elif roundNum == 3:
                accel = random.uniform(0.08, 0.1)
                
            # turn bow to point at crosshair
            position = aim
            angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
            playerrot = pygame.transform.rotate(undrawn, 560-angle*57.29)
            screen.blit(playerrot, playerpos)
            
            #remind player to draw the bow
            dRaw = smallfont.render("Hold SPACE to draw the bow", True, white)
            screen.blit(dRaw, (200, 380))
            
            #check for events
            for event in pygame.event.get():
                # check if the event is the X button 
                if event.type==pygame.QUIT:
                    # if it is quit the game
                    pygame.quit()
                    exit(0)
                #check if keys are pressed
                if event.type == pygame.KEYDOWN:
                    if event.key==K_w:
                        keys[0]=True
                    if event.key==K_a:
                        keys[1]=True
                    if event.key==K_s:
                        keys[2]=True
                    if event.key==K_d:
                        keys[3]=True
                    if event.key==K_SPACE:
                        keys[4]=True
                        drawn = 1
                if event.type == pygame.KEYUP:
                    if event.key==pygame.K_w:
                        keys[0]=False
                    elif event.key==pygame.K_a:
                        keys[1]=False
                    elif event.key==pygame.K_s:
                        keys[2]=False
                    elif event.key==pygame.K_d:
                        keys[3]=False
                    if event.key==pygame.K_SPACE:
                        keys[4]=False
                        
            #draw rings
            screen.blit(ring1, (220,140))
            screen.blit(ring2, (230,150))
            screen.blit(ring3, (240,160))
            screen.blit(ring4, (250,170))
            screen.blit(ring5, (260,180))
            screen.blit(ring6, (270,190))
            screen.blit(ring7, (280,200))
            screen.blit(ring8, (290,210))
            screen.blit(ring9, (300,220))
            screen.blit(ring10, (310,230))
            
            # draw crosshair
            if keys[4]:
                screen.blit(crosshair, crosspos)
                
            #move crosshair
            aim[0] = crosspos[0] + 36
            aim[1] = crosspos[1] + 36
            crosspos[1]-=speed[0]
            crosspos[1]+=speed[2]
            crosspos[0]-=speed[1]
            crosspos[0]+=speed[3]

            #acceleration physics
            if keys[0]:
                speed[0] = speed[0] + accel
            elif keys[0] == False:
                speed[0] = speed[0] - accel*0.2
            if speed[0] < 0:
                speed[0] = 0
            if keys[1]:
                speed[1] = speed[1] + accel
            elif keys[1] == False:
                speed[1] = speed[1] - accel*0.2
            if speed[1] < 0:
                speed[1] = 0
            if keys[2]:
                speed[2] = speed[2] + accel
            elif keys[2] == False:
                speed[2] = speed[2] - accel*0.2
            if speed[2] < 0:
                speed[2] = 0
            if keys[3]:
                speed[3] = speed[3] + accel
            elif keys[3] == False:
                speed[3] = speed[3] - accel*0.2
            if speed[3] < 0:
                speed[3] = 0
                
            #stops crosshair from moving if space is released
            if keys[4] == False:
                speed = [0,0,0,0]
                
            #create target area for target rings
            colis = centre(aim)
            if colis < 100 and colis >90:
                colis1 = True
            else:
                colis1 = False
            if colis < 90 and colis >80:
                colis2 = True
            else:
                colis2 = False
            if colis < 80 and colis >70:
                colis3 = True
            else:
                colis3 = False
            if colis < 70 and colis >60:
                colis4 = True
            else:
                colis4 = False
            if colis < 60 and colis >50:
                colis5 = True
            else:
                colis5 = False
            if colis < 50 and colis >40:
                colis6 = True
            else:
                colis6 = False
            if colis < 40 and colis >30:
                colis7 = True
            else:
                colis7 = False
            if colis < 30 and colis >20:
                colis8 = True
            else:
                colis8 = False
            if colis < 20 and colis >10:
                colis9 = True
            else:
                colis9 = False
            if colis < 10:
                colis10 = True
            else:
                colis10 = False
            #collision detection
            aim1[0] = crosspos[0] + 35
            aim1[1] = crosspos[1] + 35
            aim1[2] = 1
            aim1[3] = 1
            aimrect = pygame.Rect(aim1)
            if drawn:
                if keys[4] == False and crosspos != [200,300]:
                    shots -= 1
                    if colis1:
                        score = score + 1
                    elif colis2:
                        score +=2
                    elif colis3:
                        score+=3
                    elif colis4:
                        score+=4
                    elif colis5:
                        score+=5
                    elif colis6:
                        score+=6
                    elif colis7:
                        score+=7
                    elif colis8:
                        score+=8
                    elif colis9:
                        score+=9
                    elif colis10:
                        score += 10
                    display = smallfont.render("You scored " + str(score) + "!", True, bright_green)
                    screen.blit(display, (260, 100))
                    pygame.display.flip()
                    time.sleep(2)
                    running = 0
                    
            #refresh screen
            pygame.display.flip()
        return score
    
    score = 0
    totscore = 0
    roundnum = 1
    
    #call function for game in for loops to repeat for 3 shots per round and 3 rounds
    for i in range(3):
        for i in range(3):
            score = shot(roundnum)
            totscore+=score
            print(totscore)
        roundnum+=1
        if roundnum < 4:
            
            #draw screen for next round
            while True:
                screen.fill(0)
                screen.blit(back, (0,0))
                next1 = myfont.render("The next round will start soon", True, white)
                screen.blit(next1, (120, 240))
                pygame.display.flip()
                time.sleep(2)
                break
    avScore = totscore / 3
    
    #endgame screen
    while True:
        screen.fill(0)
        screen.blit(back, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                
    #rates and displays user's average score
        if avScore < 20:
            rate = "Try again next time!"
        elif avScore > 19 and avScore < 25:
            rate = "You did well"
        else:
            rate = "You have very good aim!"
        score = myfont.render(str(avScore), True, black)
        endmsg = myfont.render("You had an average score of " + str(round(avScore, 2)), True, white)
        screen.blit(endmsg, (120, 200))
        rate1 = myfont.render(rate, True, white)
        screen.blit(rate1, (200, 240))
        
    #asks user if they want to restart game
        pygame.draw.rect(screen, green, (240,347,160,40))
        yes = font.render("Replay", True, white)
        screen.blit(yes, (290,360))
        
        #check if mouse is on button and starts game on click
        position=pygame.mouse.get_pos()
        if 400 > position[0] > 240 and 387 > position[1] > 347:
            pygame.draw.rect(screen, bright_green,(240,347,160,40))
            textsurface = font.render('Replay', True, white)
            screen.blit(textsurface, (290,360))
        if event.type==pygame.MOUSEBUTTONDOWN and 400 > position[0] > 240 and 387 > position[1] > 347:
            break
        pygame.display.flip()
    


