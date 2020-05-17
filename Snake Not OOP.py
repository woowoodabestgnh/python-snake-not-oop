# -*- coding: utf-8 -*-


import pygame
import time
import random

black = (0,0,0)
blue = (0,0,200)
red = (200, 0, 0)
green = (0, 200, 0)
white = (240,240,240)
winheight = 400
winwidth = 800
gridsize = 20




def window(x, y):
    win = pygame.display.set_mode((x,y))
    pygame.display.set_caption('Snake')
    return win


def drawsnake(window,snakelist):
    for position in snakelist:
        pygame.draw.rect(window, red, (position[0], position[1], gridsize, gridsize))


def apple():
    applex = round(random.randrange(0, winwidth - gridsize)/gridsize) * gridsize
    appley = round(random.randrange(0, winheight- gridsize)/gridsize) * gridsize
    return [applex, appley]

def message(message, x, y, window):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(message, True, green)
    textRect = text.get_rect()
    textRect.center = (x, y)
    window.blit(text, textRect)
    
    

def main():
    pygame.init()
    win = window(winwidth,winheight)
    clock = pygame.time.Clock()
    gameon = False
    startgame = True
    endgame = False
    
    x = 200
    y = 200
    x_change = 0
    y_change = 0
    
    snakelist = []
    snakelength = 1
    snakespeed = 15
    applecoords = apple()
    while startgame == True:
        win.fill(white)
        message('Press P to start or Q to Quit', winwidth/2, winheight/2, win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameon = True
                    startgame = False
                if event.key == pygame.K_q:
                    startgame = False
                    pygame.quit()
                    
                    
    while gameon == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameon = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change += gridsize
                    y_change = 0
                if event.key == pygame.K_LEFT:
                    x_change -= gridsize
                    y_change = 0
                if event.key == pygame.K_UP:
                    y_change -= gridsize
                    x_change = 0
                if event.key == pygame.K_DOWN:
                    y_change += gridsize
                    x_change = 0
                if event.key == pygame.K_s:
                    snakespeed = 0.01
        x += x_change
        y += y_change
        if x < 0 or y < 0 or x > winwidth - gridsize or y > winheight - gridsize :
            endgame = True
        
        win.fill(black)
        pygame.draw.rect(win, green, (applecoords[0], applecoords[1], gridsize, gridsize))
        snakehead = [x,y]
        
        for position in snakelist:
            if snakelength > 1:
                if snakehead in snakelist:
                    #Change to Exit "Page"
                    endgame = True

        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
           del snakelist[0]
          
        drawsnake(win,snakelist)
        
        score = snakelength
        score = str(score)
        message('score:', 64,32, win)
        message(score, 64, 64, win)
        
        
        pygame.display.update()
        if x == applecoords[0] and y == applecoords[1]:
            applecoords = apple()
            snakelength += 1
        
   
        
        while endgame == True:
            win.fill(white)
            message('You lost! Press P to Start or Q to Quit.', winwidth/2, winheight/2, win)
            message('Your score was:', winwidth/2, (winheight/2 + 64), win)
            message(score, (winwidth/2 + 150), (winheight/2 + 64), win)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        main()
                    if event.key == pygame.K_q:
                        endgame = False
                        pygame.quit()
            
        clock.tick(snakespeed)


main()























            
    
    
    
    
    
