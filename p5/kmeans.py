
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = open('data.txt', 'r')

next(data)

X = []
f = data.readlines()
for line in f:
    arr = line.rstrip().split(",")
    X.append([int(arr[0]), int(arr[1])])




def euclidian(a_dist, b_dist):
    dis = 0
    for w in range(len(x_dist)):
        dis += (a_dist[w] - b_dist[w]) ** 2
    dis = np.sqrt(dis)
    return dis

def random_centers(X , Z):
    merk = []
    point = np.random.randint(0, len(X))
    merk.append(X[point])
    dist = np.zeros(len(X))  
    for c in range(Z-1):
        for i in range(len(X)):
            dist[i] += euclidian(merk[len(merk)-1], X[i])
        point = np.argmax(dist)   
        merk.append(X[point])
    return merk




def main_kmeans(X, k, iter_num=100):
    updated_merk = random_merk(X, k)
    for lp in range(iter_num):
        cluster = []
        for i in range(k):
            cluster.append([])
        for i in range(len(X)):
            min_i = 0
            min_d = 999999
            for j in range(k):
                d = euclidian(updated_merk[j] ,X[i])
                if d < min_d:
                    min_i = j
                    min_d = d
            cluster[min_i].append(i)
        for i in range(k):
            if len(cluster[i]) != 0:
                updated_merk[i] = mean_function(X, cluster[i])
    return [cluster, updated_merk]

def mean_function(X, k):
    n = len(k)
    s = [0] * len(X[0])
    for i in range(n):
        for j in range(len(X[0])):
            s[j] += X[merk[i]][j]
    for j in range(len(X[0])):
        s[j] /= n
    return s




def call_function(result, centers,  ax, k):
    for i in range(len(result)):
        lst = []
        col = color[i]
        for j in range(len(result[i])):
            lst.append(X[result[i][j]])
        lst = pd.DataFrame(lst)
        ax.scatter(lst[0], lst[1], alpha=0.275, cmap='viridis')
        ax.scatter(centers[i][0], centers[i][1], marker=markers[i], color="black", alpha=1.0, s= 100)

        ax.set_title('result when k = ' + str(k))


color = ['red', 'goldenrod', 'maroon', 'cyan', 'darkorange']

for k in range(K):
    data=X[X["Cluster"]==k+1]
    klr.scatter(data["SPEND"],data["INCOME"],c=color[k])
klr.xlabel('Spend')
klr.ylabel('Income')

klr.show()
