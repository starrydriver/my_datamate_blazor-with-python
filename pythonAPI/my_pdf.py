import fitz
from docx import Document
import os
from flask import  request, jsonify

UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = os.path.abspath(os.path.dirname(os.getcwd())) + r'\BlazorDisplay\BlazorDisplay\wwwroot'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
my_filename:str = ''

def register_routes1(app):
    @app.route('/api/add', methods=['GET'])#测试测试测试
    def add():
        result = 1 + 1
        return jsonify({"result": result})

    @app.route('/api/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            return jsonify({"error": "没有文件上传"}), 400
        file = request.files['file']
        my_filename = file.filename
        if file.filename == '':
            return jsonify({"error": "未选择文件"}), 400
        if file and file.filename.endswith('.pdf'): # 保存原始 PDF 文件到 wwwroot 文件夹
            original_pdf_path = os.path.join(OUTPUT_FOLDER, file.filename)
            file.save(original_pdf_path)  # 直接保存到 wwwroot 文件夹
            return jsonify({'message': '文件上传成功', 'original_file': os.path.abspath(original_pdf_path)}), 200
        else:
            return jsonify({"error": "只支持 PDF 文件"}), 400

    @app.route('/api/file_exists', methods=['GET'])
    def file_exists():
        filename = my_filename
        file_path = os.path.join(OUTPUT_FOLDER, filename)
        exists = os.path.exists(file_path)
        return jsonify({"exists": exists}), 200

    @app.route('/api/convert', methods=['POST'])
    def convert_file():
        if 'filename' not in request.json:
            return jsonify({"error": "没有文件名提供"}), 400
        filename = request.json['filename']
        pdf_path = os.path.join(OUTPUT_FOLDER, filename)
        if not os.path.exists(pdf_path):
            return jsonify({"error": "文件不存在"}), 404
        # 转换 PDF 为 Word
        docx_path = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(filename)[0]}.docx")
        convert_pdf_to_word(pdf_path, docx_path)
        return jsonify({'message': '文件转换成功', 'output_file': os.path.abspath(docx_path)}), 200

    def convert_pdf_to_word(pdf_path, docx_path):
        doc = fitz.open(pdf_path)  # 打开 PDF 文件
        document = Document()  # 创建一个 Word 文档对象
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text = page.get_text()
            document.add_paragraph(text)  # 将提取的文本添加到 Word 文档中
        document.save(docx_path)  # 保存 Word 文档