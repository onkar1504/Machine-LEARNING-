# Below application is used to demonstrate the creation of Data Frames using Pandas library.
# There are multiple ways in which we can create Data Frames using Pandas

from operator import index
import pandas as pd
border  = "-"*50

print(border)
print("empty data frames")
dataframe = pd.DataFrame()
print(dataframe)

print(border)
print("dataframe with list")
data = [1,2,3,4,5]
dataframe = pd.DataFrame(data)
print(dataframe)

print(border)
print("dataframe with list")
data = [['ppa',4],['angular',3],['python',3]]
dataframe = pd.DataFrame(data,columns=['batches','duration'])
print(dataframe)

print(border)
data ={'batches':['ppa','lb','angular','python'],'duration':[4,3,3,3]}
dataframe = pd.DataFrame(data)
print(dataframe)

print(border)
data =[{'name':'ppa','duration':3,'fees':10500},{'name':'angular','duration':3,'fees':11500},{'name':'python','duration':3,'fees':15500}]
dataframe = pd.DataFrame(data)
print(dataframe)

print(border)
d= {'one':pd.Series([1,2,3],index=['a','b','c']),
    'two':pd.Series([1,2,3,4],index=['x','y','z','w'])}
df = pd.DataFrame(d)
print(df['one'])