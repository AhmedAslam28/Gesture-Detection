from flask import Flask, render_template, request, Response
import cv2
import numpy as np
import keyboard

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

MIN_CONTOUR_AREA = 2000 # Increase to filter out smaller contours
ASPECT_RATIO_THRESHOLD = 0.6 # Lower threshold for longer, more vertical shapes



def detect_thumbs_up(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    _, thresholded = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        contour_area = cv2.contourArea(max_contour)

        if contour_area > MIN_CONTOUR_AREA:
            x, y, w, h = cv2.boundingRect(max_contour)
            aspect_ratio = float(w) / h

            if aspect_ratio >= ASPECT_RATIO_THRESHOLD:
                # Calculate center and radius for the circle around the thumbs-up area
                center_x = x + w // 2
                center_y = y + h // 2
                radius = max(w, h) // 2

                return True, (center_x, center_y, radius)

    return False, None

@app.route('/')
def index():
    return render_template('page.html')

def generate_frames():
    test_video = cv2.VideoCapture('uploaded_file.mp4')
    while True:
        ret, frame = test_video.read()
        if not ret:
            break
        
        gesture_detected, bbox = detect_thumbs_up(frame)
        
        if gesture_detected:
            center_x, center_y, radius = bbox
            
            cv2.putText(frame, "DETECTED", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.circle(frame, (center_x, center_y), radius, (0, 255, 0), 2)


        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        if keyboard.is_pressed('q'):
            break
    test_video.release()
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'fileUpload' not in request.files:
            return "No file part in request"

        file = request.files['fileUpload']

        if file.filename == '':
            return "No selected file"

        file.save('uploaded_file.mp4')

        return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True)
