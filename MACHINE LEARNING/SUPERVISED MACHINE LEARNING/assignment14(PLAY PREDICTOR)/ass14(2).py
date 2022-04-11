import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def playpredictor(file):
    data =pd.read_csv(file)
    print("size of actual dataset",len(data))

    features = ['Wether','Temperature']
    print("name of features",features)

    x1 = data.Wether
    x2 =data.Temperature
    y = data.Play

    
    le = preprocessing.LabelEncoder()

    x = le.fit_transform(x1 )
    xx= le.fit_transform(x2)
    
    x = list(zip(x,xx))
    print(x)
    
    x_train , x_test , y_train ,y_test = train_test_split(x,y,test_size=0.5)
    print("size of training dataset",len(x_train))
    print("size of testing dataset",len(x_test))

    model = KNeighborsClassifier(n_neighbors=3)
    #train model
    model.fit(x_train , y_train)

    #predict / test model
    prediction = model.predict(x_test)
    
    Accuracy =  accuracy_score(y_test,prediction)
    return Accuracy

def main():
    Accuracy = playpredictor ("MarvellousInfosystems_PlayPredictor.csv")
    print("Acuuracy of decision tree classifier : ",Accuracy*100,"%")
    
if __name__ == "__main__":
    main()