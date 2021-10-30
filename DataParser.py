import pandas
import re 

##Imports that get added throughout the project will need to be added to specifications 

#####file_Crawler()
#goes through the data folder and makes an array for each grp 
#this array can then be added to the comma_check to preformat the files


######creates commas for files that need it and ignores the rest 
def comma_Check(files):
    for x in files:
        filename = x
        with open(filename, 'r') as f:
            txt = f.read() #.replace(r"\s+", ",")
        with open(filename, 'w') as f:
            txt = re.sub(r'\s+"', ",\"", txt)
            f.write(re.sub(r'"\s+', "\",", txt))
comma_Check(array)

########csv Reader GOING TO NEED SOME CHANGES BEFORE FINAL IMPLEMENTATION 
def csv_Reader(files):
    for x in files:
        filename = x
# initializing the titles and rows list
    fields = []
    rows = []
  
# reading csv file
    with open(filename, 'r') as csvfile:
    # creating a csv reader object
         csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
        fields = next(csvreader)
  
    # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
  
    # get total number of rows
        print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the field names
    print('Field names are:' + ', '.join(field for field in fields))
  
#  printing first 5 rows
    print('\nFirst 5 rows are:\n')
    for row in rows[:1]:
    # parsing each column of a row
        for col in row:
            print("%10s"%col),
            print('\n')
#add the return for a 3d array 