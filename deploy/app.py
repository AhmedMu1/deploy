from flask import Flask, request, render_template, url_for, jsonify
from extractPDF import Extract
from sentenceTransformers import Similarity

extractPDF = Extract()
similarity = Similarity()

app = Flask(__name__)


@app.route('/listApi', methods=["GET"])
def list_job_descriptions():
    job_descriptions = similarity.list_all_job_descriptions_text()
    return jsonify(job_descriptions)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
