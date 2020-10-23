#!/usr/bin/env python
# coding: utf-8

# In[37]:


get_ipython().run_line_magic('load_ext', 'pycodestyle_magic')
get_ipython().run_line_magic('pycodestyle_on', '')

import tkinter
import turtle as t
import math
from random import *


# In[40]:


# ex 1: random moves

directions = ['l', 'r', 'f', 'b']


def move_random():
    direction = choice(directions)  # choose random direction
    distance = randint(1, 30)  # generate random distance from 1 to 30
    angle = randint(1, 180)  # generate random angle from 1 to 180
    if direction == 'l':
        t.left(angle)
    if direction == 'r':
        t.right(angle)
    if direction == 'f':
        t.forward(distance)
    else:
        t.back(distance)


t.shape('turtle')

# make 100 random moves
for i in range(100):
    move_random()


t.done()


# In[43]:


# postcode digit functions

# wrapper for post digit func
def draw_post_digit(num_func):
    x, y = t.xcor(), t.ycor()
    t.penup()
    num_func(x, y)
    t.penup()
    t.forward(20)


def one(x, y):
    t.goto(x, y + 30)
    t.pendown()
    t.goto(x + 30, y + 60)
    t.goto(x + 30, y)
    t.penup()
    t.goto(x + 30, y)


def four(x, y):
    t.goto(x, y + 60)
    t.pendown()
    t.goto(x, y + 30)
    t.goto(x + 30, y + 30)
    t.goto(x + 30, y)
    t.goto(x + 30, y + 30)
    t.goto(x + 30, y + 60)
    t.goto(x + 30, y)


def zero(x, y):
    t.pendown()
    t.goto(x + 30, y)
    t.goto(x + 30, y + 60)
    t.goto(x, y + 60)
    t.goto(x, y)
    t.goto(x + 30, y)


def seven(x, y):
    t.pendown()
    t.goto(x, y + 30)
    t.goto(x + 30, y + 60)
    t.goto(x, y + 60)
    t.penup()
    t.goto(x + 30, y)


# In[45]:


# ex 2: postcode


postcode = '1 4 1 7 0 0'

# digit to digit func dict
digit_to_func = {
    0: zero, 1: one, 2: None, 3: None, 4: four,
    5: None, 6: None, 7: seven, 8: None, 9: None
    }

t.shape('turtle')

# generated list of digit funcs to draw given postcode
postcode = [
    draw_post_digit(digit_to_func[digit])
    for digit in (int(j) for j in postcode.split())
    ]
t.done()


# In[47]:


# ex 3: draw postcodes using digits "font" from file

t.shape('turtle')

with open('lab3_postcode_digits.txt') as file:
    for line in file:
        exec(line)
t.done()
