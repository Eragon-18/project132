import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('data.csv')

m = df['Mass']
r = df['Radius']
g = df['Gravity']

# Mass vs Radius
plt.scatter(m, r)
plt.xlabel('Mass')
plt.ylabel('Radius')
plt.title('Mass vs Radius')
plt.show()

# Mass vs Gravity
plt.scatter(m, g)
plt.xlabel('Mass')
plt.ylabel('Gravity')
plt.title('Mass vs Gravity')
plt.show()