import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from pandas import datetools as dtls
import os
print("From the below, choose a block whose Energy sum you want to predict: "+ str(os.listdir("./daily_dataset")))
block_name = input("Please enter the block name: ")
daily_block0 = pd.read_csv("daily_dataset/"+block_name)
print("From the below, choose a machine name whose Energy sum you want to predict: "+ str(list(set(list(daily_block0["LCLid"])))))
machine_name = input("Please enter the machine name: ")
single_machine_daily_block0 = daily_block0.loc[daily_block0['LCLid'] == machine_name]
single_machine_daily_block0 = single_machine_daily_block0.drop(['LCLid'], axis = 1)
single_machine_daily_block0 = single_machine_daily_block0[['day', 'energy_sum']]
single_machine_daily_block0 = single_machine_daily_block0.groupby(['day']).sum().reset_index()
single_machine_daily_block0['day'] = pd.to_datetime(single_machine_daily_block0['day'], format='%Y-%m-%d')
df = single_machine_daily_block0
mon = df['day']
temp= pd.DatetimeIndex(mon)
month = pd.Series(temp.month)
to_be_plotted  = df.drop(['day'], axis = 1)
to_be_plotted = to_be_plotted.join(month)
sns.barplot(x = 'day', y = 'energy_sum', data = to_be_plotted)
# plt.show()
df = df.set_index('day')
mod = sm.tsa.SARIMAX(df['energy_sum'], trend='n', order=(0,1,0), seasonal_order=(1,1,1,12))
results = mod.fit()
start_value= len(df)-40
end_value = len(df)
near_end_value = len(df)-10
df['forecast'] = results.predict(start = start_value, end= end_value, dynamic= True)  
df[['energy_sum', 'forecast']].plot(figsize=(12, 8))
plt.show()
def forcasting_future_days(df, no_of_days):
    df_perdict = df.reset_index()
    mon = df_perdict['day']
    mon = mon + pd.DateOffset(days = no_of_days)
    future_dates = mon[-no_of_days -1:]
    df_perdict = df_perdict.set_index('day')
    future = pd.DataFrame(index=future_dates, columns= df_perdict.columns)
    df_perdict = pd.concat([df_perdict, future])
    df_perdict['forecast'] = results.predict(start = near_end_value, end = near_end_value + no_of_days, dynamic= True)  
    df_perdict[['energy_sum', 'forecast']].iloc[-no_of_days - 12:].plot(figsize=(12, 8))
    plt.show()
    return df_perdict[-no_of_days:]
predicted = forcasting_future_days(df,100)
predicted