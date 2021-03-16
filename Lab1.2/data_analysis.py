from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')

sheet = wb['Data']
col_a = sheet['A'][1:]
col_c = sheet['C'][1:]
col_d = sheet['D'][1:]

def getvalue(x): return x.value

list_a = list(map(getvalue, col_a))
list_c = list(map(getvalue, col_c))
list_d = list(map(getvalue, col_d))

pyplot.plot(list_a, list_c, label="Температура")
pyplot.plot(list_a, list_d, label="Активность")

pyplot.show()

