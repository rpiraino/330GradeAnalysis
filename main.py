
import os 
import DataParser as dp
import analyticEngine as ae
import textwrap
from textwrap import wrap
f = []
a = os.listdir('data')
#makes array for each group
for row in a:
    if ((".GRP")in row):
        f.append(row)
#goes through each group
for row in f:
    dp.comma_Check("data/" + row )
    rows = dp.csv_Reader("data/" + row )
    d , N = ae.letter_Graph(rows, row + ".pdf") #return PerClass, classNames
    a , b = dp.LtoN(rows) #return total_Count, perClass 
    M = ae.Ztest(a , b)
    dp.fromtext()
    ae.merging(row + ".pdf")
    os.remove("readme.txt")
    os.remove(row + ".pdf")
    os.remove("results.pdf")
