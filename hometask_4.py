# In[5]:


get_ipython().run_line_magic('load_ext', 'pycodestyle_magic')
get_ipython().run_line_magic('pycodestyle_on', '')


# In[32]:


# ex 1
# Дано действительное положительное число a и целоe число n.
# Вычислите a в степени n


a = float(input())
n = int(input())


def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(power(a, n))


# In[24]:


# ex 2
# Напишите функцию вычисляющие НОД для множества пар чисел


pairs = [int(j) for j in input().split()]
pairs_splitted = [pairs[i:i+2] for i in range(0, len(pairs), 2)]
res = []

for p in pairs_splitted:
    a = p[0]
    b = p[1]
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    res.append(a + b)

print(res)


# In[31]:


# ex 3
# Напишите функцию, которая в зависимости от выбора пользователя
# вычисляет площадь круга, прямоугольника или треугольника.

from math import pi


def circle_area(r):
    return pi * r * r


def rectange_area(a, b):
    return a * b


def triangle_area(a, h):
    return 0.5 * a * h


figure = input('Введите фигуру: К - круг, Т - триугольник, П - прямоугольник ')

if figure == 'К':
    r = int(input('Введите радиус '))
    print(circle_area(r))
if figure == 'Т':
    a = int(input('Введите сторону треугольника '))
    h = int(input('Введите высоту треугольника '))
    print(triangle_area(a, h))
if figure == 'П':
    a = int(input('Введите первую сторону прямоугольника '))
    b = int(input('Введите вторую сторону прямоугольника '))
    print(rectange_area(a, b))


# In[30]:


# ex 4
# Напишите функцию, которая на вход принимает квадратную матрицу
# Вычисляет сумму элементов главной или побочной диагонали

n = int(input('Введите размер квадратной матрицы '))
matrix = [[int(input()) for i in range(n)] for j in range(n)]


def diagonal_sum(sum_type):
    sum_main, sum_collateral = 0, 0
    for i in range(n):
        for j in range(n):
            if i == j:
                sum_main += matrix[i][j]
            if j == n-1-i:
                sum_collateral += matrix[i][j]
    if sum_type == 'Г':
        return sum_main
    if sum_type == 'П':
        return sum_collateral


sum_type = input("Введите вид суммы матрицы. Главная - Г, Побочная - П ")
print(diagonal_sum(sum_type))


# In[29]:


# ex 5


import matplotlib.pyplot as plt
import numpy as np


def f(x):
    if -5 <= x <= 5:
        return x * x
    elif x < -5:
        return 2 * abs(x) - 1
    elif x > 5:
        return 2 * x


x = np.linspace(-10, 10)
y = np.array([f(x[i]) for i in range(len(x))])

plt.plot(x, y)
plt.grid(True)
plt.show()
