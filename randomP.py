import random
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN

# parameters to generate the cluster to set
randomPointsNum = random.randint(500, 1000)
circle_radius = random.uniform(1, 7)
gaussianPointsNum = random.randint(500, 1000)
maxSize = 20

for j in range(1, 2): # to set
    offsetX = random.uniform(-(maxSize - circle_radius), maxSize - circle_radius)
    offsetY = random.uniform(-(maxSize - circle_radius), maxSize - circle_radius)
    theta = np.random.uniform(0.0, 2.0*np.pi, gaussianPointsNum)
    zero_to_one = np.random.uniform(0.0, 1.0, gaussianPointsNum)

    x = circle_radius * np.sqrt(zero_to_one) * np.cos(theta) + offsetX
    y = circle_radius * np.sqrt(zero_to_one) * np.sin(theta) + offsetY

    plt.plot(x, y, "ro", ms=2)
    for i in range(len(x)):
        x[i] = round(x[i], 4)
        y[i] = round(y[i], 4)
        #print(x[i], y[i])

    X = []
    Y = []

    for i in range(randomPointsNum):
        X.append(round(random.uniform(-maxSize, maxSize), 4))
        Y.append(round(random.uniform(-maxSize, maxSize), 4))


    plt.plot(X, Y, "bo", ms=2)
    plt.show()

    dataFodDBSCAN = []

    allX = []
    allY = []

    for i in x:
        allX.append(i)
    for i in X:
        allX.append(i)
    for i in y:
        allY.append(i)
    for i in Y:
        allY.append(i)

    f = open("newPoints"+ str(j) + ".txt", "w") # to set

    dbscanSample = np.array([])
    for i in range(len(allX)):
        line = str(allX[i]) + " " + str(allY[i]) + "\n"
        f.write(line)


        dataFodDBSCAN.append([allX[i], allY[i]])

    f.close()






