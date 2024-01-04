"""import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
print(tips.head())
#distplot
sns.displot(tips['total_bill'], kde=True, bins=30)
#joint plot
sns.jointplot(x='total_bill', y='tip',data=tips,kind='reg')
#pairplot
sns.pairplot(tips,hue='sex', palette='coolwarm')
plt.show()
#categorical plot
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as  np
tips=sns.load_dataset('tips')
sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)
sns.countplot(x='sex',data=tips)
sns.boxplot(x='day',y='total_bill',data=tips)
#VIOLINPLOT
sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)
plt.show()"""
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset('tips')
#STRIPPLOT
sns.stripplot(x='day',y='total_bill',data=tips,hue='sex',jitter=True,dodge=True)
plt.show()