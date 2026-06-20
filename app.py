from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze():

    if 'image' not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    file = request.files['image']

    file_bytes = np.frombuffer(
        file.read(),
        np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    if image is None:
        return jsonify({
            "error": "Invalid image"
        }), 400

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    brightness = gray.mean()

    height, width = image.shape[:2]

    center_x = width // 2
    center_y = height // 2

    x1 = center_x - 50
    y1 = center_y - 50

    x2 = center_x + 50
    y2 = center_y + 50

    cv2.rectangle(
        image,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2
    )

    return jsonify({
        "status": "processed",
        "brightness": round(float(brightness), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)