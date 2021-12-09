import DataParser as dp
import csv
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pickle
import numpy as np
import sys
from fpdf import FPDF
import PyPDF2 
from PyPDF2 import PdfFileMerger
import math


def fig_bar(yvalues, xvalues, title=''):
    # create a new figure
    fig = plt.figure()

    # plot to it
    # yvalues = 0.1 + np.arange(len(ylabels))
    plt.bar(yvalues, xvalues, figure=fig, width=0.8, color=['green', 'red'])
    plt.grid(axis='y')
    # yvalues += 0.4
    # plt.yticks(yvalues, ylabels, figure=fig)
    if title:
        plt.title(title, figure=fig)


    return fig


def letter_Graph(array, gName):
    total_Count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x = 0
    CONSTANT = 2
    for row in array:
        if (str(array[x][CONSTANT]) == "A"):
            total_Count[0] = total_Count[0] + 1
        elif(str(array[x][CONSTANT]) == "A-"):
            total_Count[1] = total_Count[1] + 1
        elif(str(array[x][CONSTANT]) == "B+"):
            total_Count[2] = total_Count[2] + 1
        elif(str(array[x][CONSTANT]) == "B"):
            total_Count[3] = total_Count[3] + 1
        elif(str(array[x][CONSTANT]) == "B-"):
            total_Count[4] = total_Count[4] + 1
        elif(str(array[x][CONSTANT]) == "C+"):
            total_Count[5] = total_Count[5] + 1
        elif(str(array[x][CONSTANT]) == "C"):
            total_Count[6] = total_Count[6] + 1
        elif(str(array[x][CONSTANT]) == "C-"):
            total_Count[7] = total_Count[7] + 1
        elif(str(array[x][CONSTANT]) == "D"):
            total_Count[8] = total_Count[8] + 1
        elif(str(array[x][CONSTANT]) == "F"):
            total_Count[9] = total_Count[9] + 1
        x += 1
    C = 0
    x = 0
    for row in array:
        if (str(array[x][CONSTANT]) == r''):
            C += 1
        x += 1

    PerClass = [[0]*10 for _ in range(C)]

    c = -1
    x = 0

    for row in array:
        if (str(array[x][CONSTANT]) == "A"):
            PerClass[c][0] = PerClass[c][0] + 1
        elif(str(array[x][CONSTANT]) == "A-"):
            PerClass[c][1] = PerClass[c][1] + 1
        elif(str(array[x][CONSTANT]) == "B+"):
            PerClass[c][2] = PerClass[c][2] + 1
        elif(str(array[x][CONSTANT]) == "B"):
            PerClass[c][3] = PerClass[c][3] + 1
        elif(str(array[x][CONSTANT]) == "B-"):
            PerClass[c][4] = PerClass[c][4] + 1
        elif(str(array[x][CONSTANT]) == "C+"):
            PerClass[c][5] = PerClass[c][5] + 1
        elif(str(array[x][CONSTANT]) == "C"):
            PerClass[c][6] = PerClass[c][6] + 1
        elif(str(array[x][CONSTANT]) == "C-"):
            PerClass[c][7] = PerClass[c][7] + 1
        elif(str(array[x][CONSTANT]) == "D"):
            PerClass[c][8] = PerClass[c][8] + 1
        elif(str(array[x][CONSTANT]) == "F"):
            PerClass[c][9] = PerClass[c][9] + 1
        elif(str(array[x][CONSTANT]) == r''):
            c += 1

        x += 1
    
    L = ["A", "A-", "B+", "B", "B-", "C+","C","C-","D","F"]
    figure, axis = plt.subplots(c)
    a = []
    a.append(fig_bar(L, total_Count, 'Group Grades'))
    classNames = []
    x = 0
    for row in array:
        if (str(array[x][CONSTANT]) == r''):
           
            classNames.append(array[x][0])
        x += 1
    v = 0
    for row in classNames:
        a.append(fig_bar(L, PerClass[v], str(classNames[v])))
        v += 1
    dp.write_pdf(str(gName), a)
    return PerClass, classNames
    
def Ztest(total , classes):
    GM = 0
    GSD = 0
    SMA = []
    SM = 0
    c = 0
    c2 = 0
    Final = 0
    SUM = 0
    c3 =0
    L = [4, 3.7, 3.3, 3, 2.7, 2.3, 2,1.7,1,0]
    r = re.compile(r"^\d*[.,]?\d*?$")
    finalString = ""
    for x in range(len(total)):
        GM = total[x] + GM
   
    GM = GM/(len(total))
 
    for x in range(len(total)):
        SUM = SUM + ((total[x] - GM)**2)
    standard = SUM / (len(total))
    standard = (math.sqrt(standard))

    for row in classes:
        if(isinstance(row, str) and c == 0):
          
            classNames = row
            c+=1
            continue
        if(isinstance(row, float)  or isinstance(row, int)):
          
            SM = SM + row
            c2+=1
        if(isinstance(row, str) and c == 1):
            classNames = row
            SM = SM/c2
          
            Final = (SM - GM)/standard
            
            if (Final < -.2):
                finalString = finalString + str(classNames) + " failed z test. Z value is: " + str(Final) + "\n"
                c3 += 1
            elif (Final > .2):
                finalString = finalString + str(classNames) + " failed z test. Z value is: " + str(Final) + "\n"
                c3 += 1
           
            SM = 0
            Final = 0
            c2 = 0
    SM = SM/c2
   
    Final = (SM - GM)/standard
  
    if (Final < -.2):
        finalString = finalString + str(classNames) + " failed z test. Z value is: " + str(Final) + "\n"
        c3 += 1
    elif (Final > .2):
        finalString = finalString + str(classNames) + " failed z test. Z value is: " + str(Final) + "\n"
        c3 += 1
    if (c3 == 0):
        finalString = finalString +  " All passed z test." 
    SM = 0
    Final = 0
    c2 = 0
    with open('readme.txt', 'w') as f:
        f.write(finalString)
   

 
def make_pdf(FINAL):
    pdf = FPDF()
  

    pdf.add_page()
  

    pdf.set_font("Arial", size = 15)
  

    pdf.cell(200, 10, txt = FINAL, ln = 1, align = 'C')

    pdf.output("results.pdf") 

def merging(name2):
    pdfs = ["results.pdf", name2]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(name2 + "resultsfile.pdf" )
    merger.close()
