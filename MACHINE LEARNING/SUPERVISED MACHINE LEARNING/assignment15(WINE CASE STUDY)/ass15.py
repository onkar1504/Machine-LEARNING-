from sklearn import datasets
from sklearn.datasets import load_wine


def winpredict():
    wine = datasets.load_wine()
    print(wine.feature_names)
    print(wine.target_names)
    
    print(wine.data[0:5])

    print(wine.target)
def main():
    winpredict()
   

if __name__ == "__main__":
    main()