#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Calling numpy
import numpy as np


# In[2]:


#Creating an array list
vec=np.array([1,2,3,4])
vec


# In[6]:


#Creating a matrix
Matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
Matrix


# In[7]:


#Transpose of matrix
print(Matrix.T)


# In[8]:


#Square root
X=np.sqrt(19999)
X


# In[12]:


#Arranging 0 to 299
Vec1=np.arange(0,300)
Vec1


# In[13]:


#Arranging from 2 to 50 in 10 addition
Vec2=np.arange(2,50,10)
Vec2


# In[14]:


#Arranging 0 to 20 including these two numbers in 10 parts
Vec3=np.linspace(0,20,10)
Vec3


# In[15]:


#Arranging in row and columns
Vec3.reshape(5,2)


# In[16]:


#Creating matrix of 0 and 1 in 4*4
Mat3=np.ones([4,4])
Mat3


# In[17]:


Mat2=np.zeros([4,4])
Mat2


# In[18]:


#Creating matrix with 1 diagonaly
Mat4=np.eye(5)
Mat4


# In[22]:


Vec1=np.array([1,2,3,4])
Vec2=np.array([5,6,7,8])
print(Vec1)
print(Vec2)


# In[24]:


#Adding Vec1 and Vec2
print(Vec1+Vec2)


# In[26]:


Vec7=np.array(["orrange","mango","potato","orrange"])
#Printing the unique value
print(np.unique(Vec7))


# In[27]:


#Printing random in 5*5
rand_mat=np.random.rand(5,5)
rand_mat


# In[28]:


#Printing mean from above data
z=np.mean(rand_mat)
z


# In[29]:


#Printing minimum from above data
j=np.min(rand_mat)
j


# In[30]:


#Printing 20 random number
rand_vec=np.random.rand(20)
rand_vec


# In[31]:


#Resulting in true or false for a condition
print(rand_vec>0)


# In[32]:


#Printing the numbers greater than 0
print(rand_vec[rand_vec>0])


# In[ ]:




