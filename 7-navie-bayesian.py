
#naive
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
msg = pd.read_csv('naivetext.csv', names=['message', 'label'])
msg['labelnum'] = msg.label.map({'pos': 1, 'neg': 0})
X = msg.message
y = msg.labelnum
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.30, random_state=42)
count_vect = CountVectorizer()
Xtrain_dtm = count_vect.fit_transform(Xtrain)
Xtest_dtm = count_vect.transform(Xtest)
clf = MultinomialNB().fit(Xtrain_dtm, ytrain)
predicted = clf.predict(Xtest_dtm)
print("The dimension of the dataset:", msg.shape)
print(X)
print(y)
print("\nThe total no of training data:", ytrain.shape)
print("\nThe total no of testing data:", ytest.shape)
print("\nThe words or tokens in the text document:\n")
print(count_vect.get_feature_names_out())
print("\nAccuracy of classifier:", metrics.accuracy_score(ytest, predicted))
print("\nConfusion matrix:")
print(metrics.confusion_matrix(ytest, predicted))
print("\nThe value of precision:", metrics.precision_score(ytest, predicted))
print("\nThe value of recall:", metrics.recall_score(ytest, predicted))
