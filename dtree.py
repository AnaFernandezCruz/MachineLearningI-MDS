from sklearn import tree
from sklearn.preprocessing import OneHotEncoder

class DTree:
    x_train = None
    x_test = None
    y_train = None
    y_test = None
    clf = tree.DecisionTreeClassifier()

    def __init__(self, x_train, x_test, y_train, y_test):
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def train(self):
        enc = OneHotEncoder(handle_unknown='ignore') ## CHECK
        enc.fit(self.x_train) ## CHECK
        clf = self.clf.fit(self.x_train, self.y_train)
