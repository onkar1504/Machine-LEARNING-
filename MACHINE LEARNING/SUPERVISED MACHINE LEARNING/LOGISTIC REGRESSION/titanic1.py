import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import axis, figure,show
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

def marvellousTitaniclogistic():
    #Step 1  = load data
    titanic_data = pd.read_csv("titanic.csv")
   
    print("first % Entries from load dataset")
    print(titanic_data.head())
    print("number of passendgers are"+str(len(titanic_data)))

    #Step 2 = analyse data
    print("Visualization : Survived and non-survived passengers")
    figure()
    target = "Survived"

    countplot(data=titanic_data,x=target).set_title("marvellous infosytem = Survived and non-survived passengers ")
    show()

    print("Visualization : Survived and non-survived passengers based on Gender")
    figure()
    target = "Survived"

    countplot(data=titanic_data,x=target,hue="Sex").set_title("marvellous infosytem = Survived and non-survived passengers based on Gender ")
    show()

    print("Visualization : Survived and non-survived passengers based on passenger class")
    figure()
    target = "Survived"

    countplot(data=titanic_data,x=target,hue="Pclass").set_title("marvellous infosytem = Survived and non-survived passengers based on passenger class")
    show()

    print("Visualization : Survived and non-survived passengers based on Age")
    figure()
    titanic_data["Age"].plot.hist().set_title(" Survived and non-survived passengers based on Age")
    show()

    print("Visualization : Survived and non-survived passengers based on Fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title(" Survived and non-survived passengers based on Fare")
    show()

    #STEP 3 = DATA CLEANING

    # titanic_data.drop("zero",axis=1 ,inplace=True)
    print("first 5 enteries from loaded dataset after remooving zero colunmn")
    print(titanic_data.head(5))

    print("value of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("values of sex column after removing one field")
    Sex =pd.get_dummies(titanic_data["Sex"],drop_first=True)
    print(Sex.head(5))

    print("values of Pclass column after removing one field")
    Pclass =pd.get_dummies(titanic_data["Pclass"],drop_first=True)
    print(Pclass.head(5))

    print("values of data set after concating new columns")
    titanic_data = pd.concat([titanic_data,Sex,Pclass],axis=1)
    print(titanic_data.head(5))

    print("values of sex column after removing irrelevent columns")
    titanic_data.drop(["Sex","SibSp","Parch","Embarked"],axis=1 ,inplace= True)
    print(titanic_data.head(5))

    X= titanic_data.drop("Survived",axis=1)
    Y = titanic_data["Survived"]

    #STEP 4 = Data Training

    X_train , X_test ,Y_train , Y_test = train_test_split(X,Y,test_size=0.5)

    logmodel = LogisticRegression()

    logmodel.fit(X_train , Y_train)

    # data testing
    prediction = logmodel.predict(X_test)

    # STEP 5 = calculate Accuracy

    print("classification report of logistic regression is:")
    print(classification_report(Y_test,prediction))

    print("confusion matrix of logistic regreesion")
    print(confusion_matrix(Y_test,prediction))

    print("Accuracy")
    print(accuracy_score(Y_test,prediction))

def main():
    print("Marvellous Infosystem")
    
    print("supervised machine learning")

    print("logistic Regerssion titanic dataset ")
   
    marvellousTitaniclogistic()
if __name__ == "__main__":
    main()