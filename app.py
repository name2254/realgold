from flask import Flask, request, jsonify
from flask_cors import CORS  # เพิ่มบรรทัดนี้

app = Flask(__name__)
CORS(app)  # เปิดใช้งาน CORS สำหรับทุก route

@app.route('/')
def home():
    return "✅ Backend is running!"

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']

    # ใส่โค้ดวิเคราะห์ภาพตรงนี้ (ตัวอย่างส่งกลับแบบ dummy)
    return jsonify({'result': 'Analyzed (demo)'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)