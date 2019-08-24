# Implement commen models and let data decide which model to use
# 1. logistic regression
#

from sklearn.linear_regression import LogisticRegression
from sklearn.datasets import load_iris

def logistic_model(penalty, C, X_train, y_train, fit_intercept=True,
	X_val=None, y_val=None, random_state=None):
	"""Fit logistic regression model.

	Args:
	  penalty: str,'l1','l2','elasticnet','none'.
	  C: float, Inverse of regularization strength
	  X_train: features of train data.
	  y_train: outcomes of train data.
	  fit_intercept: bool, optional (default=True)
	  X_val: validation data.
	  y_val: validation data.
	  random_state: random state. 
	"""


