#!/usr/bin/env python
# coding: utf-8

# In[3]:


# pip install pyautogui


# In[23]:


import pyautogui, sys
import time

print(pyautogui.position())


# In[14]:


pyautogui.size()


# In[26]:


#　Click go back : (25, 61)  Click go right (70, 64)

time.sleep(5.0)
try:
    while True:
        pyautogui.click(25, 61, duration=1)
        pyautogui.click(70, 64, duration=1)
        # pyautogui.click(X,Y, duration=1) # THE PLACE TO CLICK THE CLASS 
        # pyautogui.click(X,Y, duration=1) # THE PLACE TO CLICK THE CHOOSE
        
except KeyboardInterrupt:
    print('\n')

