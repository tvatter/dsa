import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from patsy import dmatrices
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (confusion_matrix, plot_confusion_matrix,
                             plot_roc_curve, roc_auc_score, roc_curve)
from statsmodels.discrete.discrete_model import Logit, MNLogit
from statsmodels.stats.outliers_influence import \
    variance_inflation_factor as vif

# https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model_sm.Logit.html
# https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model_sm.MNLogit.html
# https://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model_sm.LogitResults.html
# https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model_sm.MultinomialResults.html
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

# from statsmodels.datasets import get_rdataset
# df = get_rdataset('mtcars').data
# from patsy import dmatrices
# y, x = dmatrices('am ~ C(cyl) + hp + wt', df)
# model_sm = Logit(y, x)
# from statsmodels.formula.api import logit
# model_sm_formula = logit('am ~ C(cyl) + hp + wt', df)

# Read data and create model matrix
df = pd.read_csv("https://stats.idre.ucla.edu/stat/data/binary.csv")
y, x = dmatrices('admit ~ gre + gpa + C(rank)', df)

# Fit, summarize, predict with sm/sk
model_sm = Logit(y, x)
fit_sm = model_sm.fit()
fit_sm.summary()
model_sk = LogisticRegression(fit_intercept=False, solver='liblinear', C=1e9)
fit_sk = model_sk.fit(x, np.ravel(y))
score_sm = fit_sm.predict()
classes_sm = (score_sm > 0.5).astype(int)
score_sk = fit_sk.predict_proba(x)
classes_sk = fit_sk.predict(x)

# Confusion matrix
fit_sm.pred_table()
confusion_matrix(y, classes_sm)
confusion_matrix(y, classes_sk)
plot_confusion_matrix(fit_sk, x, y)
plt.show()

# ROC/AUC
roc_auc_score(y, score_sm)

fpr, tpr, thresholds = roc_curve(y, score_sm)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(fpr, tpr)
plot_roc_curve(fit_sk, x, y, ax=ax2)
fig.show()

# Let's now look at some data with multicolinearity
x, y = load_breast_cancer(return_X_y=True)
print([vif(x, i) for i in range(x.shape[1])])

model_sk = LogisticRegression(solver='liblinear')
fit_sk = model_sk.fit(x, y)
roc_auc_score(y, fit_sk.predict_proba(x)[:, 1])

fig, (ax1, ax2) = plt.subplots(1, 2)
plot_confusion_matrix(fit_sk, x, y, ax=ax1)
plot_roc_curve(fit_sk, x, y, ax=ax2)
fig.show()
