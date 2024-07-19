#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np


# In[3]:


df=pd.read_csv("G:\My Drive\Titanic.csv")


# In[4]:


df


# # 1.how many rows and columns are in it ?

# In[5]:


rows, columns = df.shape


# In[8]:


print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")


# # 2.in which class category more numbers of women died percentage from that class ? 

# In[9]:


women = df[df['Sex'] == 'female']


# In[10]:


women


# In[11]:


class_death_percentage = women.groupby('Pclass')['Survived'].apply(lambda x: (x == 0).mean() * 100)


# In[12]:


class_death_percentage


# In[13]:


class_death_percentage.idxmax()


# In[14]:


class_death_percentage.max()


# # 3.the oldest passenger was a male or a female ?

# In[15]:


oldest_passenger = df.loc[df['Age'].idxmax()]


# In[16]:


oldest_passenger


# In[17]:


oldest_gender = oldest_passenger['Sex']
oldest_age = oldest_passenger['Age']


# In[19]:


oldest_gender


# In[20]:


oldest_age


# In[18]:


print(f"The oldest passenger was a {oldest_gender} aged {oldest_age} years.")


# # 4. find the name of the oldest survived female ?

# In[21]:


survived_females = df[(df['Sex'] == 'female') & (df['Survived'] == 1)]


# In[22]:


survived_females


# In[23]:


oldest_survived_female = survived_females.loc[survived_females['Age'].idxmax()]


# In[24]:


oldest_survived_female


# In[25]:


oldest_female_name = oldest_survived_female['Name']
oldest_female_age = oldest_survived_female['Age']


# In[26]:


oldest_female_name


# In[27]:


oldest_female_age 


# In[28]:


print(f"The oldest surviving female passenger was {oldest_female_name}, aged {oldest_female_age} years.")


# # 5. find the deatails of the youngest passenger who could not survived ?

# In[30]:


non_survivors = df[df['Survived'] == 0]


# In[31]:


non_survivors 


# In[32]:


youngest_non_survivor = non_survivors.loc[non_survivors['Age'].idxmin()]


# In[33]:


youngest_non_survivor


# In[35]:


youngest_passenger_details = youngest_non_survivor


# In[36]:


youngest_passenger_details


# # 6. overall, what percentage of passengers survived the disaster ?

# In[38]:


number_of_survivors = df['Survived'].sum()


# In[39]:


number_of_survivors


# In[40]:


total_passengers = df.shape[0]


# In[41]:


total_passengers 


# In[42]:


survival_percentage = (number_of_survivors / total_passengers) * 100


# In[43]:


survival_percentage


# In[44]:


print(f"Overall, {survival_percentage:.2f}% of passengers survived the disaster.")


# # 7.which sex of passengers were more on the board ?

# In[45]:


passenger_counts_by_sex = df['Sex'].value_counts()


# In[46]:


passenger_counts_by_sex 


# In[50]:


number_of_males = passenger_counts_by_sex['male']
number_of_females = passenger_counts_by_sex['female']


# In[51]:


number_of_males


# In[52]:


number_of_females


# In[55]:


print(f"There were more male passengers on board the Titanic.")
print(f"Number of male passengers: {number_of_males}")


# # 8.which passenger has less average age ticket class wise ?

# In[56]:


average_age_by_class = df.groupby('Pclass')['Age'].mean()


# In[57]:


average_age_by_class


# In[58]:


lowest_average_age_class = average_age_by_class.idxmin()
lowest_average_age = average_age_by_class.min()


# In[59]:


lowest_average_age_class 


# In[60]:


lowest_average_age 


# In[61]:


print(f"The ticket class with the lowest average age is Class {lowest_average_age_class}.")
print(f"The average age in this class is {lowest_average_age:.2f} years.")


# # 9.the highest fare belonged to which class ?

# In[62]:


highest_fare_row = df.loc[df['Fare'].idxmax()]


# In[63]:


highest_fare_row 


# In[64]:


highest_fare_class = highest_fare_row['Pclass']
highest_fare = highest_fare_row['Fare']


# In[65]:


highest_fare_class


# In[66]:


highest_fare


# In[67]:


print(f"The highest fare belonged to Class {highest_fare_class}.")
print(f"The fare was {highest_fare:.2f} currency units.")


# # 10. which class has more number of passengers ?

# In[68]:


passenger_counts_by_class = df['Pclass'].value_counts()


# In[69]:


passenger_counts_by_class


# In[70]:


most_passengers_class = passenger_counts_by_class.idxmax()
most_passengers_count = passenger_counts_by_class.max()


# In[71]:


most_passengers_class 


# In[72]:


most_passengers_count


# In[73]:


print(f"Class {most_passengers_class} had the most passengers.")
print(f"Number of passengers in this class: {most_passengers_count}")


# In[ ]:




