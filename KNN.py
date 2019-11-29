#When doing statistics we deal with alot of data.
#This data can contain anomalies, so it is important to have methods in which we can detect these anomalies.


#A boxplot is a really simple, yet effective, technique when it comes to visually detecting anomalies in data.
#Here is the code example of a boxplot below:
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=random_data)


#K Nearest Neighbor is another way we can detect for anomlaies in our data.
#This a distance based algorithm that uses the euclidean distance.
#Here is the sampe code of K Nearest Neighbor: 
from sklearn.neighbors import NearestNeighbors
import numpy as np

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)
