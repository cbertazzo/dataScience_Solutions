import pandas as pd
from openpyxl import *

df = pd.read_excel('File_1.xlsx','Sheet1')
print(df)
book = load_workbook('File_2.xlsx')
writer = pd.ExcelWriter('File_2.xlsx',engine='openpyxl')
writer.book = book
df.to_excel(writer,sheet_name='New Sheet')
writer.save()


