from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def  MarvellousAccuracyDecisionTree():
    #load data
    iris = load_iris()
   
    data = iris.data
    target = iris.target

    data_train ,data_test , target_train, target_test = train_test_split(data , target ,test_size=0.5)

    classifier = tree.DecisionTreeClassifier()

    classifier.fit(data_train,target_train)

    prediction = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test,prediction)
    return Accuracy

def MarvellousAccuracyKNeibour():
    #load data
    iris = load_iris()
   
    data = iris.data    
    target = iris.target

    data_train ,data_test , target_train, target_test = train_test_split(data , target ,test_size=0.5)

    classifier = KNeighborsClassifier()

    classifier.fit(data_train,target_train)

    prediction = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test,prediction)
    return Accuracy

def main():

    Accuracy = MarvellousAccuracyDecisionTree()
    print("Acuuracy of decision tree classifier : ",Accuracy*100,"%")

    Accuracy = MarvellousAccuracyKNeibour()
    print("Acuuracy of  knn classifier : ",Accuracy*100,"%")
if __name__ =="__main__":
    main()