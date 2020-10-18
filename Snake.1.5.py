# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:23:24 2018

@author: GOUTHAM
"""

import turtle
import random
import os
import time

#initializing score
score=0
high_score=0

wn=turtle.Screen()
wn.setup(width=1000,height=800)
wn.title("HUNGRY SNAKE")
wn.bgpic(os.path.expanduser("~\Desktop\game_screen.gif"))
wn.addshape(os.path.expanduser("~\Desktop\grass.gif"))
wn.addshape(os.path.expanduser("~\Desktop\snake_tail_up.gif"))
wn.addshape(os.path.expanduser("~\Desktop\snake_tail_down.gif"))
wn.addshape(os.path.expanduser("~\Desktop\snake_tail_left.gif"))
wn.addshape(os.path.expanduser("~\Desktop\snake_tail_right.gif"))
wn.addshape(os.path.expanduser("~\Desktop\segment_y.gif"))
wn.addshape(os.path.expanduser("~\Desktop\segment_x.gif"))
wn.addshape(os.path.expanduser("~\Desktop\snake_head_up.gif"))
wn.addshape(os.path.expanduser("~\Desktop\snake_head_down.gif"))
wn.addshape(os.path.expanduser("~\Desktop\snake_head_right.gif"))
wn.addshape(os.path.expanduser("~\Desktop\snake_head_left.gif"))
wn.addshape(os.path.expanduser("~\Desktop\game_rat.gif"))
wn.addshape(os.path.expanduser("~\Desktop\game_fence.gif"))


game_screen=turtle.Turtle()
game_screen.setposition(0,0)
game_screen.speed(0)
game_screen.color("red")
game_screen.write('PRESS ENTER TO PLAY', align='center' , font=('Arial',35,'bold'))
game_screen.penup()

#screen
bg=turtle.Turtle()
bg.shape(os.path.expanduser("~\Desktop\grass.gif"))
bg.speed(0)
bg.penup()

#Snake head
snake=turtle.Turtle()
snake.shape(os.path.expanduser("~\Desktop\snake_head_up.gif"))
snake.speed(0)
snake.penup()#So that it does not draw lines
snake.direction='stop'

#tail
tail=turtle.Turtle()
tail.shape(os.path.expanduser("~\Desktop\snake_tail_right.gif"))
tail.speed(0)
tail.penup()

#fences
f1=turtle.Turtle()
f2=turtle.Turtle()
f3=turtle.Turtle()
f4=turtle.Turtle()
#list of fence turtles
LF=[f1,f2,f3,f4]
for i in LF:
    i.speed(0)
    i.penup()
    i.shape(os.path.expanduser("~\Desktop\game_fence.gif"))
    
f1.setposition(-210,random.randrange(-215,215,60))
f2.setposition(-210,random.randrange(-215,215,60))
f3.setposition(210,random.randrange(-215,215,60))
f4.setposition(210,random.randrange(-215,215,60))
while f1.distance(f2)<65:
    f1.setposition(-210,random.randrange(-215,215,60))
while f3.distance(f4)<65:
    f3.setposition(210,random.randrange(-215,215,60))
y1=f1.ycor()
y2=f2.ycor()
y3=f3.ycor()
y4=f4.ycor()

#body
body=[]

#score board
pen=turtle.Turtle()
pen.speed()
pen.color('white')
pen.penup()
pen.setposition(0,320)
pen.write('Score: 0 High Score: 0', align ='center',font=('Arial',24,'normal'))

#food
food=turtle.Turtle()
food.shape(os.path.expanduser("~\Desktop\game_rat.gif"))
food.speed(0)
food.penup()
def food_correction():
    food.goto(random.randrange(-290,290,30),random.randrange(-290,290,30))
    if food.xcor() in range(-300,-119):
        while food.ycor() in range(y1-30,y1+30) or food.ycor() in range(y2-30,y2+30):
            food.goto(random.randrange(-290,290,30),random.randrange(-290,290,30))
    if food.xcor() in range(120,301):
        while food.ycor() in range(y3-30,y3+30) or food.ycor() in range(y4-30,y4+30):
            food.goto(random.randrange(-290,290,30),random.randrange(-290,290,30)) 
food_correction()

#Functions to move turtle
def up():
    if snake.direction != 'down':
        snake.direction='up'
        snake.tiltangle(90)
        snake.shape(os.path.expanduser("~\Desktop\snake_head_up.gif"))
        tail.shape(os.path.expanduser("~\Desktop\snake_tail_up.gif"))
        segment.shape(os.path.expanduser("~\Desktop\segment_y.gif"))
def down():
    if snake.direction != 'up':
        snake.direction='down'
        snake.tiltangle(270)
        snake.shape(os.path.expanduser("~\Desktop\snake_head_down.gif"))
        tail.shape(os.path.expanduser("~\Desktop\snake_tail_down.gif"))
        segment.shape(os.path.expanduser("~\Desktop\segment_y.gif"))
def right():
    if snake.direction != 'left':
        snake.direction='right'
        snake.tiltangle(0)
        snake.shape(os.path.expanduser("~\Desktop\snake_head_right.gif"))
        tail.shape(os.path.expanduser("~\Desktop\snake_tail_right.gif"))
        segment.shape(os.path.expanduser("~\Desktop\segment_x.gif"))
def left():
    if snake.direction != 'right':
        snake.direction='left'
        snake.tiltangle(180)
        snake.shape(os.path.expanduser("~\Desktop\snake_head_left.gif"))
        tail.shape(os.path.expanduser("~\Desktop\snake_tail_left.gif"))
        segment.shape(os.path.expanduser("~\Desktop\segment_x.gif"))
def move():
    
    if snake.direction=='up':
        snake.sety(snake.ycor()+25)
    if snake.direction=='down':          
        snake.sety(snake.ycor()-25)
    if snake.direction=='left':
        snake.setx(snake.xcor()-25)
    if snake.direction=='right':
        snake.setx(snake.xcor()+25)
        
def segmentx():
    for i in body:
        i.shape(os.path.expanduser("~\Desktop\segment_x.gif"))
def segmenty():
    for i in body:
        i.shape(os.path.expanduser("~\Desktop\segment_y.gif"))
    
def tryagain():
    b=turtle.Turtle()
    b.speed(0)
    b.setposition(0,0)
    b.color("blue")
    b.penup()
    b.hideturtle()
    b.write('Try Again',align='center',font=('Arial',24,'bold'))
    time.sleep(2)
    b.clear()
        
def show():
    wn.bgpic("~\Desktop\game_screen_1.gif")
    snake.showturtle()
    bg.showturtle()
    segment.showturtle()
    tail.showturtle()
    food.showturtle()
    game_screen.hideturtle()
    f1.showturtle()
    f2.showturtle()
    f3.showturtle()
    f4.showturtle()

def collision():
            global score,high_score
            snake.goto(0,0)
            snake.direction="stop"
            snake.shape(os.path.expanduser("~\Desktop\snake_head_right.gif"))   
            for i in body:
                i.goto(1000,1000)
            body.clear()
            snake.hideturtle()
            tail.hideturtle()
            tryagain()
            snake.showturtle()
            tail.showturtle()
            segment=turtle.Turtle()
            segment.shape(os.path.expanduser("~\Desktop\segment_x.gif"))
            segment.speed(0)
            segment.penup()   
            body.append(segment)     
            segment.goto(snake.xcor()-25,snake.ycor())
            tail.shape(os.path.expanduser("~\Desktop\snake_tail_right.gif"))
            tail.goto(segment.xcor()-25,segment.ycor())
            score=0
            pen.clear()
            pen.write('Score: {} High Score: {}'.format(score,high_score),align='center',font=('Arial',24,'normal'))
      
def hit_border():
    if snake.xcor() in range(-300,-120):
        if snake.ycor() in range(y1-20,y1+20) or snake.ycor() in range(y2-20,y2+20):
            collision()
    if snake.xcor() in range(120,300):
        if snake.ycor() in range(y3-20,y3+20) or snake.ycor() in range(y4-20,y4+20):
            collision()
    if snake.xcor()>295 or snake.xcor()<-295 or snake.ycor()>295 or snake.ycor()<-295:
       collision()
             
for turtles in wn.turtles():
    turtles.hideturtle()
    turtles.penup()
    game_screen.penup()
game_screen.showturtle()

wn.listen()
wn.onkeypress(up,'Up')
wn.onkeypress(down,'Down')
wn.onkeypress(left,'Left')
wn.onkeypress(right,'Right')
wn.onkeypress(show,'\n')

segment=turtle.Turtle()
segment.speed(0)
segment.penup()

#Main loop
while True:
    game_screen.hideturtle()
    wn.update()   
    #The window updates everthing
    #touch border and fences
    
    #snake touches the food
    if snake.distance(food)<25:
        food_correction()
    
        #add score  
        pen.clear()
        score+=10
        if score>high_score:
            high_score=score
        pen.write('Score: {} High Score: {}'.format(score,high_score),align='center',font=('Arial',24,'normal'))

        #add body
        segment=turtle.Turtle()
        if snake.direction=='up' or snake.direction=='down':
            segment.shape(os.path.expanduser("~\Desktop\segment_y.gif"))
        else:
            segment.shape(os.path.expanduser("~\Desktop\segment_x.gif"))
        segment.speed(0)
        segment.penup()
        body.append(segment)                
     
    #Adding body in reverse order
    for i in range(len(body)-1,0,-1):
        body[i].goto(body[i-1].xcor(),body[i-1].ycor())
   
    if body==[]:
        body=[segment]
         #move body to head
    if len(body)>0 :     
        if snake.direction=="up":
            body[0].goto(snake.xcor(),snake.ycor()-22)
            segmenty()
            tail.goto(segment.xcor(),segment.ycor()-10)
        if snake.direction=="down":
            body[0].goto(snake.xcor(),snake.ycor()+22)
            segmenty()
            tail.goto(segment.xcor(),segment.ycor()+10)
        if snake.direction=="right":
            body[0].goto(snake.xcor()-22,snake.ycor())
            segmentx()
            tail.goto(segment.xcor()-10,segment.ycor())
        if snake.direction=="left":
            body[0].goto(snake.xcor()+22,snake.ycor())
            segmentx()
            tail.goto(segment.xcor()+10,segment.ycor())
    move()
    hit_border()
    #if head hits the body
    for segment in body:
        if segment.distance(snake) < 20:
           collision()      

turtle.done()
