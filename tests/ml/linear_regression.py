import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rpy2.robjects as ro
import statsmodels.formula.api as smf
from patsy import dmatrices, dmatrix
from plotnine import aes, facet_wrap, geom_line, geom_point, ggplot
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.packages import data, importr
from sklearn.linear_model import LinearRegression


def load_df(df_name='sim1'):
  modelr = importr('modelr')
  df_env = data(modelr).fetch(df_name)
  with localconverter(ro.default_converter + pandas2ri.converter):
    df = ro.conversion.rpy2py(df_env[df_name])
  return df


# sim1
df = load_df()

# sklearn and statsmodels obviously give the same results
fit_sklearn = LinearRegression().fit(df[['x']], df['y'])
fit_smf = smf.ols('y ~ x', data=df).fit()

fit_smf.params - np.array([fit_sklearn.intercept_, fit_sklearn.coef_[0]])

x_grid = pd.DataFrame({'x': pd.unique(df['x'])})
max(abs(fit_smf.predict(x_grid) - fit_sklearn.predict(x_grid)))

# plotting predictions and residuals
df_pred = x_grid.assign(pred=fit_sklearn.predict(x_grid))
fig, axs = plt.subplots(1, 2, sharex=True)
axs[0].scatter(df['x'], df['y'])
axs[0].plot(x_grid, fit_sklearn.predict(x_grid), c='black')
axs[0].set_title('Observations and predictions')

df_fit = df.assign(pred=fit_sklearn.predict(df[['x']]),
                   res=lambda df: df.y - df.pred)
axs[1].scatter(df_fit['x'], df_fit['res'])
axs[1].set_title('Residuals')
fig.show()

# sim2
df = load_df('sim2')
fit_sklearn = LinearRegression().fit(
    pd.get_dummies(df, drop_first=True)[['x_b', 'x_c', 'x_d']], df['y'])
fit_smf = smf.ols('y ~ x', data=df).fit()
x_grid = pd.DataFrame({'x': pd.unique(df['x'])})
max(
    abs(
        fit_smf.predict(x_grid) -
        fit_sklearn.predict(pd.get_dummies(x_grid, drop_first=True))))

# plotting predictions and residuals
df_pred = x_grid.assign(pred=fit_smf.predict(x_grid))
fig, axs = plt.subplots(1, 2, sharex=True)
axs[0].scatter(df['x'], df['y'])
axs[0].scatter(df_pred['x'], df_pred['pred'], c='red')
axs[0].set_title('Observations and predictions')

df_fit = df.assign(pred=fit_smf.predict(df[['x']]),
                   res=lambda df: df.y - df.pred)
axs[1].scatter(df_fit['x'], df_fit['res'])
axs[1].set_title('Residuals')
fig.show()

# sim3
df = load_df('sim3')
fit_smf1 = smf.ols('y ~ x1 + x2', data=df).fit()
fit_smf2 = smf.ols('y ~ x1 * x2', data=df).fit()
y, x = dmatrices('y ~ x1 + x2', data=df)
fit_sklearn1 = LinearRegression(fit_intercept=False).fit(x, y)
x = dmatrix('~ x1 * x2', data=df)
fit_sklearn2 = LinearRegression(fit_intercept=False).fit(x, y)
max(abs(fit_smf1.predict(df) - fit_sklearn1.predict(x).squeeze()))
max(abs(fit_smf2.predict(df) - fit_sklearn2.predict(x).squeeze()))

# plotting predictions and residuals
x_grid = df[['x1', 'x2']].drop_duplicates()
df_pred = (x_grid.assign(pred1=fit_smf1.predict(x_grid),
                         pred2=fit_smf2.predict(x_grid)).melt(
                             id_vars=['x1', 'x2'],
                             var_name='model',
                             value_name='pred'))
(ggplot(df, aes(x='x1', y='y', color='x2')) + geom_point() +
 geom_line(mapping=aes(y='pred'), data=df_pred) + facet_wrap('~ model'))
df_res = (df[['x1', 'x2', 'y']].assign(
    pred1=fit_smf1.predict(df), pred2=fit_smf2.predict(df)).melt(
        id_vars=['x1', 'x2', 'y'], var_name='model',
        value_name='pred').assign(res=lambda df: df['y'] - df['pred']))
(ggplot(df, aes(x='x1', y='y', color='x2')) + geom_point() +
 geom_line(mapping=aes(y='pred'), data=df_pred) + facet_wrap('~ model'))

# splines
df = pd.DataFrame({
    'x': np.linspace(0, 3.5 * np.pi)
}).assign(y=lambda df: 4 * np.sin(df.x) + np.random.normal(size=50))

(ggplot(df, aes(x='x', y='y')) + geom_point())

y, x1 = dmatrices("y ~ bs(x, df=1, degree=1) - 1", df)
x3 = dmatrix("bs(x, df=3, degree=3) - 1", df)
x5 = dmatrix("bs(x, df=5, degree=5) - 1", df)
fit_sklearn1 = LinearRegression().fit(x1, y)
fit_sklearn3 = LinearRegression().fit(x3, y)
fit_sklearn5 = LinearRegression().fit(x5, y)

df_pred = (df.assign(pred1=fit_sklearn1.predict(x1),
                     pred2=fit_sklearn3.predict(x3),
                     pred5=fit_sklearn5.predict(x5)).melt(id_vars=['x', 'y'],
                                                          var_name='model',
                                                          value_name='pred'))
(ggplot(df, aes(x='x', y='y')) + geom_point() +
 geom_line(mapping=aes(y='pred'), data=df_pred, color='red') +
 facet_wrap('~ model'))
