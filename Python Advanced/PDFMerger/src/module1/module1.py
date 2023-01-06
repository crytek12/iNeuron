import os
import PyPDF2


def dir_list(path):
    """Returns the list of all the file and folders from a directory, or returns None if the directory does
    not exist."""
    # Check if the directory exists
    if os.path.exists(path):
        # Return a list of the files and folders in the directory
        return os.listdir(path)
    else:
        # Return None if the directory does not exist
        return None


def open_pdf(path):
    # Check if the path is a directory
    if os.path.isdir(path):
        # Get a list of all the PDF files in the directory
        pdf_files = [f for f in os.listdir(path) if f.endswith('.pdf')]

        # Check if there are any PDF files
        if len(pdf_files) > 0:
            # Merge all the PDF files into a single PDF file
            merged_pdf = merge_pdfs(path, pdf_files)

            # Open the merged PDF file in the default app
            os.startfile(merged_pdf)


def merge_pdfs(path, pdf_files):
    # Create a PDF merger object
    merger = PyPDF2.PdfFileMerger()

    # Loop through all the PDF files
    for pdf in pdf_files:
        # Construct the absolute path to the PDF file
        pdf_path = os.path.join(path, pdf)
        # Open the current PDF file
        with open(pdf_path, 'rb') as file:
            # Add the current PDF file to the merger object
            merger.append(file)

    # Create a new PDF file to store the merged PDF
    merged_pdf = 'merged.pdf'

    # Open the new PDF file in write mode
    with open(merged_pdf, 'wb') as file:
        # Write the merged PDF to the new file
        merger.write(file)

    # Return the name of the merged PDF file
    return merged_pdf
