# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:37:22 2018

@author: Tony
"""
import glob
import pandas as pd
path =r'C:\Users\Tony\Downloads\daily_dataset\daily_dataset' # use your path

frame = pd.DataFrame()
list_ = []
def aggSumFn(path,grpByCol):
    allFiles = glob.glob(path + "/*.csv")
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0)
        
        list_.append(df)
    frame = pd.concat(list_)
    frame=frame.groupby([grpByCol])['energy_sum'].agg('sum')
    frame.to_csv(r'C:\Users\Tony\Downloads\daily_dataset\summary\daily_dataset_summary.csv',header = ['total_consumption'])
    print('completed')

aggSumFn(path,'day')
#