from os.path import abspath
import os
from werkzeug.utils import safe_join
from flask import Flask, request, send_file, render_template, make_response, send_from_directory
from data_to_pdf import _Create_PDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form2.html')

@app.route('/submit-form', methods=['POST'])
def generate_pdf():
    name = request.form['name']
    email = request.form['email']
    print(name)
    print(email)
    ss = _Create_PDF()
    ss.ccc(name,email)
    return {'status': 'success'}, 200


@app.route('/download-pdf', methods=['GET'])
def download_pdf():
    file_path = safe_join('static', 'test.pdf')
    abs_path = abspath(file_path)
    if not os.path.isfile(abs_path):
        return "File not found", 404
    with open(file_path, 'rb') as f:
        file_data = f.read()
        print("File size:", len(file_data))  # Print file size to ensure it's not zero

    return send_file(abs_path, as_attachment=False, download_name='test.pdf',mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
