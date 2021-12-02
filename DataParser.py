
import re 
import csv

#input for both should be the name of the group file including the path of data folder IE "data/class.GRP"

######creates commas for files that need it and ignores the rest 

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
