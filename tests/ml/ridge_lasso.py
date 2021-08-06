# from plotnine import aes, facet_wrap, geom_line, geom_point, ggplot
from re import compile

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.linear_model import ElasticNet, Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_squared_error

# X, y, w = make_regression(n_features=10, coef=True)

models = [Ridge(), Lasso(max_iter=100000), ElasticNet(max_iter=100000)]

d = 10
n = 10
n_informative = 10  # Set this one to 2 to see how the Lasso can help !!
X, y, w = make_regression(n_samples=n,
                          n_features=d,
                          n_informative=n_informative,
                          coef=True,
                          random_state=1,
                          bias=3.5)

coefs = {}
errors = {}

n_alpha = 200
alphas = np.logspace(-6, 6, n_alpha)

# Train the model with different regularisation strengths
for model in models:
  coef = np.empty((n_alpha, d))
  error = np.empty((n_alpha, 1))
  for i, a in enumerate(alphas):
    model.set_params(alpha=a)
    model.fit(X, y)
    coef[i, :] = model.coef_
    error[i] = mean_squared_error(model.coef_, w)
  coefs[model] = coef
  errors[model] = error

# Plot the results
p = compile('^\w*')  # To extract the model's name
fig, axs = plt.subplots(3, 2, sharex=True)

for i, model in enumerate(models):
  axs[i, 0].plot(alphas, coefs[model])
  axs[i, 0].set_xscale('log')
  axs[i, 0].set_xlabel('alpha')
  axs[i, 0].set_ylabel('weights')
  axs[i, 0].set_title(
      '{} coefficients as a function of the regularization'.format(
          p.findall(str(model))[0]))

  axs[i, 1].plot(alphas, errors[model])
  axs[i, 1].set_xscale('log')
  axs[i, 1].set_xlabel('alpha')
  axs[i, 1].set_ylabel('error')
  axs[i, 1].set_title(
      '{} coefficient error as a function of the regularization'.format(
          p.findall(str(model))[0]))

fig.show()
