import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from numpy.core.numeric import zeros_like
from numpy.lib.shape_base import tile
from numpy.random import default_rng
# from sklearn.cluster import KMeans
# from sklearn.datasets import load_digits
from sklearn.neighbors import KDTree

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00'])

# Let's sample some data
rng = default_rng(12345)
n = 100
mean1 = (1, 2)
mean2 = (-1, -2)
cov = [[1, 0], [0, 1]]
x1 = rng.multivariate_normal(mean1, cov, size=n)
x2 = rng.multivariate_normal(mean2, cov, size=n)
x = np.vstack([x1, x2])
y = np.concatenate([np.ones(n), np.zeros(n)])
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=cmap_bold)
plt.show()


def kmeans(x, k, steps=3, plot=False):
  def update_means():
    means = [None] * k
    for kk in range(k):
      means[kk] = np.mean(x[clusters == kk, :], axis=0)
    return np.array(means)

  def update_clusters():
    tree = KDTree(means)
    return tree.query(x, 1, return_distance=False).ravel()

  # Random initialization
  clusters = rng.choice(a=k, size=x.shape[0], replace=True)
  means = update_means()

  if plot:

    # To plot the decision boundary
    h = 0.02
    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    x_grid = np.c_[xx.ravel(), yy.ravel()]
    zz = KDTree(means).query(x_grid, 1,
                             return_distance=False).reshape(xx.shape)
    # The subplots
    ncols = int(np.ceil((steps + 1) / 2))
    fig, ax = plt.subplots(nrows=2, ncols=ncols, sharex=True, sharey=True)
    # ax[0, 0].pcolormesh(xx, yy, zz, cmap=cmap_light, shading='auto')
    ax[0, 0].scatter(x[:, 0], x[:, 1], c=clusters, cmap=cmap_bold)
    ax[0, 0].scatter(means[:, 0], means[:, 1], color='black', s=100)
    ax[0, 0].set_xlim(xx.min(), xx.max())
    ax[0, 0].set_ylim(yy.min(), yy.max())
    ax[0, 0].set_title('Initialization')

  for step in range(steps):
    clusters = update_clusters()
    means = update_means()

    if plot:
      row = (step + 1) // ncols
      col = (step + 1) % ncols
      ax[row, col].pcolormesh(xx, yy, zz, cmap=cmap_light, shading='auto')
      ax[row, col].scatter(x[:, 0], x[:, 1], c=clusters, cmap=cmap_bold)
      ax[row, col].scatter(means[:, 0], means[:, 1], color='black', s=100)
      ax[row, col].set_title('Iteration {}'.format(step + 1))
      zz = KDTree(means).query(x_grid, 1,
                               return_distance=False).reshape(xx.shape)

  if plot:
    fig.show()

  return clusters, means


clusters, means = kmeans(x, 2, plot=True)
