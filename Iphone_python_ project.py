#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import plotly.express as p
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv("G:/My Drive/apple_products.csv")


# In[4]:


df


# In[5]:


df.isnull().sum()


# In[6]:


df.describe()


# # I Phone Sales Analysis In India

# In[7]:


rating=df.sort_values(by=["Star Rating"],ascending=False)
rating=rating.head(10)
print(rating["Product Name"])


# In[17]:


iphone=rating["Product Name"].value_counts()
labels = iphone.index
counts = rating["Number Of Ratings"]
figure = p.bar(rating,x=labels,y=counts,title="Number Of  higest Ratings")
figure.show()


# In[18]:


print(iphone)


# In[19]:


iphone=rating["Product Name"].value_counts()
labels = iphone.index
counts = rating["Number Of Reviews"]
figure = p.bar(rating,x=labels,y=counts,title="Number Of  higest Reviews")
figure.show()


# In[21]:


iphone=rating["Number Of Reviews"].value_counts()
print(iphone)


# In[32]:


figure = p.scatter(data_frame=df,x="Number Of Ratings",y="Sale Price",size="Discount Percentage",trendline="ols",
                 title="Relationship between sales price and number of ratings")
figure.show()


# In[44]:


figure = p.scatter(data_frame=df,x="Number Of Ratings",y="Discount Percentage",size="Sale Price",trendline="ols",
                 title="Relationship between Discount Percentage and number of ratings")
figure.show()


# In[ ]:




