from flask import Flask, request, render_template, url_for, jsonify
import os

app = Flask(__name__)


@app.route('/listApi', methods=["GET"])
def list_all_job_descriptions_text():
    # Set the path to the folder containing the TXT files
    folder_path = 'Job_description_TXT'

    # Get a list of all the files in the folder
    files = os.listdir(folder_path)

    # Filter the list to include only TXT files
    txt_files = [file for file in files if file.endswith('.txt')]

    # Join the names of the TXT files using a delimiter
    job_description_names = "\n".join(txt_files)

    return job_description_names


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
