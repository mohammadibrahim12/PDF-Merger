#Requires the PyPDF2 library 
from PyPDF2 import PdfFileMerger, PdfFileReader

#Creates merger object 
combine = PdfFileMerger()

#Will loop and keep asking for a file name as long as a file is not found, if it is then will break out of loop 
while True:
    try:
        #ask user for the file 
        input_filename = str(input("Enter the first filename or path to the file: "))
        #calls append function on merger opject to append the given file 
        combine.append(PdfFileReader(open(input_filename, 'rb')))
        break
    except FileNotFoundError: 
        #Prints message if file is not found
        print ("File not found, check spelling or directory")

while True:
    try:
        #ask user for the file name (can be file itself if it is in the currect directory or path to the file)
        input_filename2 = str(input("Enter the second filename or path to the file: "))
        #calls append function on merger opject to append the given file to second file 
        combine.append(PdfFileReader(open(input_filename2, 'rb')))
        break
    except FileNotFoundError: 
         #Prints message if file is not found
        print ("File not found, check spelling or directory")

#Ask user for the name of the merged output file name 
output_filename = str(input("Enter the name of the .pdf merged file: "))
#Create the merged file with the given file name; will go into whichever directory script is run from, unless directory is specified
combine.write("{}.pdf".format(output_filename))

print("\n\n{0} combined with {1} into {2}.pdf\n\n".format(input_filename, input_filename2, output_filename))