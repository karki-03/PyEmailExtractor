# PyEmailExtractor [![Downloads](https://static.pepy.tech/badge/pyemailextractor)](https://pepy.tech/project/pyemailextractor)

PyEmailExtractor is a tool designed specifically for extracting emails from PDF and DOCX files, with a focus on resumes. It provides a convenient way to extract email addresses from these document formats, which can be useful for various applications, such as recruitment, data analysis, or contact management.

## Features

- Extract email addresses from PDF files.
- Extract email addresses from DOCX files.
- Designed specifically for resumes, ensuring accurate email extraction.
- Simple and easy-to-use.

## Installation

You can install PyEmailExtractor using pip:

```
pip install PyEmailExtractor
```
## Example Usage
```
from PyEmailExtractor import extract_emails

dir = "/home/username/Downloads/resumes"

list_emails = extract_emails(dir)

print(list_emails)
```

- The above example will print the parsed emails in a `list`.

## Requirements

PyEmailExtractor requires the following dependencies:
- docx2txt==0.8
- lxml==4.9.2
- PyPDF2==3.0.1
- python-docx==0.8.11
- PyMuPDF==1.22.5
- pytesseract

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.
License

`PyEmailExtractor is released under the MIT License. See the LICENSE file for more details.`
