# # META CODE
# from sklearn.multiclass import OneVsRestClassifier
# from xgboost import XGBClassifier
# from sklearn.preprocessing import MultiLabelBinarizer

# clf = OneVsRestClassifier(XGBClassifier(n_jobs=-1, max_depth=4))

# # You may need to use MultiLabelBinarizer to encode your variables from arrays [[x, y, z]] to a multilabel
# # format before training.
# mlb = MultiLabelBinarizer()
# y = mlb.fit_transform(y)

# clf.fit(X, y)

# logistic regression for multi-class classification using built-in one-vs-rest
from operator import mul

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.metrics import confusion_matrix
from sklearn.multiclass import OneVsOneClassifier  # , OneVsRestClassifier

# define dataset
X, y = make_classification(n_samples=1000,
                           n_features=10,
                           n_informative=5,
                           n_redundant=5,
                           n_classes=3,
                           random_state=1)

# define model
models = [
    OneVsOneClassifier(LogisticRegression()),
    LogisticRegression(multi_class='ovr'),
    LogisticRegression(multi_class='multinomial')
]

for model in models:
  model.fit(X, y)
  yhat = model.predict(X)
  print(confusion_matrix(y, yhat))

# define model
models = [
    OneVsOneClassifier(LogisticRegressionCV()),
    LogisticRegressionCV(multi_class='ovr'),
    LogisticRegressionCV(multi_class='multinomial')
]

for model in models:
  model.fit(X, y)
  yhat = model.predict(X)
  print(confusion_matrix(y, yhat))
