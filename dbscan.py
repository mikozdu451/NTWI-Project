import numpy as np
from sklearn.cluster import DBSCAN

f = open("test1/newPoints1.txt", "r")
dataForDBSCAN = []
for line in f.readlines():
        dataForDBSCAN.append([float(line.split(' ')[0].replace('\n', '')), float(line.split(' ')[1].replace('\n', ''))])
print(dataForDBSCAN)

#DBSCAN
epsilon = 3.5
min_samples = 14

db = DBSCAN(eps=epsilon, min_samples=min_samples).fit(dataForDBSCAN)
labels = db.labels_

no_clusters = len(np.unique(labels) )
no_noise = np.sum(np.array(labels) == -1, axis=0)

print('Estimated no. of clusters: %d' % no_clusters)
print('Estimated no. of noise points: %d' % no_noise)

for i in range(len(dataForDBSCAN)):
    print(dataForDBSCAN[i][0], " ", dataForDBSCAN[i][1], " ", labels[i])

