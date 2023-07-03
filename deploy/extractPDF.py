import stopwords as stopwords
from PyPDF2 import PdfReader
import re
from pathlib import Path
import nltk
import os
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))
nltk.download('stopwords')



class Extract:
    # Extract Job Description from pdf and convert it into text file
    def extract_all(self, Pdf_Path, Text_Path):
        folder_path = Pdf_Path

        # Get a list of all the files in the folder
        files = os.listdir(folder_path)

        # Filter the list to include only PDF files
        pdf_files = [file for file in files if file.endswith('.pdf')]

        # Print the names of the PDF files
        for file in pdf_files:
            pdf = PdfReader(Pdf_Path + file)
            with Path(Text_Path + file[:-4] + '.txt').open(mode='w', encoding='utf-8') as x_file:
                text = ''
                for page in pdf.pages:
                    text += page.extract_text()
                    x_file.write(text)



