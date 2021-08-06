import matplotlib.pyplot as plt
import numpy as np
from numpy.random import default_rng
from scipy.spatial import KDTree
# from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.neighbors import KNeighborsRegressor


# A simple implementation based on scipy's KDTree
def knn(x, y, x_new=None, k=5):

  if x_new is None:
    x_new = x

  tree = KDTree(x)
  fit = np.empty(x_new.shape)
  for i, xx in enumerate(x_new):
    _, idx = tree.query(xx, k=k)
    fit[i] = np.mean(y[idx])
  return fit


# Sample some data from y = sin(3 pi x) + eps
# with x ~ U(0,1), eps ~ N(0,1)
rng = default_rng(12345)
n = 10**2
sd = 0.5
eps = rng.normal(size=(n, 1), scale=sd)
x = rng.uniform(size=(n, 1))
y = np.sin(3 * np.pi * x) + eps

# Plot fits for different values of k
x_new = np.expand_dims(np.linspace(0, 1, 200), 1)
neigh = KNeighborsRegressor()
# plt.plot(x, y, 'o', label='data')
for k in [3, 15, 50]:
  knn_scipy = knn(x, y, x_new, k)
  neigh.set_params(n_neighbors=k)
  neigh.fit(x, y)
  knn_sklearn = neigh.predict(x_new)
  print(max(abs(knn_scipy - knn_sklearn)))
  plt.plot(x_new, knn_scipy, label='k = {}'.format(k))
plt.legend()
plt.show()

# Let's do so 10-fold cross-validation
cv_scores = []
for k in range(30):
  neigh.set_params(n_neighbors=k + 1)
  cv_scores.append(-np.mean(
      cross_val_score(neigh, x, y, cv=10, scoring='neg_mean_squared_error')))

plt.plot(list(range(1, 31)), cv_scores)
plt.axvline(x=np.argmin(cv_scores) + 1, color='red', label='optimal k')
plt.xlabel('k')
plt.ylabel('Cross-validated MSE')
plt.legend()
plt.show()

# Alternatively, using sklearn's GridSearchCV
neigh_grid = GridSearchCV(neigh, {'n_neighbors': list(range(1, 31))}, cv=10)
neigh_grid = neigh_grid.fit(x, y)
neigh_grid.best_params_
np.argmax(neigh_grid.cv_results_['mean_test_score']) + 1
