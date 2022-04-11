import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()


print("featuers name of iris dataset")
print(iris.feature_names)                #fetaures ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

print("target names of iris dataset")
print(iris.target_names)                       #['setosa' 'versicolor' 'virginica']       labels


#indices to removed elements
test_index=[1,51,101]

#training data to removed elements
train_target = np.delete(iris.target,test_index)
train_data = np.delete(iris.data,test_index,axis=0)

#testing data for testing on training data
test_target = iris.target[test_index]
test_data = iris.data[test_index]

#form  decision tree classifier

classifier = tree.DecisionTreeClassifier()

#applay training data   form tree
classifier.fit(train_data,train_target)

print("values removed from testing :")
print(test_data)

print("result of testing")
print(classifier.predict(test_data))

