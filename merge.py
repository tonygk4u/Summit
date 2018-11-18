# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:14:09 2018

@author: Tony.George
"""

import os
import glob
import pandas as pd

path = r'C:\Users\tony.george\Documents\docs\EYC3\Summit\hack\daily_dataset\daily_dataset'                    
all_files = glob.glob(os.path.join(path, "*.csv")) 
names = [os.path.basename(x) for x in glob.glob(path+'\*.csv')] 

df = pd.DataFrame()
for file_ in all_files:
    file_df = pd.read_csv(file_,sep=',', parse_dates=[0], infer_datetime_format=True,header=0 )
    file_df['file_name'] = os.path.basename(file_)
    df = df.append(file_df)

house_info = pd.read_csv(r'C:\Users\tony.george\Documents\docs\EYC3\Summit\hack\informations_households.csv')
#df.to_csv('out.csv')
    