#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_excel(r"C:\Users\kumak\Desktop\selfstudy\Customer Call List.xlsx")
df


# In[4]:


#first thing lets get rid of the obvious coloumn 
df = df.drop(columns=['Not_Useful_Column'])
df


# In[5]:


#now lets clean those unecessarly characters in this specific coloumn
df["Last_Name"]=df["Last_Name"].str.strip("/._")
df


# In[8]:


#getting rid of null values and storing it to another value so its easy to be used again withour ruinin the data
d2=df.fillna('')
d2


# In[9]:


#regardless that the data say  the same its bettes to conver it to harmonise and be easy ti beread
d2["Do_Not_Contact"] = d2["Do_Not_Contact"].str.replace('Yes','Y')

d2["Do_Not_Contact"] = d2["Do_Not_Contact"].str.replace('No','N')
d2


# In[12]:


#now inorder to get rid of this n/a its better to use replace since it didnt work to drop  it or use fillna
d3=d2.replace("N/a","")
d3


# In[20]:


#same process for this coloumn replace by one value regardless they have the same meaning
d3["Paying Customer"]=d3["Paying Customer"].str.replace('Yes','Y')
d3["Paying Customer"]=d3["Paying Customer"].str.replace('No','N')
d3


# In[30]:


#splitting the adress to be easy for the sale departemetn to read and have clear idea instead of goin one by one
d3[["Street_Address", "State", "Zip_Code"]]=d3["Address"].str.split(',',2, expand=True)
d3


# In[32]:


#after the previous action its seen the value none , hence its better to get rid of the null value again
data=d3.fillna('')
data


# In[44]:


#recap of how our data is like 
data


# In[46]:


#using indexing to go through all the rows to get rid of people that dont want to be called i t will be irrevelant data 
for x in data.index:
    if data.loc[x, "Do_Not_Contact"] == 'Y':
        data.drop(x, inplace=True)

data


# In[47]:


#i noticed there is a duplicated row so its better to just get rid of 
data.drop_duplicates()


# In[ ]:


#regardless that the costumer wanted to be called their numbers remain absent thus its better to remove them


# In[53]:


for x in data.index:
    if data.loc[x, "Phone_Number"] == '':
        data.drop(x, inplace=True)

data


# In[ ]:




