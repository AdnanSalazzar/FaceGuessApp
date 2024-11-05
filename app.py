from flask import Flask, render_template, request, redirect, url_for
import cv2 as cv
import numpy as np
import os
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load the pre-trained model
haarCascade = cv.CascadeClassifier('harr_face.xml')
face_recognizer = cv.face.LBPHFaceRecognizer_create()
    
face_recognizer.read('face_trained.yml')

people = ['ben_afflek', 'elton_john', 'jerry_seinfeld', 'madonna', 'mindy_kaling']

def detect_face(image_path):
    img = cv.imread(image_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_rect = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    face_data = []  # Store label and confidence for each detected face

    for (x, y, w, h) in faces_rect:
        face_roi = gray[y:y + h, x:x + w]

        label, confidence = face_recognizer.predict(face_roi)
        cv.putText(img, str(people[label]), (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Save label and confidence in the list
        face_data.append({'label': people[label], 'confidence': confidence})

    # Save the output image
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'detected.jpg')
    cv.imwrite(output_path, img)
    return output_path , face_data

def cleanup_uploads_folder():
    # Path to the uploads folder
    upload_folder = app.config['UPLOAD_FOLDER']
    
    # List all files in the uploads folder
    files = [os.path.join(upload_folder, f) for f in os.listdir(upload_folder) if os.path.isfile(os.path.join(upload_folder, f))]
    
    # Sort files by modification time (oldest to newest)
    files.sort(key=os.path.getmtime)
    
    # If more than 3 files, delete the oldest ones
    while len(files) > 3:
        os.remove(files[0])  # Remove the oldest file
        files.pop(0)         # Remove it from the list

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)
    
    image = request.files['image']
    if image.filename == '':
        return redirect(request.url)

    if image:
        
        # Run the cleanup function before saving the new file
        cleanup_uploads_folder()
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(file_path)
 
         # Perform face detection
        result, face_data = detect_face(file_path)

        return render_template('index.html', result=result , face_data = face_data)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
