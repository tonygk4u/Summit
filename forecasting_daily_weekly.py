# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 06:01:32 2018

@author: Tony
"""

import pandas as pd

import statsmodels.api as sm

import matplotlib.pyplot as plt

path_day = r'C:\Users\353020\Back up\SmartMeter\summary\daily_dataset_summary.csv'

def forecastFn(path,field):
    
    df = pd.read_csv(path)
    df[field] = pd.to_datetime(df[field], format='%Y-%m-%d')
    df = df.set_index(field)
    mod = sm.tsa.SARIMAX(df['total_consumption'], trend='n', order=(0,1,0), seasonal_order=(1,1,1,12))
    results = mod.fit()
    return results,df

results_days,df_days = forecastFn(path_day,'day')
df_days['forecast'] = results_days.predict(start = 735, end= 815, dynamic= True)  
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
    df_perdict['forecast'] = results_days.predict(start = 810, end = 810 + no_of_days, dynamic= True)  
    df_perdict[['total_consumption', 'forecast']].iloc[-no_of_days - 12:].plot(figsize=(12, 8))
    plt.show()
    return df_perdict[-no_of_days:]

daily_predicted = forcasting_future_days(df_days,100)

#print(daily_predicted)


#-----weekly prediction

path_week = r'C:\Users\353020\Back up\SmartMeter\summary\weekly_dataset_summary.csv'

results_week,df_week = forecastFn(path_week,'week')
df_week['forecast'] = results_week.predict(start = 735, end= 815, dynamic= True)  

def forcasting_future_weeks(df, no_of_weeks):
    df_perdict = df.reset_index()
    mon = df_perdict['week']
    mon = mon + pd.DateOffset(weeks = no_of_weeks)
    future_dates = mon[-no_of_weeks -1:]
    df_perdict = df_perdict.set_index('week')
    future = pd.DataFrame(index=future_dates, columns= df_perdict.columns)
    df_perdict = pd.concat([df_perdict, future])
    df_perdict['forecast'] = results_week.predict(start = 810, end = 810 + no_of_weeks, dynamic= True)  
    df_perdict[['total_consumption', 'forecast']].iloc[-no_of_weeks - 12:].plot(figsize=(12, 8))
    plt.show()
    return df_perdict[-no_of_weeks:]

weekly_predicted = forcasting_future_weeks(df_week,10)
print(weekly_predicted)