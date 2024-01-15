#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_prime(num1):
    factors = 0
    if num1 == 1:
        return 0
    elif num1 < 4:
        return num1
    elif num1%2 == 0:
        return 0
    elif num1 < 9:
        return num1
    elif num1%3 == 0 or num1%5 == 0 or num1%7 == 0:
        return 0
    elif factors == 0:
        for x in range(1,num1+1):
            if num1%x == 0:
                factors += 1
        if factors > 2:
            return 0
        else:
            return num1


# In[ ]:




