#!/usr/bin/env python
# coding: utf-8
1. Write a Python program to convert kilometers to miles?
# In[1]:


km=float(input("enter your values in kms:"))
miles=(0.621371)*km
print(km,"kms will be", miles,"miles")

2-Write a Python program to convert Celsius to Fahrenheit?
# In[3]:


celsius=int(input("Enter temp in Celsius:"))
fahrenheit=(celsius*(9/5))+32
print("the converted value is",fahrenheit,"Fahrenheit")

3-Write a Python program to display calendar?
# In[15]:


import calendar

year=int(input("Enter the Year:"))

month=int(input("Enter the month:"))
print("\n",calendar.month(year,month))

4-Write a Python program to solve quadratic equation?
# In[1]:


import cmath

# a, b, and c represent the coefficients in the quadratic equation
a = float(input("Enter the value of coefficient a: "))
b = float(input("Enter the value of coefficient b: "))
c = float(input("Enter the value of coefficient c: "))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find the two solutions using the quadratic formula
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

# print the solutions
print(f"The solutions to the quadratic equation {a}x^2 + {b}x + {c} = 0 are {sol1} and {sol2}")


# In[ ]:


get_ipython().set_next_input('5. Write a Python program to swap two variables without temp variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[2]:


# initial values
a = 5
b = 7

# swap values
a, b = b, a

# print new values
print("a =", a)
print("b =", b)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




