# In[ ]:


#1
n=int(input())
hh = n%(24*60)//60
mm = n%(24*60)%60
print(hh, mm)


# In[10]:


#2
text = input()
n = int(input())
print('{}'.format(', '.join([text for i in range(n)])))


# In[29]:


#3
a,b,c = [int(i) for i in input().split()]
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)


# In[28]:


#4
v, t = [int(i) for i in input().split()]
print((v*t)%109)


# In[23]:


#5
n = int(input())
t = 1
s = 0
for i in range(1, n+1):
    t*=i
    s+=t
print(s)


# In[25]:


#6
max1, max2 = 0, 0
while True:
    x = int(input())
    if x == 0:
        break
    if  x > max1:
        max1 = max1
        max1 = x
    elif x > max2:
        max2 = x
print(max2)


# In[31]:


#7
l = input().split()
print('{}'.format(' '.join([l[i] for i in range(0, n, 2)])))


# In[35]:


#8
l = [i for i in input().split()]
print('{}'.format(' '.join([i for i in l if int(i)%2==0])))


# In[39]:


#9
from math import sqrt

def distance(x1,x2,y1,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))
