import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def playpredictor(file):
    data =pd.read_csv(file)
    print(len(data))

    feature_names = ['Whether','Temprature']
    print("name of features",feature_names)

    wheter = data.Wether
    Temprature = data.Temperature
    play = data.Play 

    #create labelEncodeing
    le = preprocessing.LabelEncoder()

    #convert string labels into numbers(wether)
    wether_encoding = le.fit_transform(wheter)
    print(wether_encoding)

    #convert string labels into numbers(Temperature)
    temperature_encoding = le.fit_transform(Temprature)
    print(temperature_encoding)
    
    #convert string labels into numbers(Play)
    label =le.fit_transform(play)
    print(label)

    #combined wheter and temprature
    features = list(zip(wether_encoding,temperature_encoding))
    #step 3 Train data
    model = KNeighborsClassifier(n_neighbors=3)

    #train model using training sets
    model.fit(features,label)

    #step 4 test data
    predict =model.predict([[0,2]]) #0:overcast , 2:Mild
    print("prediction is",predict)

    if predict==1:
        print("u can play")
    elif predict == 0:
        print("not play")


def main():
    playpredictor ("MarvellousInfosystems_PlayPredictor.csv")
    Accuracy = playpredictor ("MarvellousInfosystems_PlayPredictor.csv")
    print("Acuuracy of decision tree classifier : ",Accuracy*100,"%")

    
if __name__ == "__main__":
    main()


