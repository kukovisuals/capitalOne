import pdfplumber
import os
import re

current_directory = os.getcwd()
print("Current working directory:", current_directory)
# Replace 'path/to/your/pdf.pdf' with the actual path to your PDF file
pdf_file_path = 'assets/feb23.pdf'

with pdfplumber.open(pdf_file_path) as pdf:
    # Assuming the table is on the first page, set the page number to 0
    page = pdf.pages[2]

    # Extract the table
    text = page.extract_text()

    #split th etxt by lines
    lines = text.split('\n')

    # Specify the header titles
    header = ['Trans Date', 'Post Date', 'Description', 'Amount']
    print("Header:", header)

    # Define a regular expression pattern to match the row structure
    pattern = r"(\w{3} \d{2})\s+(\w{3} \d{2})\s+(.+?(?=\s+-?\$))\s+(-?\$[\d,]+(?:\.\d{1,2})?)"
    
    # Print the rows (excluding the header)
    for line in lines[1:]:
        match = re.match(pattern, line)
        if match:
            row = list(match.groups())
            # Check if the "Description" column has a trailing minus sign
            if row[2].endswith(" -"):
                row[2] = row[2].rstrip(" -")
                row[3] = "-" + row[3]
            
            print("Row:", row)
