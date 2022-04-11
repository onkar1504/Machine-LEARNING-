import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def winepredictor(file):
    data = pd.read_csv(file)

    featuresnames =['Alcohol','Malic acid','Ash','Alcalinity of ash']

    fnames = data[featuresnames]
    lnames = data.Class

    # print(fnames) 
    # print(lnames)

    fnames_train , fnames_test , lnames_train , lnames_test = train_test_split(fnames,lnames , test_size=0.3)
    print("size of tainning dataset",len(fnames_train))
    print("size of testing dataset",len(fnames_test))

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(fnames_train , lnames_train)

    # predict
    prediction = model.predict(fnames_test)
    # if prediction == 3:
    #     print("class 3")
    # elif prediction == 1:
    #     print("class 1")
    # else:
    #     print("class 2")

    print(prediction)

    Accuracy = accuracy_score(prediction,lnames_test)
    print("accuracy model is",Accuracy)
    
def main():

    winepredictor("WinePredictor.csv")
   

if __name__ == "__main__":
    main()