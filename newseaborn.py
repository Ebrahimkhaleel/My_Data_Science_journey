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
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset('tips')
#STRIPPLOT
sns.stripplot(x='day',y='total_bill',data=tips,hue='sex',jitter=True,dodge=True)
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset('tips')
#SWARMPLOT(vilon plot and swarmplot can be combined)
sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset('tips')
#FACTORPLOT(deprecated to catplot with kind argument of bar)
sns.catplot(x='day',y='total_bill',data=tips, kind='bar')
plt.show()"""
#starting matrix plot 
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset('tips')
flights =sns.load_dataset('flights')

"""numeric_tips = tips.select_dtypes(include=['float64', 'int64'])

# Calculate correlation matrix for numerical columns
tc = numeric_tips.corr()
#heatmap
sns.heatmap(tc,annot=True)
plt.show()
fv=flights.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(fv,cmap='magma', linecolor='w', linewidths=0.5)

plt.savefig('heatmap.pdf')
plt.show()"""
fv=flights.pivot_table(index='month',columns='year',values='passengers')
sns.clustermap(fv, cmap='coolwarm', standard_scale=1)
#clustermap (basically shows simitarities between rows and column)
plt.savefig('clustermap.pdf')
plt.show()