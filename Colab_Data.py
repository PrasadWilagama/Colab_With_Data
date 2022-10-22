# -*- coding: utf-8 -*-
"""IT20195366_Lab Test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lG6P4OIpRce4nPxB2UNYsyO-sKxQwo6M

Importing Packages
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import  StandardScaler

"""(1) Import the CSV file"""

movie_data=pd.read_csv("movie.csv")

"""(2) Explore the data

"""

movie_data

movie_data.head(5)

movie_data.describe

movie_data.info()

"""(3) Plot """

x=movie_data.gross

y=movie_data.votes

x

y

plt.scatter(movie_data['gross'],movie_data['votes'])

plt.plot(x, y, label="Budget")

mdata=movie_data.iloc[:,[4,5,6]]

mdata

"""(4) Optimal No of Clusters"""

wcss=[]
for i in range(1,11):
 kmeans = KMeans(i)
 kmeans.fit(mdata)
 wcss_iter = kmeans.inertia_
 wcss.append(wcss_iter)

movie_clusters = range(1,11)
plt.plot(movie_clusters,wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')

"""(5) Optimal No of Clusters
#2

(6) Data Set with Cluster No
"""

kmeans = KMeans(3)
kmeans.fit(mdata)

identified_clusters = kmeans.fit_predict(mdata)
identified_clusters

data_with_Clusters=movie_data.copy()
data_with_Clusters['Clusters']=identified_clusters
plt.scatter(data_with_Clusters['gross'],data_with_Clusters['votes'],c=data_with_Clusters['Clusters'],cmap='rainbow')