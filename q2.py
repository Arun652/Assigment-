#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
days = [1,2,3,4,5,6,7]
sales_1 = [160,150,140,145,175,165,180] 
sales_2 = [70,90,160,150,140,145,175]  
plt.plot(days,sales_1,'r',linewidth=2,markersize=10)
plt.plot(days,sales_2,'b',linewidth=2,markersize=10)
plt.title("Q2")
plt.xlabel("Days")
plt.ylabel("Sales")


# In[ ]:




