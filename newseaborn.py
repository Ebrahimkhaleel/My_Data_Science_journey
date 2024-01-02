import seaborn as sns
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