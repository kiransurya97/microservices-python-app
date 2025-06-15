import os
from flask import Flask, request
from werkzeug.utils import secure_filename

server = Flask(__name__)

@server.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part in request', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    upload_dir = '/tmp'
    os.makedirs(upload_dir, exist_ok=True)

    filename = secure_filename(file.filename)
    save_path = os.path.join(upload_dir, filename)

    try:
        file.save(save_path)
        print(f"[INFO] File saved to {save_path}")
        return 'success'
    except Exception as e:
        print(f"[ERROR] Failed to save file: {e}")
        return f"internal server error: {str(e)}", 500

if __name__ == '__main__':
    # ✅ Debug enabled
    server.run(host='0.0.0.0', port=8080, debug=True)
