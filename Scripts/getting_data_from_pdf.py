#Importing module to read the pdf file
import PyPDF2

# Getting file object
# Reading in binary
file = open("../Data/LUYIA PROVERBS.pdf", 'rb')

#Getting a reader object from the file object
reader = PyPDF2.PdfFileReader(file)

# Getting number of pages from the reader object
num_of_pages = reader.numPages

pdf_data = []

# Iterating through the number of pages to get the proverbs
for i in range(0,num_of_pages,1):
    # Getting invividual pages
    page = reader.getPage(i)
    # Extracting text from page and appending it to the pdf_data list
    pdf_data.append(page.extractText())

with open("../Data/proverbs.txt", "w", encoding="utf-8") as f:
    for item in pdf_data:
        f.write(str(item))