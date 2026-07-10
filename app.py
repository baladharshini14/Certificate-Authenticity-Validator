from flask import Flask, render_template, request, redirect, send_file
import mysql.connector
import PyPDF2
import re
import qrcode
import os

app = Flask(__name__)

conn = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    port=int(os.environ.get("DB_PORT")),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME")
)

cursor = conn.cursor()

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/admin')
def admin():

    cursor.execute("SELECT * FROM certificates")
    certificates = cursor.fetchall()

    return render_template(
        'admin.html',
        certificates=certificates
    )


@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():

    file = request.files['certificate']

    if file and file.filename.endswith('.pdf'):

        pdf_reader = PyPDF2.PdfReader(file)

        text = ""

        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        print(text)

        cursor.execute("SELECT certificate_id FROM certificates")
        ids = cursor.fetchall()

        genuine = False
        cert_id = ""

        for row in ids:
            if row[0] in text:
                genuine = True
                cert_id = row[0]
                break

        if genuine:
            result = f"✅ Genuine Certificate ({cert_id})"
        else:
            result = "❌ Fake Certificate"

        return render_template(
            'result.html',
            result=result
        )

    return "Please upload PDF file only"


if __name__ == '__main__':
    app.run(debug=True)
