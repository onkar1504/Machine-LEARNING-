from sklearn.linear_model import LinearRegression
import pandas as pd

def MarvellousBrainPredictor():
    data = pd.read_csv("MarvellousHeadBrain (1) (1).csv")
    print("size of data",data.shape)
    print('_'*50)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    X =X.reshape(-1,1)
    
    n = len(X)

    reg  = LinearRegression()
    
    reg =reg.fit(X,Y)

    Y_pred = reg.predict(X)

    r2 = reg.score(X,Y)

    print("R square ",r2)

def main():
    print('_'*50)
    print("Marveelous infosystem")
    print("Head brain case study by sklearn")
    print("Supervised machine learning")
    print("linear regression ")
    print('_'*50)

    MarvellousBrainPredictor()
if __name__ == "__main__":
    main()
