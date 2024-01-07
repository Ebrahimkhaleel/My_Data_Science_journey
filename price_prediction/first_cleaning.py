import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(20,10)
df=pd.read_csv('Bengaluru_House_Data.csv')
print(df.head(),df.shape)
print(df.groupby('area_type')['area_type'].agg('count'))
df1=df.drop(['area_type','society','availability','balcony'],axis='columns')
"""print(df1.head())"""
print(df1.isnull().sum())
