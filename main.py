#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from plyer import notification
from time import sleep


# In[ ]:


while True:

    notification.notify(

        title = "Drink water, you dehydrated fool!",
        message = "You are important, just make sure you stay hydrated and drink enough water :). And yes, it is the passive-aggressive threat smile there :). 💧💦",
        app_icon = "http://localhost:8888/view/water.jpg",
        timeout = 10
    )

    sleep(60*60)


# In[ ]:




