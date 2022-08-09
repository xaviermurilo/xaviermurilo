#!/usr/bin/env python
# coding: utf-8

# In[123]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# In[57]:


df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
df_bitcoin = pd.read_csv('Bitcoin Search Trend.csv')
df_bitcoin_price = pd.read_csv('Daily Bitcoin Price.csv')


# In[8]:


df_tesla.head()
df_unemployment.head()


# In[9]:


df_unemployment.head()


# In[18]:


df_bitcoin.head()


# In[23]:


df_bitcoin_price.head()


# ***whats is the shape ?***
# 

# In[11]:


df_unemployment.shape


# In[12]:


df_tesla.shape


# In[19]:


df_unemployment.shape


# In[24]:


df_bitcoin_price.shape


# In[13]:


df_unemployment.describe()


# In[14]:


df_tesla.describe()


# In[21]:


df_bitcoin.describe()


# In[25]:


df_bitcoin_price.describe()


# In[38]:


df_tesla.isna().sum()


# In[34]:


df_unemployment.isna().sum()


# In[56]:


df_bitcoin.isna().sum()


# In[58]:


df_bitcoin_price.isna().sum()


# In[63]:


df_bitcoin_price.dropna(inplace=True)


# ***convertion datatype***

# In[92]:


df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_bitcoin.MONTH = pd.to_datetime(df_bitcoin.MONTH)
df_bitcoin_price.DATE = pd.to_datetime(df_bitcoin_price.DATE)


# In[106]:


df_bitcoin_price.head()


# In[105]:


df_bitcoin.head()


# In[107]:


df_bitcoin_price_monthly = df_bitcoin_price.resample('M', on='DATE').last()


# In[135]:


plt.figure(figsize = (14,9), dpi=120)
ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()
 
ax1.set_ylabel('TSLA Stock Price', color = 'red')
ax2.set_ylabel('Search Trend')
 

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color = 'red')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH)



# In[179]:


plt.figure(figsize = (8,4), dpi=120)
ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()
 
ax1.set_ylabel('BTC Price', color = 'red')
ax2.set_ylabel('bitcoin search', color = 'BLUE')

plt.title('Bitcoin News Search vs Resampled Price')


ax1.plot(df_bitcoin_price.DATE, df_bitcoin_price.CLOSE, color = 'red', marker='o',markersize=2,linestyle='dashed',linewidth=2)
ax2.plot(df_bitcoin.MONTH, df_bitcoin.BTC_NEWS_SEARCH)


# In[184]:


plt.figure(figsize = (8,4), dpi=120)
ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()
 
ax1.set_ylabel('fred UE/rate', color = 'red')
ax2.set_ylabel('search', color = 'BLUE')

plt.title('unemployment benefits')


ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color = 'red', marker='o',markersize=2,linestyle='dashed',linewidth=2)
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH)


# In[183]:


df_unemployment_6montg_average = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()


# In[199]:


plt.figure(figsize = (8,4), dpi=120)
ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()
ax3 = ax1.twinx() 

ax1.set_ylabel('fred UE/rate', color = 'red')
ax2.set_ylabel('search', color = 'BLUE')
ax3.set_ylabel('average fred 6 months', color = 'green')

plt.title('unemployment benefits')


ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color = 'red', marker='o',markersize=2,linestyle='dashed',linewidth=2)
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH)
ax3.plot(df_unemployment.MONTH,df_unemployment_6montg_average.UE_BENEFITS_WEB_SEARCH, color='grey' )


# In[200]:


df_ue_2020 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')


# In[204]:


df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)


# In[207]:


plt.figure(figsize = (8,4), dpi=120)
ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()
 
ax1.set_ylabel('fred UE/rate', color = 'red')
ax2.set_ylabel('search', color = 'BLUE')

plt.title('unemployment benefits 2020')


ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, color = 'red', marker='o',markersize=2,linestyle='dashed',linewidth=2)
ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH)


# In[ ]:





# In[ ]:





# In[ ]:




