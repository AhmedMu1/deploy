
from extractPDF import Extract

from sentenceTransformers import Similarity

extractPDF = Extract()
similarity = Similarity()

jobDescriptionPdf_Path = 'Job_description_PDF/'
jobDescriptionText_Path = 'Job_description_TXT/'

CVs_PDF_Path = 'CVs_PDF/'
CVs_Text_Path = 'CVs_TXT/'

# extractPDF.extract_all(jobDescriptionPdf_Path, jobDescriptionText_Path)
# extractPDF.extract_all(CVs_PDF_Path, CVs_Text_Path)

print(similarity.list_all_job_descriptions_text())
similarity.calculate_similarity()
