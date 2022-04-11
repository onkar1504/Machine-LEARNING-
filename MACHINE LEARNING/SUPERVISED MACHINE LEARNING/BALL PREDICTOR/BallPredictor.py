from sklearn import tree

def MarvellousML(weight,surface):

    ballfeatures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    
    Names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]


    clf =tree.DecisionTreeClassifier()

    clf = clf.fit(ballfeatures,Names)

    result =clf.predict([weight,surface])

    if result == 1:
        print("ur object looks likes tennis ball")
    elif result == 2:
        print("ur obj lokks like cricket ball")

def main():

    print("marvellous infosystem")

    print("enter thw weight of ur object")
    weight =input()

    print("what is the surface of ut object Rough or Smooth")
    surface = input()

    if surface.lower()== "Rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0
    else:
        print("wrong input")
        exit()

    MarvellousML(weight,surface)
    
if __name__ == "__main__":
       
    main()