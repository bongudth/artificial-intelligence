import numpy as np

class Kmeans:
    def __init__(self, X, K):
        self.X = X
        self.K = K
        
    def find_closest_centroids(self, centroids):
        m = len(self.X)
        c = np.zeros(m)
        for i in range(m):
            distances = np.linalg.norm(self.X[i] - centroids, axis=1)
            c[i] = np.argmin(distances)
        return c

    def compute_means(self, idx):
        m, n = self.X.shape
        centroids = np.zeros((self.K, n))
        for k in range(self.K):
            points_belong_k = self.X[np.where(idx == k)]
            centroids[k] = np.mean(points_belong_k, axis=0,)
        return centroids

    def find_k_means(self, max_iters=10):
        _, n = X.shape
        centroids = self.X
        for i in range(max_iters):
            idx = self.find_closest_centroids(centroids)
            centroids = self.compute_means(idx)

        return centroids, idx

# X = [[0, 3], [1, 4], [2, 0], [3, 0]]
# X = [[0, 4, 1], [1, 3, 3], [4, 0, 2], [3, 1, 4], [2, 1, 2], [2, 3, 4]]
X = [[0, 20, 5], [5, 15, 15], [20, 0, 10], [15, 5, 20], [10, 5, 10], [10, 15, 20]]
X = np.array(X)
k_means = Kmeans(X, 2)
idx = k_means.find_closest_centroids(X)
centroids = k_means.compute_means(idx)
centroids, idx = k_means.find_k_means()
print(centroids)
print(idx)