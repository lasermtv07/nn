#!/usr/bin/python3
import pygame as pg
import sys
import math as m
import random
pg.init()
data=[]
for i in range(0,256):
    data.append(0)
screen=pg.display.set_mode((256,256))
font = pg.font.Font(pg.font.get_default_font(), 16)
text=font.render('test',True,(255,255,255),(0,0,0))
textRect=text.get_rect()
textRect.top=240
char=1
txt=""
while True:
    text=font.render(f'Write: {str(char)}',True,(255,255,255),(0,0,0))
    textRect=text.get_rect()
    textRect.top=240
    screen.blit(text, textRect)
    for e in pg.event.get():
        if e.type==pg.QUIT:
            print(txt)
            f=open('data.txt','r')
            d=f.read()
            f.close()
            f=open('data.txt','w')
            f.write(d+"\n"+txt)
            f.close()
            sys.exit()
        if e.type==pg.KEYDOWN: 
            if e.key==127:
                data=[]
                for i in range(0,256):
                    data.append(0)
            else:
                txt+=str(char)
                txt+="=>"
                for i in data:
                    txt+=str(i)
                txt+="\n"
                char=random.randint(0,9)
                data=[]
                for i in range(0,256):
                    data.append(0)
    for i in range(16):
        pg.draw.line(screen,(32,32,32),(0,16+i*16),(256,16+i*16))
        pg.draw.line(screen,(32,32,32),(16+i*16,0),(16+i*16,256))
    for i in range(0,16):
        for j in range(0,16):
            if data[16*i+j]==1:
                pg.draw.rect(screen,(255,255,255),pg.Rect(16*j,16*i,16,16))
    
    if pg.mouse.get_pressed()[0]:
        x=pg.mouse.get_pos()[0]
        y=pg.mouse.get_pos()[1]
        x=m.floor(x/16)
        y=m.floor(y/16)
        data[x+y*16]=1
    if pg.mouse.get_pressed()[2]:
        x=pg.mouse.get_pos()[0]
        y=pg.mouse.get_pos()[1]
        x=m.floor(x/16)
        y=m.floor(y/16)
        data[x+y*16]=0
    pg.display.flip()
    screen.fill((0,0,0))
