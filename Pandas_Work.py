#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing numpy and pandas
import numpy as np
import pandas as pd


# In[6]:


mylist=[5,4,6.1,7,8.3,2.7,3]
print(mylist)


# In[7]:


myarray=np.array(mylist)
print(myarray)


# In[8]:


myseries1=pd.Series(data=mylist)
print(myseries1)


# In[9]:


mylabels=['first','second','third','fourth','fifth','sixth','seventh']
myseries3=pd.Series(data=mylist,index=mylabels)
print(myseries3)


# In[10]:


myseries4=pd.Series([5.5,1.1,8.8,1.6],['first','second','third','fourth'])
print(myseries4)


# In[12]:


print(myseries4+myseries3) #NaN = Not a number


# In[22]:


#Combining two data sets to form one data frame
df1=pd.concat([myseries3,myseries4],axis=1,sort=False)
df1


# In[23]:


#Creating one data fram from random numbers
df2=pd.DataFrame(np.random.randn(5,5))
df2


# In[24]:


#Giving labels to the data drame
df3=pd.DataFrame(np.random.randn(4,4),index=['first row','second row','third row','fourth row'], columns=['first col','second col','third col','fourth col'])
df3


# In[25]:


#Accesing individual series in data frame
df3['second col']


# In[26]:


#accesing with the help of INDEX
df3.iloc[1]


# In[27]:


df3.loc[['fourth row','first row'],['second col','third col']]


# In[28]:


#logical indexing
df3<=0


# In[29]:


print(df3[df3>0])


# In[30]:


#Adding a column to the data frame
df3['fifth col']=np.random.randn(4,1)
df3


# In[31]:


#remove columns
df3.drop('first col',axis=1)


# In[32]:


#creating a new data frame after deleting a column
df4=df3.drop('first col',axis=1)
df4


# In[33]:


#remove index
df4.reset_index()


# In[34]:


#assign new names in index
df4['new name']=['this','is','the','row']
df4


# In[35]:


df4.mean()


# In[36]:


df4.median()


# In[13]:


#combining data frames
#there are 3 methods to combine data frames
#concat 
#join
#merge

import pandas as pd


# In[14]:


df8=pd.DataFrame({"customer":['101','102','103','104'],'category':['cat2','cat2','cat1','cat3'],'important':['yes','no','yes','yes'],'sales':[123,52,214,663]}) #index =[0,1,2,3]
df8


# In[15]:


df9=pd.DataFrame({"customer":['101','102','103','104'],'color':['yellow','green','green','blue'],'distance':[12,9,44,21],'sales':[123,214,663,331]})
df9


# In[19]:


pd.concat([df8,df9],axis=0,sort=True)


# In[20]:


pd.concat([df8,df9],axis=0,sort=True)


# In[42]:


#merger and join
#merger combines data frames using a colum's value to identify common entries
#join combines data frames using the index to identify common entries


# In[43]:


#outer merge is union
pd.merge(df8,df9,how='outer',on='customer')


# In[44]:


#inner merge is union
pd.merge(df8,df9,how='inner',on='customer')


# In[45]:


#left merge is just first on,but all columns
pd.merge(df8,df9,how='left',on='customer')


# In[46]:


#right merge is just first on,but all columns
pd.merge(df8,df9,how='right',on='customer')


# In[47]:


#join behaves kust like merge except instead of using values of columns to combine data frames it uses index labels
df10=pd.DataFrame({'Q1':[101,102,103],'Q2':[201,202,203]},index=['I0','I1','I2'])
df11=pd.DataFrame({'Q3':[301,302,303],'Q4':[401,402,403]},index=['I0','I2','I3'])
df10


# In[48]:


df11


# In[49]:


#outer, inner, left and right same as merge
df10.join(df11,how='outer')


# In[50]:


df10.join(df11,how='inner')


# In[51]:


df9.mean()


# In[52]:


df10.mean()


# In[53]:


df9['color'].unique()


# In[54]:


df9['color'].value_counts()


# In[55]:


df9.mode()


# In[56]:


#save and load dataframes
df9


# In[57]:


df9.to_csv('df9.csv',index=True)


# In[63]:


new_df9=pd.read_csv('df9.csv',index_col=0)
new_df9


# In[59]:


df9.to_excel('df9.xlsx',index=False,sheet_name='first sheet')
newer_df9=pd.read_excel('df9.xlsx',sheet_name='first sheet',index_col=0)
newer_df9


# In[ ]:





# In[ ]:




