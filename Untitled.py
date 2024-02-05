#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing useful libraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


#reading date 

df = pd.read_csv("Sales_Dataset.csv", encoding = "unicode_escape")


# In[3]:


#show first 5 rows

df.head()


# In[4]:


#finding rows and column or shape of data

df.shape


# In[5]:


# this provide us a brief discription about each columns of data 

df.info()


# In[6]:


#drop one or more columns

df.drop(['Status', 'unnamed1'], axis = 1, inplace = True)


# In[7]:


df.info()


# In[8]:


# total null values in columns

pd.isnull(df).sum()


# In[9]:


#Removing null values rows

df.dropna(inplace = True)


# In[10]:


df.shape


# In[11]:


#removing duplicate value rows 

df.drop_duplicates(inplace = True)


# In[12]:


df.shape


# In[13]:


# Change amount float to integer

df['Amount'] = df['Amount'].astype(int)


# In[14]:


df['Amount'].dtypes


# In[15]:


df.columns


# In[16]:


# Rename column 

df.rename(columns = {'Age Group': 'Age_Group'}, inplace = True)


# In[17]:


df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis
#  

# In[18]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[19]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men
# In[20]:


ax = sns.countplot(data = df, x = 'Age_Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


sales_age = df.groupby(['Age_Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age_Group',y= 'Amount' ,data = sales_age)

From above graphs we can see that most of the buyers are of age group between 26-35 yrs female
# In[22]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[23]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')

From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively*
# In[24]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[25]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# In[26]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[27]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')

From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector
# In[28]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[29]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')

From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category
# In[30]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# # Conclusion 
Married womens with age group 26-35 yrs from Uttar Pradesh, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products in Food, Clothing and Electronics category.