
import re 
import csv
import fpdf
from matplotlib.backends.backend_pdf import PdfPages
from fpdf import FPDF

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
def write_pdf(fname, figures):
    doc = PdfPages(fname)
    for fig in figures:
        fig.savefig(doc, format='pdf')
    doc.close()

def LtoN(array):
        total_Count = []
        x = 0
        CONSTANT = 2
        for row in array:
                if (str(array[x][CONSTANT]) == "A"):
                        total_Count.append(4)
                elif(str(array[x][CONSTANT]) == "A-"):
                        total_Count.append(3.7)
                elif(str(array[x][CONSTANT]) == "B+"):
                        total_Count.append(3.3)
                elif(str(array[x][CONSTANT]) == "B"):
                        total_Count.append(3)
                elif(str(array[x][CONSTANT]) == "B-"):
                        total_Count.append(2.7)
                elif(str(array[x][CONSTANT]) == "C+"):
                        total_Count.append(2.3)
                elif(str(array[x][CONSTANT]) == "C"):
                        total_Count.append(2)
                elif(str(array[x][CONSTANT]) == "C-"):
                        total_Count.append(1.7)
                elif(str(array[x][CONSTANT]) == "D"):
                        total_Count.append(1)
                elif(str(array[x][CONSTANT]) == "F"):
                        total_Count.append(0)
                x += 1
        perClass = []
        x = 0
        for row in array:
                if (str(array[x][CONSTANT]) == "A"):
                        perClass.append(4)
                elif(str(array[x][CONSTANT]) == "A-"):
                        perClass.append(3.7)
                elif(str(array[x][CONSTANT]) == "B+"):
                        perClass.append(3.3)
                elif(str(array[x][CONSTANT]) == "B"):
                        perClass.append(3)
                elif(str(array[x][CONSTANT]) == "B-"):
                        perClass.append(2.7)
                elif(str(array[x][CONSTANT]) == "C+"):
                        perClass.append(2.3)
                elif(str(array[x][CONSTANT]) == "C"):
                        perClass.append(2)
                elif(str(array[x][CONSTANT]) == "C-"):
                        perClass.append(1.7)
                elif(str(array[x][CONSTANT]) == "D"):
                        perClass.append(1)
                elif(str(array[x][CONSTANT]) == "F"):
                        perClass.append(0)
                elif(str(array[x][CONSTANT]) == r''):
                        perClass.append(str(array[x][0]))
                x += 1 
       
        print('\n')
      
        return total_Count, perClass 
def fromtext():
        pdf = FPDF()   
   
        
        pdf.add_page()
        

        pdf.set_font("Arial", size = 15)
        
     
        f = open("readme.txt", "r")
        
       
        for x in f:
                pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        
       
        pdf.output("results.pdf")  
