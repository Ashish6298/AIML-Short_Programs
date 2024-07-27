#KNN

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
X_train, X_test, y_train, y_test = train_test_split(load_iris()["data"], load_iris()["target"], random_state=0)
kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(X_train,y_train)
prediction=kn.predict(X_test)
confusion_matrix(y_test,prediction)


# output
# array([[13,  0,  0],
#        [ 0, 15,  1],
#        [ 0,  0,  9]], dtype=int64)


