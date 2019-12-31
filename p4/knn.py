import pandas as pd
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

dataTest= pd.read_csv("test.csv")

f= open("train.csv","r")



def str_column_to_float(dataset, column):
    for r in dataset:
        r[column] = float(r[column].strip())

def str_column_to_int(dataset, column):
    class_values = [r[column] for r in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
        print('[%s] => %d' % (value, i))
    for r in dataset:
        r[column] = lookup[r[column]]
    return lookup


def euclideanDistance(insta1, insta2, length):
    mdista = 0
    for x in range(2,length):
        mdista += pow((float(insta1[x]) - float(insta2[x])), 2)
    return math.sqrt(mdista)

def getNeighbors(trainingSet, testInsta, k):
    mdista = []
    length = len(testInsta) -1
    for x in range(len(trainingSet)):
        mdist = euclideanMDista(testInsta, trainingSet[x], length)
        mdista.append((trainingSet[x], dist))
    mdista.sort(key=operator.itemgetter(1))
    
    neighbors = []
    for x in range(k):

        neighbors.append(mdista[x][0][20])

    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1),  reverse=True)
    return sortedVotes[0][0]


def normalize_dataset(dataset, minmax):
    for r in dataset:
        for i in range(len(r)):
            r[i] = (r[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

print ('Test set: ' + repr(len(testSet)))

print ('Train set: ' + repr(len(trainingSet)))



y_coordinate = []
k = 10

k_neighbors_price_ranges = []

for x in range(len(testSet)):
    k_neighbors_price_range = getNeighbors(trainingSet, testSet[x], k)

    k_neighbors_price_ranges.append(k_neighbors_price_range)

for j in range(1, k + 1):
    predictions = []
    print("k: ", j)
    for i in range(len(k_neighbors_price_ranges)):

        result = getResponse(k_neighbors_price_ranges[i][0:j])
        predictions.append(result)

    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + str(accuracy) + "%\n")

    y_coordinate.append(accuracy)

num_neighbors = 10
n_folds = 4

test_file = 'lab4/test.txt'

train_file = 'lab4/train.txt'

test_dataset = load_csv(test_file)[1:]

dataset = load_csv(train_file)[1:]


for i in range(len(test_dataset[0])-1):
    str_column_to_float(test_dataset, i)

test_converter = str_column_to_int(test_dataset, len(test_dataset[0])-1)


f = plt.figure()

plt.plot(range(1, 11),y_coordinate,color='blue',
 linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)

f.savefig("plot.pdf")
plt.show()


