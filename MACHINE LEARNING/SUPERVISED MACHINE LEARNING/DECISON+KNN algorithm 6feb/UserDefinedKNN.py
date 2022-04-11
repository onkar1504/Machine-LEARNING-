from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return  distance.euclidean(a,b)

class MarvellousKNN():

    def fit(self,TrainingData ,TrainingTarget):
        self.Traingdata = TrainingData
        self.Traingtarget = TrainingTarget
    
    def predict(self,TestData):
        prediction=[]
        for row in TestData:
            label = self.closest(row)
            prediction.append(label)
        return prediction
    
    def closest(self,row):
        bestdistance = euc(row,self.Traingdata[0])
        bestindex =0
        for i in range(1,len(self.Traingdata)):
            dist =euc(row,self.Traingdata[i])

            if dist < bestdistance:
                bestdistance = dist
                bestdistance = i
            return self.Traingtarget[bestindex]


def MarvellousNeibour():
    border ="-"*50
    iris = load_iris()

    data =iris.data
    target = iris.target

    print(border)
    print("Actual Data Set")
    print(border)

    for i in range(len(iris.target)):
        print("ID:%d,TARGET:%s,FEATURES%s"%(i ,iris.data[i],iris.target[i]))
    print(border)
    print("Size of Actual Data set %d"%(i+1))
    
    data_tarin , data_test ,  target_train , target_test = train_test_split(data,target ,test_size=0.5)


    print(border)
    print("Training Data set")
    print(border)
    for i in range(len(data_tarin)):
        print("ID:%d,TARGET%s,FEATURES%s"%(i ,data_tarin[i],target_train[i]))
    print("Size of Training Data set %d"%(i+1))

    print(border)
    print("Test Data set")
    print(border)
    for i in range(len(data_test)):
        print("ID:%d,TARGET%s,FEATURES%s"%(i ,data_test[i],target_test[i]))
    print("Size of Test Data set %d"%(i+1))
    print(border)

    classifier = MarvellousKNN()

    classifier.fit(data_tarin , target_train)

    prediction = classifier.predict(data_test)

    Accuracy =accuracy_score(target_test,prediction)
    return Accuracy

def main():
    Accuracy = MarvellousNeibour()
    print("Acuuracy of USer defined decision tree classifier : ",Accuracy*100,"%")

if __name__ =="__main__":
    main()