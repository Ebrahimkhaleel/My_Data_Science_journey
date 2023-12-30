"""import pandas as pd 
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
plt.plot(v,h, color='red',linestyle='dashed', markersize=6)
plt.xlabel('day')
plt.ylabel('Temperature')
plt.title('Tempreture accross Asia')
plt.show()

days = range(1,8) 

import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,5,11)
y=x**2
plt.subplot(1,2,1)
plt.plot(x,y,'y')

plt.subplot(1,2,2)
plt.plot(y,x,'g')
plt.show()"""
import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,5,11)
y=x**2

fig= plt.figure()
 
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(y,x)
axes1.set_title('large')
axes2.plot(x,y)
axes2.set_title('small')
plt.show()