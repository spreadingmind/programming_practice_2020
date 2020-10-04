# In[93]:


import tkinter
import turtle
import math

def square(length):
    for i in range(4):       
        turtle.forward(length)
        turtle.left(90)

def left_circle(r, n):
    for i in range(n):
        turtle.forward(r)
        turtle.left(r)
        turtle.forward(r)
        turtle.left(r)

    
def semisquare(length):
    for i in range(2):       
        turtle.forward(length)
        turtle.left(90) 

def polygon(n, length):
    for i in range(n):
        turtle.right(360 / n) 
        turtle.forward(length) 


# In[2]:


# 2 S
turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.done()


# In[4]:


# 3 square
turtle.shape('turtle')
a = 50
square(a)
turtle.done()


# In[55]:


# 4 circle
radius = 10
resolution = 100
turtle.shape('turtle')
left_circle(radius, resolution)
turtle.done()


# In[7]:


# 5 concentric squares
turtle.shape('turtle')
n = 10
initial_length = 20
outset = 10
for i in range(1, n):
    square(initial_length)
    initial_length += 20
    turtle.penup()
    turtle.goto(turtle.xcor()-outset, turtle.ycor()-outset)
    turtle.pendown()
turtle.done()


# In[8]:


# 6 spider

turtle.shape('turtle')

n_paws = int(input())
length = 100

for i in range(n_paws):
    turtle.forward(length)
    turtle.stamp()
    turtle.back(length)
    turtle.left(360/n_paws)
turtle.done()


# In[9]:


# rose

for i in range(200):
    turtle.forward(1+i)
    turtle.right(50)
    turtle.forward(1+i)
    turtle.right(50)

turtle.done()    


# In[10]:


# 7 archimedian spiral
turtle.shape('turtle')
turtle.down()
for i in range(300):
    t = i / 20 * math.pi
    x = (1 + 2 * t) * math.cos(t)
    y = (1 + 2 * t) * math.sin(t)
    turtle.goto(x, y)
turtle.up()
turtle.done()


# In[11]:


# 8 square spiral
turtle.shape('turtle')
n = 20
initial_length = 20

for i in range(1, n):
    semisquare(initial_length)
    initial_length += 20
turtle.done()


# In[34]:


#9 10 n-side polygons

turtle.shape('turtle')
initial_length = 20
outset_x = 15
outset_y = 15


for i in range(3, 13):
    polygon(i, initial_length)
    initial_length += 30
    turtle.penup()
    turtle.goto(turtle.xcor()+outset_x, turtle.ycor()+outset_y)
    turtle.pendown()
turtle.done()



# In[74]:


# 10 flower from circles
turtle.shape('turtle')
for angle in range(0, 360, 60): 
    turtle.seth(angle)  
    turtle.circle(80)  

turtle.done()


# In[102]:


# 11 butterfly from circles

turtle.shape('turtle')
turtle.speed(10)
radius = 50
counter = 0

for angle in range(90, 3600, 180): 
    turtle.seth(angle)  
    turtle.circle(radius)
    counter += 1
    if counter % 2 == 0:
        radius += 10

    
turtle.done()


# In[121]:


# 12 spring

turtle.shape('turtle')
turtle.speed(10)
radius = 50
counter = 0
outset_x=5
for angle in range(90, 3600, 180): 
    turtle.seth(-90)  
    turtle.circle(radius, -180)
    turtle.goto(turtle.xcor()-outset_x, turtle.ycor())

    
turtle.done()


# In[149]:



