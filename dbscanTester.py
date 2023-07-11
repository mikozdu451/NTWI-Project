import numpy as np
from sklearn.cluster import DBSCAN
import time

for test_number in range(1, 5):

    filename = "test" + str(1) +"/newPoints" + str(test_number) + ".txt" # to set
    f = open(filename, "r")
    dataForDBSCAN = []
    line_num = 0
    for line in f.readlines():
            dataForDBSCAN.append([float(line.split(' ')[0].replace('\n', '')), float(line.split(' ')[1].replace('\n', ''))])
            line_num += 1
    #print(dataForDBSCAN)
    f.close()
    print("PROCESS START")

    start_time = time.time()
    for i in range(1, 50): # to set
        #DBSCAN
        epsilon = float(i/10)
        #print(epsilon)
        for j in range(3, 400): # to set
            min_samples = j
            db = DBSCAN(eps=epsilon, min_samples=min_samples).fit(dataForDBSCAN)
            labels = db.labels_

            no_clusters = len(np.unique(labels) )
            no_noise = np.sum(np.array(labels) == -1, axis=0)

            # for i in range(len(dataForDBSCAN)):
            #     print(dataForDBSCAN[i][0], " ", dataForDBSCAN[i][1], " ", labels[i])

            # print('Estimated no. of clusters: %d' % no_clusters)
            # print('Estimated no. of noise points: %d' % no_noise)

            if no_clusters == 2 and no_noise != line_num and no_noise != 0: #nu_clusters == 2 represents 1 cluster and noise
                #print(epsilon, min_samples)
                f = open("test" + str(1) +"/DBSCAN_RESULTS" + str(test_number) + ".txt", "a") # to set
                f.write(str(epsilon) + " ")
                f.write(str(min_samples) + "\n")


            f.close()

    print("PROCESS FINISH")
    print("Execution time - " + str(time.time() - start_time) + "s")
