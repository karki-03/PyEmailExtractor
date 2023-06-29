from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="PyEmailExtractor",
    version="0.2",
    author="Bidut Karki",
    author_email="bidutjava3@gmail.com",
    description="Tool for extracting emails from pdf and docx files. (Designed especially for resumes)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["PyEmailExtractor"],
    install_requires=[
        "docx2txt==0.8",
        "lxml==4.9.2",
        "PyPDF2==3.0.1",
        "python-docx==0.8.11",
        "PyMuPDF==1.22.5",
        "pytesseract",
    ],
)
