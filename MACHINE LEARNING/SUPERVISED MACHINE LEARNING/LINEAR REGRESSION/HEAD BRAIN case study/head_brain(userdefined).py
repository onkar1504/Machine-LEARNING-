from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def MarvellousBrainPredictor():
    data = pd.read_csv("MarvellousHeadBrain (1) (1).csv")
    print("size of data",data.shape)
    print('_'*50)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    #least square method mean kadhycha x and y
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    
    n= len(X)

    numerator  = 0
    denominator =0
    
    #equation of line y=mX+c

    for i in range(n):
        numerator += (X[i]-mean_x)*(Y[i]-mean_y)
        denominator += (X[i]-mean_x)**2

    m = numerator/denominator

    c =mean_y -(m * mean_x)

    print("slope of line",m)
    print("Y interception of regression line",c)

    max_x =np.max(X)+100
    min_x = np.min(X)-100

    #display plotting above points

    x =np.linspace(min_x,max_x , n)
    
    y = m*x +c

    plt.plot(x,y,color="red",label="regresion line")
    plt.scatter(X,Y ,color="blue",label="scatter plot")
    
    plt.xlabel('head brain size in cm3')
    plt.ylabel("brain weight in gram")

    plt.legend()
    plt.show()

    print('_'*50)
    #findout goodness of fit R square
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = m*X[i] +c
        ss_t += (Y[i]-mean_y)**2
        ss_r += (y[i]- y_pred)**2
    print(ss_t,ss_r)
    r2 = 1 - (ss_t/ss_r) 
    print("R square is",r2)

def main():
    print('_'*50)
    print("Marveelous infosystem")
    print("Head brain case study user defined")
    print("Supervised machine learning")
    print("linear regression ")
    print('_'*50)

    MarvellousBrainPredictor()
if __name__ == "__main__":
    main()