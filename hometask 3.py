# In[3]:


#1 
ns = [int(i) for i in input().split()]
n = 0
for i in range(len(ns)-1):
    if ns[i] > ns[i-1] and ns[i] > ns[i+1]:
        n += 1
print(n)


# In[8]:


# 2

minind, maxind = 0,0
ns = [int(i) for i in input().split()]

for i in range(len(ns)):
    if ns[i] > ns[maxind]:
        maxind = i
    if ns[i] < ns[minind]:
        minind = i
ns[maxind], ns[minind] = ns[minind], ns[maxind]
print(' '.join([str(i) for i in ns]))


# In[ ]:


# 3
ns = [int(i) for i in input().split()]
cnt = 0
for i in range(0,len(ns)-1):
    for j in range(i+1, len(ns)):
        if ns[i] == ns[j]:
            cnt += 1
print(cnt)


# In[ ]:


# 4
ns = [int(i) for i in input().split()]
for i in range(len(ns)):
    for j in range(len(ns)):
        if i != j and ns[i] == ns[j]:
            break
    else:
        print(ns[i], end=' ')


# In[ ]:


# 5
ns1 = [int(i) for i in input().split()]
ns2 = [int(i) for i in input().split()]
dups = [i for i in ns1 if i in ns2]
dups.sort()
print(' '.join([str(i) for i in dups]))


# In[7]:


# 6
ns = [int(i) for i in input().split()]
res = ['YES' if ns[i] in ns[:i] else 'NO' for i in range(len(ns))]
for i in res:
    print(i)


# In[10]:


# 7
import re
n = int(input())
words = []

for i in range(n):
    text = input().replace(';', '').replace('.', '').replace(',', '').replace('.', '')
    text_splitted = re.split('\s*', text)
    words.extend(text_splitted)
print(len(set(words)))


# In[15]:


#8
n = int(input())
d = dict()
for i in range(n):
    k, v = input().split()
    d[k] = v
last = input()
res = [k for k, v in d.items() if v == last] or [v for k, v in d.items() if k == last]
print(res[0])


# In[ ]:


#9
word_count = {}
n = int(input())

for i in range(n):
    for w in input().split():
        word_count[w] = word_count.get(w, 0) + 1
        
max_count = max(word_count.values())
word_count_sorted = sorted(word_count.items(), key=lambda x: (x[0]))

for i in word_count_sorted:
    if i[1] == max_count:
        print(i[0])
        break
    


# In[30]:


#10
from collections import defaultdict
from sys import stdin

def defualt_value(): return 0
clients = defaultdict(lambda: defaultdict(int))

for line in stdin.readlines():
    client, item, number = line.split()
    clients[client][item] += int(number)

clients_sorted = sorted(clients)

for client in clients_sorted:
    print(client)
    for item in sorted(clients[client]):
        print(item, clients[client][item])

