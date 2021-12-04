import DataParser 
import csv 
import re
import matplotlib.pyplot as plt
import pickle 
import numpy as np
#import pandas

#def grade_Converter(): 
#takes csv reader array and converts letter grade into a numeric grade 
#returns array with each numeric grade 

#def Math one (): Not sure what to name this yet 
# takes the numeric grades and runs them through the equation 
#this will build plots and visuals that get returned and added to the website 
def csv_Reader(files):

    filename = []
    with open(files, 'r') as f:
        filename=f.read().split("\n")
# initializing the titles and rows list
        
        fields = []
        rows = []
  
# reading csv file
        filename.pop(0)
        for element in filename:
                with open("data/"+element, 'r') as csvfile:
    # creating a csv reader object
                        csvreader = csv.reader(csvfile)

      
    # extracting field names through first row
                        fields = next(csvreader)
                        rows.append(fields)
    # extracting each data row one by one
                        for row in csvreader:
                                rows.append(row)
        return rows
def comma_Check(files):
        filename = []
        with open(files, 'r') as f:
                filename=f.read().split("\n")
        filename.pop(0)
        for element in filename:
                with open("data/"+element, 'r') as f:
                        txt = f.read() #.replace(r"\s+", ",")
                with open("data/"+element, 'w') as f:
                        txt = re.sub(r'\s+"', ",\"", txt)
                        f.write(re.sub(r'"\s+', "\",", txt))
comma_Check("data/COMSCprogram.GRP")
rows = csv_Reader("data/COMSCprogram.GRP")
def letter_Graph(array):
        total_Count = [0,0,0,0,0,0,0,0,0,0]
        x=0
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
                x+=1
        C = 0
        x=0 
        for row in array: 
            if (str(array[x][CONSTANT]) == r''):
                print(str(array[x][CONSTANT]))
                C+=1
            x+=1

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
                        c+=1
                        
                x+=1
        
        L = ["A", "A-","B+","B","B-","C+","C","C-","D","F"]
        figure, axis = plt.subplots(3)
        axis[0].bar(L,total_Count,width = 0.8, color = ['green' ,'red'])
        plt.grid(axis = 'y')
        for x in range(2):
                axis[1].bar(L,PerClass[x-1],width = 0.8, color = ['green' ,'red'])
                plt.grid(axis = 'y')
        #plt.plot(L,total_Count)
        plt.show()
# loop to count amount of class in section by checking amount in array
#loop for each graph until null maybe implent unknown array amount clause or make a muly dimensional array per class with grades 
#multi dimensional array is most likely the best option 
#return each array type so that the graph functinn and numeric function can use them 
#make the graphing function 

letter_Graph(rows)
import numpy as np
import matplotlib.pyplot as plt

# an example graph type
def fig_barh(ylabels, xvalues, title=''):
    # create a new figure
    fig = plt.figure()

    # plot to it
    yvalues = 0.1 + np.arange(len(ylabels))
    plt.barh(yvalues, xvalues, figure=fig)
    yvalues += 0.4
    plt.yticks(yvalues, ylabels, figure=fig)
    if title:
        plt.title(title, figure=fig)

    # return it
    return fig

from matplotlib.backends.backend_pdf import PdfPages

def write_pdf(fname, figures):
    doc = PdfPages(fname)
    for fig in figures:
        fig.savefig(doc, format='pdf')
    doc.close()

def main():
    a = fig_barh(['a','b','c'], [1, 2, 3], 'Test #1')
    b = fig_barh(['x','y','z'], [5, 3, 1], 'Test #2')
    c = fig_barh(['x','y','z'], [5, 3, 1], 'Test #3')
    write_pdf('test.pdf', [a, b, c])

if __name__=="__main__":
    main()
#total_Count = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"] [0 , 1, 1 ]
