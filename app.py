import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from flask import Flask, request, jsonify

nltk.download('punkt')

app = Flask(__name__)


def filter_text(text):
    # Tokenize the text into individual words
    tokens = word_tokenize(text)

    # Join the filtered tokens back into a single string
    filtered_text = ' '.join(tokens)

    # Remove extra whitespaces
    filtered_text = ' '.join(filtered_text.split())

    return filtered_text


def extract_text_from_pdf(file):
    text = ""

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)

    # Iterate over each page in the PDF document
    for page_number in range(len(pdf_reader.pages)):
        # Extract the text from the page and append it to the string
        text += pdf_reader.pages[page_number].extract_text()

    return text


def calc_semantic(cv_text, job_description_text):
    try:
        module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        model = hub.load(module_url)

        # Encode the CV text and job description text into document embeddings
        cv_embedding = np.array(model([cv_text])[0])
        job_embedding = np.array(model([job_description_text])[0])

        # Calculate cosine similarity between the document embeddings
        similarity_score = np.dot(cv_embedding, job_embedding) / (
                    np.linalg.norm(cv_embedding) * np.linalg.norm(job_embedding))

        return similarity_score
    except Exception as e:
        print(e)


@app.route('/test')
def index():
    data = {"status": "Hello"}
    return jsonify(data)


@app.route("/rating", methods=["POST"])
def rating():
    if request.method == "POST":
        cv = request.files.get('cv')
        job_description_text = request.form.get('job_description')

        if cv is None or cv.filename == "" or job_description_text is None or job_description_text == "":
            return jsonify({"error": "No file or input string provided"})

        try:
            # Extract text from the CV PDF
            cv_text = extract_text_from_pdf(cv)

            # Calculate the semantic similarity
            semantic_similarity = calc_semantic(cv_text, job_description_text)

            data = {"rating": float(semantic_similarity)}

            return jsonify(data)

        except Exception as e:
            return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
