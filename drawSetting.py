import math
import turtle
import os
import random

store_setting = [[]] #Used to store position of randomly generated map and pig location for user-retries.
def start_from(x,y): #shortcut
  t.penup()
  t.goto(x, y)
  t.pendown()
def draw_tree(xposition):
  start_from(x, 0)
  t.pencolor("brown")
  stem = random.randint(80, 150) #Randomly chooses the size of the stem
  t.color("Sienna")
  t.begin_fill()
  #Draws tree stem
  t.setheading(90)
  for i in range(2):
    t.forward(stem)
    t.right(90)
    t.forward(20)
    t.right(90)
  t.end_fill()
  t.setheading(0)
  t.goto(x+10,stem-10) #Randomly chooses the size of the leaves and draws the leaves
  t.color("green")
  t.begin_fill()
  t.circle(random.randint(40, 60))
  t.end_fill()
def draw_pig(x):
  start_from(x, -20)
  t.fillcolor("pink")
  #t.pencolor()
  t.begin_fill()
  t.forward(10)
  t.left(90)
  t.forward(30)
  t.backward(20)
  t.right(90)
  t.forward(8)
  t.left(90)
  t.forward(20)
  t.right(90)
  t.backward(18)
  t.left(90)
  t.backward(30)
  t.forward(30)
  t.right(90)
  t.forward(60)
  t.backward(18)
  t.right(90)
  t.forward(20)
  t.left(90)
  t.forward(8)
  t.right(90)
  t.forward(10)
  t.backward(30)
  t.forward(30)
  t.left(90)
  t.forward(10)
  t.left(90)
  t.forward(50)
  t.right(90)
  t.circle(20)
  t.backward(58)
  t.right(90)
  t.forward(20)
  t.pencolor("black")
  t.end_fill()
def draw_map():
  t.speed(0)
  t.fillcolor("brown")
  t.begin_fill()
  t.forward(400)
  t.right(90)
  t.forward(400)
  t.right(90)
  t.forward(2300) #Changes to hill or flatland (The smaller the number the bigger the hill)
  t.right(90)
  t.forward(250)
  t.right(90)
  t.forward(250)
  t.end_fill()
  for i in range(3):
    draw_tree(i*70 + random.randint(0,30))
  draw_pig(Pig_location)
def draw_thrower():
  arm_length = 40
  leg_length = 35

  def reset():
    t.pu()
    t.setpos(-180,0)
    t.pd()


  #draw a stickman

  reset()

  #head
  t.seth(90)
  t.fd(5)
  t.rt(90)
  t.circle(20)

  reset()

  #arm 1
  t.seth(150)
  t.fd(arm_length/2)
  t.rt(20)
  t.fd(arm_length/2)

  reset()

  #arm 2
  t.seth(100)
  t.fd(arm_length/2)
  t.lt(20)
  t.fd(arm_length/2)

  reset()

  #leg 1
  t.seth(270)
  t.fd(25)
  t.seth(230)
  t.fd(leg_length/2)
  t.lt(20)
  t.fd(leg_length/2)

  reset()

  #leg 2
  t.seth(270)
  t.fd(25)
  t.seth(310)
  t.fd(leg_length/2)
  t.rt(40)
  t.fd(leg_length/2)

def draw_stickman(posx, posy):
  arm_length = 35
  leg_length = 35

  def reset():
    t.pu()
    t.setpos(posx,posy)
    t.pd()


  #draw a stickman

  reset()

  #head
  t.seth(45)
  t.fd(15)
  t.rt(45)
  t.circle(10)

  reset()

  #arm 1
  t.seth(40)
  t.fd(arm_length/2)
  t.rt(25)
  t.fd(arm_length/2)

  reset()

  #arm 2
  t.seth(25)
  t.fd(arm_length/2)
  t.lt(25)
  t.fd(arm_length/2)

  reset()

  #leg 1
  t.seth(135)
  t.fd(25)
  t.seth(115)
  t.fd(leg_length/2)
  t.lt(4)
  t.fd(leg_length/2)

  reset()

  #leg 2
  t.seth(135)
  t.fd(25)
  t.seth(155)
  t.fd(leg_length/2)
  t.rt(5)
  t.fd(leg_length/2)
def set_the_stage(mode): #integer input: 1 for not yet thrown, 2 for thrown.
  draw_map()
  draw_thrower()
  if mode == 1:
    draw_stickman(-230,-10)
  if mode == 2:
    draw_stickman(power, 0) #power is the x coordinate of the stickman

