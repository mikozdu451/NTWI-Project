import matplotlib.pyplot as plt


results = {1: []} # to set

for i in range(1, 2):
    f = open("test1/DBSCAN_RESULTS_BIGGER.txt") #+ str(i) +".txt", "r") # to set
    for j in f.readlines():
        results[i].append(j.replace("\n", ""))


#print(results)

f = open("test1/finalresultBIGGER.txt", "a") # to set

for i in range(1, 50):
    #DBSCAN
    epsilon = float(i/10)
    #print(epsilon)
    for j in range(3, 400):
        min_samples = j
        to_check = str(epsilon) + " " + str(min_samples)
        if to_check in results[1]: #and to_check in results[2] and to_check in results[3] and to_check in results[4] and to_check in results[5]: # to set
            print(to_check)
            f.write(to_check + "\n")

f.close()
