from flask import Flask, request, render_template, make_response
from xhtml2pdf import pisa
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form2.html')


@app.route('/submit-form', methods=['POST'])
def generate_pdf():
    name = request.form['name']
    email = request.form['email']
    print(f"Received Name: {name}, Email: {email}")  # Debugging statement

    rendered_html = render_template('pdf_template.html', name=name, email=email)

    pdf = io.BytesIO()

    pisa_status = pisa.CreatePDF(io.StringIO(rendered_html), dest=pdf)

    if pisa_status.err:
        print("Error in PDF creation")  # Debugging statement
        return "Error creating PDF", 500

    pdf.seek(0)  # Rewind the buffer
    response = make_response(pdf.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=form_data.pdf'

    return response


#
if __name__ == '__main__':
    app.run(debug=True)
