# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 06:01:32 2018

@author: Tony
"""

import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from pandas import datetools as dtls
import matplotlib.pyplot as plt

path = r'C:\Users\Tony\Downloads\daily_dataset\summary\daily_dataset_summary.csv'

#def forecastFn(path):
    
df = pd.read_csv(path)
df['day'] = pd.to_datetime(df['day'], format='%Y-%m-%d')
df = df.set_index('day')
mod = sm.tsa.SARIMAX(df['total_consumption'], trend='n', order=(0,1,0), seasonal_order=(1,1,1,12))
results = mod.fit()
#print(results.summary())
#print(df.head())
df['forecast'] = results.predict(start = 735, end= 815, dynamic= True)  
#    df[['total_consumption', 'forecast']].plot(figsize=(12, 8))
#    plt.show()
    
#forecastFn(path)

def forcasting_future_days(df, no_of_days):
    df_perdict = df.reset_index()
    mon = df_perdict['day']
    mon = mon + pd.DateOffset(days = no_of_days)
    future_dates = mon[-no_of_days -1:]
    df_perdict = df_perdict.set_index('day')
    future = pd.DataFrame(index=future_dates, columns= df_perdict.columns)
    df_perdict = pd.concat([df_perdict, future])
    df_perdict['forecast'] = results.predict(start = 810, end = 810 + no_of_days, dynamic= True)  
    df_perdict[['total_consumption', 'forecast']].iloc[-no_of_days - 12:].plot(figsize=(12, 8))
    plt.show()
    return df_perdict[-no_of_days:]

predicted = forcasting_future_days(df,100)

print(predicted)