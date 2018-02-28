#! /usr/bin/env python
#encoding=utf-8

import xlwt
import json
wb = xlwt.Workbook()
ws = wb.add_sheet("Students")
data = ''
with open(r'E:/PythonCaseWork/XML transfer to XLS/Students.txt','rb') as f:
    line = f.readline().decode().replace('\n','')
    while line :
        data = data + line
        line = f.readline().decode().replace('\t','')
        line = line.replace('\n','')
parsedData = json.loads(data)
for r in range(1,len(parsedData) + 1):
    for c in range(4):
        ws.write(r,c,parsedData[str(r)][c])
wb.save(r'E:/PythonCaseWork/XML transfer to XLS/output.xls')