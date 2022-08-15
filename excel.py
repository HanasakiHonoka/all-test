#coding=utf-8
import xlrd

data = xlrd.open_workbook("D:\\biz\\companyEmployee_test2.xlsx")

names = data.sheet_names()
table = data.sheets()[0]
nrows = table.nrows
for i in range(0, 5):
    print(table.row_values(i))
print(nrows)
