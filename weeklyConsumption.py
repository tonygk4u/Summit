# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 06:50:48 2018

@author: Tony
"""

import glob
import pandas as pd
import datetime
path =r'C:\Users\Tony\Downloads\daily_dataset\daily_dataset' # use your path

frame = pd.DataFrame()
list_ = []
def aggSumFn(path,grpByCol):
    allFiles = glob.glob(path + "/*.csv")
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0)
        
        list_.append(df)
    
    frame = pd.concat(list_)
    frame[grpByCol] = pd.to_datetime(frame['day'], format='%Y-%m-%d')
    frame[grpByCol] = pd.to_datetime(df[grpByCol]) - pd.to_timedelta(7, unit='d')
    frame=frame.groupby([pd.Grouper(key=grpByCol, freq='W-MON')])['energy_sum'].sum().reset_index().sort_values(grpByCol)
    frame.to_csv(r'C:\Users\Tony\Downloads\daily_dataset\summary\weekly_dataset_summary.csv',header = ['total_consumption'])
    print('completed')

aggSumFn(path,'day')
#

