
from sklearn.datasets import load_iris 

iris = load_iris()

print("featuers name of iris dataset")
print(iris.feature_names)                #fetaures ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

print("target names of iris dataset")
print(iris.target_names)                       #['setosa' 'versicolor' 'virginica']       labels


for i in range(len(iris.target)):
    print("id:%d,features%slabels:%s" % (i,iris.data[i],iris.target[i]))