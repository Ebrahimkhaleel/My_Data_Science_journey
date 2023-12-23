import pandas as pd 
import matplotlib.pyplot as plt


df=pd.DataFrame({
    'day':[1,2,3,4,5,6,7,8],
    'temp':[47,67,73,75,20,30,40,47]
})
df.set_index('day', inplace=True)

v=[1,2,3,4,5,6,7,8]
h=[47,67,73,75,20,30,40,47]
print(len(v))
print(len(h))
plt.plot(v,h, color='red',linestyle='dashed')
plt.xlabel('day')
plt.ylabel('Temperature')
plt.title('Tempreture accross Asia')
plt.show()

