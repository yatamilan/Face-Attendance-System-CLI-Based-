import cv2
import os
import numpy as np

# Paths
dataset_path = "dataset"
model_path = "face_model.yml"
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

# Initialize face detector
face_cascade = cv2.CascadeClassifier(cascade_path)

# Prepare training data
faces = []
labels = []
label_dict = {}  # map label id to name
current_label = 0

for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    if not os.path.isdir(folder_path):
        continue

    student_id, student_name = folder.split("_", 1)
    label_dict[current_label] = f"{student_id}_{student_name}"

    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces_rects = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces_rects:
            face_roi = gray[y:y+h, x:x+w]
            faces.append(face_roi)
            labels.append(current_label)

    current_label += 1

# Train LBPH recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))
recognizer.save(model_path)

# Save label dictionary
import pickle
with open("labels.pickle", "wb") as f:
    pickle.dump(label_dict, f)

print("✅ Training complete. Model saved as 'face_model.yml'")
print("Labels saved as 'labels.pickle'")
