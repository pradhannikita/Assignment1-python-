#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

# take input from the user
number = float(input("Enter a number: "))

# check if the number is positive, negative, or zero
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")


# In[9]:


#2. Write a Python Program to Check if a Number is Odd or Even?

# take input from the user
number = int(input("Enter a number: "))

# check if the number is odd or even
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# In[12]:


#3. Write a Python Program to Check Leap Year?

# take input from the user
year = int(input("Enter a year: "))

# check if the year is a leap year
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# In[14]:


#4. Write a Python Program to Check Prime Number?
# take input from the user
number = int(input("Enter a number: "))

# check if the number is prime
if number > 1:
    for i in range(2, int(number/2)+1):
        if (number % i) == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# In[15]:


#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# define a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# print all prime numbers in the interval 1-10000
for i in range(1, 10001):
    if is_prime(i):
        print(i)


# In[ ]:




