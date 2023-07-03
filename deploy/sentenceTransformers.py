from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os
from tabulate import tabulate


# GPT 3
# CodeBERT
class Similarity():

    def list_all_job_descriptions_text(self):
        # Set the path to the folder containing the TXT files
        folder_path = 'Job_description_TXT'

        # Get a list of all the files in the folder
        files = os.listdir(folder_path)

        # Filter the list to include only TXT files
        txt_files = [file for file in files if file.endswith('.txt')]

        # Join the names of the TXT files using a delimiter
        job_description_names = "\n".join(txt_files)

        return job_description_names

    def calculate_similarity(self):
        job_description_name = input("Enter Job description Name: ")
        with open('Job_description_TXT/' + job_description_name, 'r', encoding='utf-8') as g:
            job_description_text = g.read()

        folder_path = 'CVs_TXT'

        cv_texts = []
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    cv_texts.append((file_name, text))

        model = SentenceTransformer('all-MiniLM-L6-v2')
        cv_encodings = model.encode([text for _, text in cv_texts]).reshape(len(cv_texts), -1)
        job_encoding = model.encode(job_description_text).reshape(1, -1)

        # calculate similarity scores
        similarity_scores = cosine_similarity(cv_encodings, job_encoding) * 100

        # create a list of lists containing (filename, similarity score)
        similarity_scores_list = []
        for i, (cv_name, _) in enumerate(cv_texts):
            similarity_scores_list.append([cv_name, similarity_scores[i][0]])

        # print table
        headers = ['CV Name', 'Similarity Score']
        print(tabulate(similarity_scores_list, headers=headers))

        return similarity_scores_list
