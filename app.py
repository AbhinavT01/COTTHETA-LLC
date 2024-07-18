from flask import Flask, request, render_template, send_from_directory, jsonify, url_for
import os
from main import main_file
from card_detect import extract_info
from card_detect import extract_text_from_image
from doc_text_detect import detect_document_text
from TableOCR import extract_text_and_generate_csv

app = Flask(__name__)

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = 'uploads/outputcsv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bank')
def bank():
    return render_template('bank.html')

@app.route('/doc')
def doc():
    return render_template('doc.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/uploadid', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Process the image
        processed_text = main_file(file_path)
        
        return render_template('result.html', result=processed_text)

@app.route('/uploaddoc', methods=['POST'])
def upload_doc():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Process the image
        processed_text = detect_document_text(file_path)
        
        return render_template('resultdoc.html', result=processed_text)

@app.route('/uploadbank', methods=['POST'])
def upload_bank():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Process the image
        processed_text = extract_info(file_path)
        
        return render_template('resultbank.html', result=processed_text)

@app.route('/uploadtable', methods=['POST'])
def upload_table():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Process the table image and generate CSV
        csv_path = extract_text_and_generate_csv(file_path)

        csv_filename = os.path.basename(csv_path)
        csv_url = url_for('download_csv', filename=csv_filename)
        
        return render_template('resulttable.html', result='Table processed successfully.', csv_url=csv_url)

@app.route('/uploads/outputcsv/<filename>')
def download_csv(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
