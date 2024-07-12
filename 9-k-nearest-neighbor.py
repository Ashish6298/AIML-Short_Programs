#KNN

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Load the dataset and split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(load_iris()["data"], load_iris()["target"], random_state=0)

# Initialize and train the KNeighborsClassifier
kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(X_train, y_train)

# Make predictions and calculate confusion matrix
prediction = kn.predict(X_test)
cm = confusion_matrix(y_test, prediction)

print("Confusion Matrix:\n", cm)
