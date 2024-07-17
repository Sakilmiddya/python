#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as p
import plotly.graph_objects as go


# In[2]:


data=pd.read_csv("G:/My Drive/Book_ipl22_ver_33.csv")


# In[3]:


data


# In[4]:


figure = p.bar(data, x=data["match_winner"],
            title="Number of Matches Won in IPL 2022")
figure.show()


# In[5]:


figure = p.bar(data, x = data["player_of_the_match"], 
                title="Most Player of the Match Awards")
figure.show()


# In[6]:


figure = p.bar(data, x = data["best_bowling"], 
                title="Best Bowling Figures")
figure.show()


# In[7]:


figure = p.bar(data, x=data["top_scorer"],
            title="Top Scorers in IPL 2022")
figure.show()


# In[8]:


figure = p.bar(data, x=data["top_scorer"], 
                y = data["highscore"], 
                color = data["highscore"],
            title="Top Scorers in IPL 2022")
figure.show()


# In[9]:


figure = p.bar(data, x=data["match_winner"], color = "venue",
            title="Teams Performance at diffrent Venues in IPL 2022")
figure.show()


# In[10]:


toss = data["toss_decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue','yellow']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decision')
fig.update_traces(hoverinfo='label+percent', 
                  textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=2)))
fig.show()


# In[11]:


data["won_by"] = data["won_by"].map({"Wickets": "Chasing", 
                                     "Runs": "Defending"})
won_by = data["won_by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['gold','lightgreen']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches Won By Defending Or Chasing')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# In[ ]:




