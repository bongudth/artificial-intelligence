from __future__ import print_function
import numpy as np
from scipy.spatial.distance import cdist

X = np.array([[0, 1, 1], [1, 1, 0], [2, 2, 0], [0, 1, 2], [2, 2, 2], [2, 3, 0]])
K = 3

class KMean:
    def __init__(self, k):
        self.K = k

    def kmeans_init_centers(self, X):
        return X[np.random.choice(X.shape[0], self.K, replace=False)]

    def kmeans_assign_labels(self, X, centers):
        D = cdist(X, centers)
        return np.argmin(D, axis=1)

    def kmeans_update_centers(self, X, labels):
        centers = np.zeros((self.K, X.shape[1]))
        for k in range(K):
            Xk = X[labels == k, :]
            centers[k, :] = np.mean(Xk, axis=0)
        return centers

    def has_converged(self, centers, new_centers):
        return (set([tuple(a) for a in centers]) == set([tuple(a) for a in new_centers]))

    def predict(self, X):
        centers = [self.kmeans_init_centers(X)]
        labels = []
        it = 0
        while True:
            labels.append(self.kmeans_assign_labels(X, centers[-1]))
            new_centers = self.kmeans_update_centers(X, labels[-1])
            if self.has_converged(centers[-1], new_centers):
                break
            centers.append(new_centers)
            it += 1
        self.centers = centers[-1]
        self.labels = labels[-1]
        return labels[-1]

kmean = KMean(K)
labels = kmean.predict(X)
for i in range(kmean.centers.shape[0]):
    print(f'Cac diem thuoc nhom {i + 1} la:', end=' ')
    for x in X[labels == i, :]:
        print(f'({x[0]}, {x[1]}, {x[2]})', end='; ')
    print(f'\nTrong tam cua nhom {i + 1} la : ({kmean.centers[i][0]}, {kmean.centers[i][1]}, {kmean.centers[i][2]})', end='\n')