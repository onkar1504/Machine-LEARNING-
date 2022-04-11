# Below application is used to demonstrates operations on Excel file using Pandas Library.
import pandas as pd

border="-"*50

print(border)
excelfile = "Marvellous.xlsx"
batches = pd.read_excel(excelfile)
print(batches.head())

print(border)
batches_sheet1 = pd.read_excel(excelfile,sheet_name=0,index_col=0)
print(batches_sheet1.head())

print(border)
xlsx =pd.ExcelFile(excelfile)
batches_sheets =[]

for sheet in xlsx.sheet_names:
    print(sheet)
    batches_sheets.append(xlsx.parse(sheet))

batches = pd.concat(batches_sheets)
print(batches)
