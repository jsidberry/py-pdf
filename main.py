import PyPDF2

pdf_file_name = ""

# Open the PDF file
with open(pdf_file_name, 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)
    
    # Initialize a variable to store all the text
    text = ""
    
    # Loop through all the pages and extract text
    for page_num in range(num_pages):
        # Get a specific page
        page = pdf_reader.pages[page_num]
        
        # Extract text from the page
        text += page.extract_text() + "\n"
    
    # Print the text extracted from the PDF
    print(text)
