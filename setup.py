from setuptools import setup

setup(
    name="PyEmailExtractor",
    version="0.1",
    author="Bidut Karki",
    author_email="bidutjava3@gmail.com",
    description="Tool for extracting emails from pdf and docx files. (Designed especially for resumes)",
    packages=["PyEmailExtractor"],
    install_requires=[
        "docx2txt==0.8",
        "lxml==4.9.2",
        "PyPDF2==3.0.1",
        "python-docx==0.8.11",
        "PyMuPDF==1.22.5",
        # "fitz",
    ],
)
