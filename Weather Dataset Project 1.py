#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_csv (r"C:\Users\DELL\Desktop\Data Analysis with Python\1. Weather Data.csv")


# In[4]:


data


# In[5]:


data.head()


# In[7]:


data.shape


# In[8]:


data.index


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[14]:


data.nunique()


# In[15]:


data['Weather'].unique()


# In[16]:


data.count()


# In[18]:


data['Weather'].value_counts()


# In[19]:


data.info()


# 

# # Q. 1)  Find all the unique 'Wind Speed' values in the data.

# In[20]:


data.head(2)


# In[21]:


data['Wind Speed_km/h'].nunique()


# In[22]:


data['Wind Speed_km/h'].unique()


# # Q. 2) Find the number of times when the 'Weather is exactly Clear'.

# In[23]:


data.Weather.value_counts()


# In[27]:


data[data.Weather == 'Clear']


# In[28]:


data.groupby('Weather').get_group('Clear')


# # Q. 3) Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[29]:


data [data['Wind Speed_km/h'] == 4]


# # Q. 4) Find out all the Null Values in the data.

# In[31]:


data.isnull().sum()


# In[32]:


data.notnull().sum()


# # Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[41]:


data.rename(columns = {'Weather' : "Weather Condition"}, inplace = True)
data.head(2)


# # Q. 6) What is the mean 'Visibility' ?

# In[36]:


data.Visibility_km.mean()


# # Q. 7) What is the Standard Deviation of 'Pressure'  in this data?

# In[37]:


data.Press_kPa.std()


# # Q. 8) What is the Variance of 'Relative Humidity' in this data ?

# In[38]:


data['Rel Hum_%'].var()


# # Q. 9) Find all instances when 'Snow' was recorded.

# In[43]:


data['Weather Conditon'].value_counts()


# In[44]:


data[data['Weather Conditon'] == 'Snow']


# In[45]:


data[data['Weather Conditon'].str.contains('Snow')]


# # Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[47]:


data[(data['Wind Speed_km/h'] >24)& (data['Visibility_km'] ==25)]


# # Q. 11) What is the Mean value of each column against each 'Weather Condition ?

# In[48]:


data.groupby('Weather Conditon').mean()


# # Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition ?

# In[49]:


data.groupby('Weather Conditon').min()


# In[50]:


data.groupby('Weather Conditon').max()


# # Q. 13) Show all the Records where Weather Condition is Fog.

# In[51]:


data[data['Weather Conditon'] == 'Fog']


# # Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[53]:


data[(data['Weather Conditon'] == 'Clear') | (data['Visibility_km'] > 40)]


# # Q. 15) Find all instances when :A. 'Weather is Clear' and 'Relative Humidity is greater than 50'orB. 'Visibility is above 40'

# In[54]:


data[(data['Weather Conditon'] == 'Clear') & (data['Rel Hum_%'] > 50) |  (data['Visibility_km']>40)]


# In[ ]:




