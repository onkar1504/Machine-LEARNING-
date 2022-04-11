import pandas as pd

from matplotlib import pyplot

from sklearn.metrics import classification_report


def Insurance(path):
    df = pd.read_csv(path)
    print("*"*50)
    #renaming exences column to boughtinsurance
    df.rename(columns={'expenses':'bought_insurance'},inplace=True)
    df.drop(['sex','bmi','children','smoker','region'],axis=1,inplace=True)
    print(df.head())
   
    
def main():
    print("marveloous infosystem")
    print("supervised machine learning")
    print("logistic regression on insurance set")

    Insurance("insurance.csv")

if __name__ == "__main__":
    main()