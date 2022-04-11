import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

dataset = pd.read_csv("Mall_Customers.csv")
print(dataset.head())

print(dataset.info())
print(dataset.describe())

#extracting 2 features

X = dataset.iloc[:,[3,4]]
print(X)


#plotiing 2 features

plt.figure(figsize=(10,5))
plt.scatter(x = X['Annual Income (k$)'],y=X['Spending Score (1-100)'])
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

#implement KMEans

km = KMeans(n_clusters=3)
km.fit(X)

print(km)