#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Write a Python program to print "Hello Python"?


# In[10]:


a="Hello Python"
print("Hello Python")

2-Write a Python program to do arithmetical operations addition and division.?
# In[11]:


a=23
b=12
c=a+b
print("addition:",c)


# In[12]:


e=30
f=5
g=e/f
print("division:",g)

3-Write a Python program to find the area of a triangle?
# In[7]:


a=float(input("enter the length of first side"))
b=float(input("enter the length of second side"))
c=float(input("enter the length of third side"))


s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("\narea of tringle is",area)

4-Write a Python program to swap two variables?
# In[8]:


def swap_variables(a, b):
    a, b = b, a
    return (a, b)

x = 5
y = 10
x, y = swap_variables(x, y)
print("x =", x)
print("y =", y)

5-Write a Python program to generate a random number?
# In[9]:


import random

# Generate a random number between 1 and 100 (inclusive)
random_number = random.randint(1, 100)

print("Random number:", random_number)


# In[ ]:





# In[ ]:




