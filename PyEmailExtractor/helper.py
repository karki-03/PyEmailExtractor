import re
import os
import PyPDF2
import docx2txt
from docx import Document
import fitz


def fetch_files(directory, file_extensions):
    """To fetches all the file with the given ext in the given directory"""
    files = []
    try:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                if any(filename.endswith(ext) for ext in file_extensions):
                    filepath = os.path.join(dirpath, filename)
                    files.append(filepath)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write("Error from fetch_files function: \n" + str(e) + "\n")
    return files


def extract_email_from_pdf(pdf_file):
    """To extract emails from pdfs files"""
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email = ""
    try:
        doc = fitz.open(pdf_file)
        page1 = doc[0]
        text = str(page1.get_text("words"))
        email = re.findall(email_pattern, text)
        if not email:
            with open("no_email_logs.txt", "a") as f:
                f.write(str(pdf_file) + "\n")
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write("Error from extract_email_from_pdf function: \n" + str(e) + "\n")
    return email


def extract_email_from_docx(docx_file):
    """To extract emails from docx files"""
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email = ""
    try:
        text = docx2txt.process(str(docx_file))
        email = re.findall(email_pattern, text)
        if not email:
            with open("no_email_logs.txt", "a") as f:
                f.write(str(docx_file) + "\n")
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write("Error from extract_email_from_docx function: \n" + str(e) + "\n")
    return email
