import xlrd
path=input('请输入excel文件路径：')
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)
for row in range(sheet.nrows):
    print()
    for col in range(sheet.ncols):
        print('%7s'%sheet.row(row)[col].value,'\t',end='')