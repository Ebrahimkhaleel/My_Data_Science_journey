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
plt.show()
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

fig,ax=plt.subplots(nrows=1,ncols=2)
ax[1].plot(y,y)

plt.show()
import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(0,5,11)
y=x**2
fig,ax=plt.subplots(nrows=2,ncols=1,figsize=(8,2))

ax[0].plot(x,y)
ax[1].plot(y,x)
plt.tight_layout()
fig.savefig("new.pdf")
import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(0,5,11)
y=x**2
fig=plt.figure()
axes=fig.plot(x,x**2)
axes2=fig.plot(x,x**3)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import random 

random.seed(7)
days = range(1, 8)
mint = [random.randint(31, 40) for _ in days]
maxt = [random.randint(42, 50) for _ in days]
avgt = [random.randint(43, 48) for _ in days]


plt.plot(days,maxt,label="max")
plt.plot(days,mint,label="min")
plt.plot(days,avgt,label="avg")
plt.legend(loc="lower left", shadow=True)
plt.xlabel("days")
plt.ylabel("temperature")
plt.title("weather")
plt.grid()

plt.tight_layout()

plt.show()
#vertical bar chart
import numpy as np
import matplotlib.pyplot as plt
import random
random.seed()
company=['goog','amzn','khalil','dattech']
revenue=[random.randint(200,300) for _ in company]
profit=[random.randint(40,70) for _ in company]
xpos=np.arange(len(company))
plt.xticks(xpos,company)
plt.bar(xpos-0.2,revenue,label="Revenue",width=0.4)
plt.bar(xpos+0.2,profit,label="profit",width=0.4)
plt.legend()
plt.ylabel("Revenue")
plt.title("US Tech stocks")
plt.grid()
plt.show()
#horizontal barchart 
import numpy as np
import matplotlib.pyplot as plt
import random
random.seed()
company=['goog','amzn','khalil','dattech']
revenue=[random.randint(200,300) for _ in company]
profit=[random.randint(40,70) for _ in company]
ypos=np.arange(len(company))
plt.yticks(ypos,company)
plt.barh(ypos-0.2,revenue,label="Revenue", height=0.4)
plt.barh(ypos+0.2,profit,label="profit",height=0.4)
plt.legend()
plt.ylabel("Revenue")
plt.title("US Tech stocks")
plt.grid()
plt.show()
#HISTOGRAM
import matplotlib.pyplot as plt
import random

random.seed()
patient=['khalil','leslie','menz','fati','kexa','malam','hassan','saffiya']
blood_sugar_level=[random.randint(60,200)for _ in patient]
blood_sugar_levelw=[random.randint(40,180)for _ in patient]
plt.hist([blood_sugar_level,blood_sugar_levelw],orientation="horizontal", bins=[80,100,125,150], rwidth=0.95,label=["men","women"],color=['red','blue'])

plt.legend()
plt.xlabel('blood sugar level')
plt.ylabel("frequency")
plt.title("blood sugar analysis")
plt.show()"""

import matplotlib.pyplot as plt
import random

random.seed(1)
items=['rent','food','luxury','data','transportation']
amount=[random.randint(400,2500) for _ in items]

plt.pie(amount,labels=items,autopct='%0.2f%%',explode=[0,0,0,0.3,0.1])
plt.tight_layout()
plt.show()
