import matplotlib.pyplot as plt

X = []
Y = []

f = open("test1/finalresultBIGGER.txt", "r") # to set
for line in f.readlines():
    X.append(float(line.split(" ")[0]))
    Y.append(int(line.split(" ")[1].replace("\n", "")))

print(X)
print(Y)

plt.plot(X, Y, "bo", ms=2)
plt.savefig('test1/finalgraphBIGGER.png') # to set
plt.show()

