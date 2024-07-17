#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import plotly.express as p
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[7]:


df=pd.read_csv("G:/My Drive/NFLX.csv")


# In[8]:


df


# In[9]:


df.head()


# In[24]:


df.set_index('Date')


# In[26]:


df['Date']=pd.to_datetime(df['Date'])
df=df.set_index('Date')
df.head()


# In[29]:


sns.lineplot(x=df.index,y=df['Volume'],label='Volume')
plt.title("Volume of stock vs Time")
plt.grid()
plt.show()


# In[32]:


df.plot(y=['High','Close','Open'],title='Netflix stock pricre')
plt.grid()


# In[37]:


fig,(ax1,ax2,ax3)=plt.subplots(3,figsize=(15,10))
df.groupby(df.index.day).mean().plot(y='Volume',ax=ax1,xlabel='day')
df.groupby(df.index.month).mean().plot(y='Volume',ax=ax2,xlabel='month')
df.groupby(df.index.year).mean().plot(y='Volume',ax=ax3,xlabel='year')


# # dates with higest stock price

# In[39]:


df.sort_values(by='High',ascending=False).head(5)


# # dates with lowest stock price

# In[41]:


df.sort_values(by='Low',ascending=True).head(5)


# In[57]:


fig,axes=plt.subplots(nrows=1,ncols=2,sharex=True,figsize=(12,5))
fig.suptitle('High & Low values stock per period of time',fontsize=18)
sns.lineplot(ax=axes[0],y=df['High'],x=df.index,color='green')
sns.lineplot(ax= axes[1],y=df['Low'],x=df.index,color='red')

