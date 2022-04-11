from sklearn import datasets, metrics
from sklearn import svm
from sklearn.model_selection import train_test_split


def marvellousSVM():
    #load dataset
    cancer = datasets.load_breast_cancer()
    
    #print 13 features
    print("featuers of cancer datasets",cancer.feature_names)

    #print label type("mallignant",'bengin')
    print("labels of canceer dataset",cancer.target_names)

    #print data (featuers) shape
    print("shape of datasets",cancer.data.shape)

    #print top 5 recordds
    print("first 5 records")
    print(cancer.data[0:5])

    #print label ("0:mallignant",'1:bengin')
    print("target of datasets:",cancer.target)

    #split dataset into training and testing    
    x_train , x_test , y_train , y_test = train_test_split(cancer.data , cancer.target,test_size=0.3,random_state=109)

    #create svm classifier
    clf = svm.SVC(kernel='linear') 

    #traing model
    clf.fit(x_train , y_train)

    #predict
    y_predict = clf.predict(x_test) 

    #model accuracy
    print("accuracy of model is",metrics.accuracy_score(y_test,y_predict)*100)


def main():
    print("----marvellous Svm----")

    marvellousSVM()

if __name__ == "__main__":
    main()