import pandas as pd


nigeria=pd.DataFrame({
    'city':['kano','zaria','jos'],
    'temp':[34,32,23],
    'humidity':[5,6,3]
})
southafrica=pd.DataFrame({
    'city':['capetown','durban','johannesburg'],
    'temp':[24,27,21],
    'humidity':[4,8,7]
})
print(nigeria)
print(southafrica)

df= pd.concat([nigeria,southafrica], keys=['nigeria', 'southafrica'])
print(df)