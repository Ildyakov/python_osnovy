
# coding: utf-8

# In[1]:


def fahr_to_cels(deg, bool): # deg это значение в цельсиях или фаренгейтах, bool это логическое значение перевода "1" из фаренгейта в цельсии, "-1" из цельсия в фаренгейты
    if bool == 1:
        return (deg - 32) * 5/9
    if bool == -1:
        return 9/5 * deg + 32


# In[2]:


def fibonacchi(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacchi(n - 1) + fibonacchi(n - 2)


# In[3]:


def square_square(a):
    return a**2


# In[4]:


def square_perimeter(a):
    return 4*a


# In[8]:


def avg_from3(a, b, c):
    return (a + b + c)/3


# In[14]:


def summa(x, y):
    return x + y
def func(f, a, b):
    return f(a, b)
v = func(summa, 10, 3)
print(v)


# In[15]:


def sum_of_squares(num):
    x = 0
    for i in range(1, num + 1):
        x += i ** 2
    return x


# In[16]:


print(sum_of_squares(6))

