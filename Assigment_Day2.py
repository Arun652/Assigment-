#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.DataFrame(randn(10,4),columns=['a','b','c','d'])
df.plot.bar()
plt.title("bar Graph")


# In[ ]:




