import cv2
import numpy as np
import pandas as pd
import os
import datetime as dt
import pickle

# Paths
model_path = "face_model.yml"
labels_path = "labels.pickle"
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
attendance_file = "attendance_face.xlsx"

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(model_path)

# Load labels
with open(labels_path, "rb") as f:
    labels = pickle.load(f)

# Initialize face detector
face_cascade = cv2.CascadeClassifier(cascade_path)

# Read existing attendance or create new
if os.path.exists(attendance_file):
    df = pd.read_excel(attendance_file, engine='openpyxl')
else:
    df = pd.DataFrame(columns=["Student ID", "Name", "Date", "Time"])

# Track who has been marked today
today_str = dt.date.today().isoformat()
marked_today = set(df[df["Date"]==today_str]["Student ID"].tolist())

# Open webcam
cap = cv2.VideoCapture(0)
print("Opening webcam... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        label_id, confidence = recognizer.predict(face_roi)
        student_info = labels.get(label_id, "Unknown")

        # Draw rectangle and name
        color = (0, 255, 0) if student_info != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)
        cv2.putText(frame, str(student_info), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Mark attendance if not already marked
        student_id = student_info.split("_")[0]
        student_name = student_info.split("_")[1] if "_" in student_info else "Unknown"

        if student_id not in marked_today and student_info != "Unknown":
            now = dt.datetime.now()
            new_entry = {
                "Student ID": student_id,
                "Name": student_name,
                "Date": now.date().isoformat(),
                "Time": now.strftime("%H:%M:%S")
            }
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            df.to_excel(attendance_file, index=False)
            marked_today.add(student_id)
            print(f"✅ Attendance marked: {student_name} ({student_id}) at {now.strftime('%H:%M:%S')}")

    cv2.imshow("Face Attendance - Press 'q' to quit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Attendance saved to {attendance_file}")