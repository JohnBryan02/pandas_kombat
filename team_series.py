#!/usr/bin/env python
# coding: utf-8

# # Team Pandas Series

# In[10]:


# imports

import pandas as pd
import numpy as np


# ---

# ### Kombat 1: How to create a series from a list, numpy array and dict?
# 
# Create a pandas series from each of the items below: a list, numpy and a dictionary

# In[18]:


# Input

mylist = list('abcde')
myarr = np.arange(5)
mydict = dict(zip(mylist, myarr))


# In[23]:


test_list = ['a','b','c','d']
df1 = pd.DataFrame.from_records(mylist)
df1


# In[28]:


print(myarr)
df2 = pd.DataFrame(np.array(myarr))
df2


# In[33]:


df3 = pd.DataFrame(mydict)
df3


# In[17]:


df2 = pd.DataFrame.from_records(myarr)
df2


# In[5]:


# Fight!!!

df1 = mylist
df1 = pd.df1.

df1 = []


# In[ ]:


df2


# In[ ]:


df3


# In[4]:


# Output

print(mylistserie)
print(myarrserie)
print(mydictserie)


# ---

# ### Kombat 2: How to get the items of series A not present in series B?
# 
# From ser1 remove items present in ser2.

# In[39]:


# Input

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])


# In[41]:


# Fight
res = ser1[~ps1.isin(ps2)]
res


# In[37]:


# Output

ser1


# ---

# ### Kombat 3: How to bin a numeric series to 10 groups of equal size?
# 
# Bin the series ser into 10 equal deciles and replace the values with the bin name.

# In[42]:


# Input

ser = pd.Series(np.random.random(20))


# In[50]:


# Fight
result = pd.cut(ser,bins = bins,labels = False)


# In[10]:


# Output

print(ser)
print(rank)


# ---

# ### Kombat 4: How to convert a numpy array to a dataframe of given shape?
# 
# Reshape the series ser into a dataframe with 7 rows and 5 columns.

# In[51]:


# Input

ser = pd.Series(np.random.randint(1, 10, 35))


# In[56]:


ser


# In[59]:


res = ser.values.reshape(7,5)


# In[61]:


# Fight

#print(ser)
serpd = pd.DataFrame(res,
                    index=[0,1,2,3,4,5,6],
                    columns=['0','1','2','3','4'])
print(serpd)
print(type(serpd))


# In[62]:


# Output

serpd


# ---

# ### Kombat 5: How to create a TimeSeries starting ‘2022-01-02’ and 10 weekends (sundays) after that, having random numbers as values?

# In[63]:


# Input

time_series = pd.Series(np.random.randint(1, 10, 10))


# In[69]:


# Fight

time_series
 
time_series = {"2022-01-02": time_series[0], "2022-01-09": time_series[1], "2022-01-16": time_series[2], "2022-01-23": time_series[3], "2022-01-30": time_series[4], "2022-02-06": time_series[5], "2022-01-16": time_series[6]}
time_series2= pd.DataFrame(time_series)


# In[70]:


# Output

time_series2


# ---

# ### Kombat 6: How to change column values when importing csv to a dataframe?
# 
# Import the boston housing dataset, but while importing change the 'medv' (median house value) column so that values < 25 becomes ‘Low’ and > 25 becomes ‘High’.

# In[72]:


# Input

url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'


# In[74]:


# Fight
def converter(cell):
    if cell > 25:
        return 'High'
    if cell < 25:
        return 'Low'

df = pd.read_csv(url)
df


# In[75]:


converter(df['medv'])


# In[19]:


# Solution

df


# ---

# ### Kombat 7: How to get the nrows, ncolumns, datatype, summary stats of each column of a dataframe?
# 
# Get the number of rows, columns, datatype and summary statistics of each column of the Cars93 dataset.

# In[77]:


# Input

url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'


# In[83]:


#Fight

data = pd.read_csv(url)
data.info()


# In[22]:


# Output

print(numberofcols)
print(numberofrows)
print(datatype)
print(summarystats)


# In[ ]:





# ---

# ### Kombat 8: How to slice a DataFrame by column value?
# 
# Get every Chevrolet car with a EngineSize lower than 3.0 from the Cars93 dataset.

# In[23]:


# Input

url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'


# In[24]:


# Fight



# In[25]:


# Output

chevy


# ---

# # FINISH HIM!!!
