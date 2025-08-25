# 🎯 Face Attendance System (CLI Based)

A simple **Face Recognition Attendance System** built with **OpenCV, Pandas, and Python**.
This project allows you to register students' faces, train a recognition model, and mark daily attendance automatically.

---

## 📂 Project Structure

```
Face-Attendance-Project/
│── dataset/                # Stores student face images
│    ├── 101_WangLing/
│    ├── 102_Naruto/
│    └── 103_Ayanokoji/
│
│── face_register.py        # Register new student faces + train model
│── face_attendance.py      # Run attendance system
│── face_model.yml          # Trained face recognition model (auto-created)
│── labels.pickle           # Mapping of student IDs to names (auto-created)
│── requirements.txt        # Dependencies + instructions
```

---

## ⚡ Features

* Face registration (capture dataset from webcam)
* Train face recognition model
* Mark daily attendance automatically in Excel sheet
* Attendance saved with **date-wise Excel file** (`attendance_DD-MM-YYYY.xlsx`)
* CLI-based (no GUI) → simple & lightweight

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/face-attendance-project.git
   cd face-attendance-project
   ```

2. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure your system has:

   * Python 3.9+
   * Webcam connected & working

---

## 🚀 Usage

### Step 1: Create Dataset

Make a folder named `dataset/` with subfolders for each student:

```
dataset/
├── 101_WangLing/
├── 102_Naruto/
└── 103_Ayanokoji/
```

Each folder name format:

```
<studentID>_<studentName>
```

---

### Step 2: Register Faces & Train Model

Run:

```bash
python face_register.py
```

* Captures face images from webcam
* Trains the model → generates `face_model.yml` & `labels.pickle`

---

### Step 3: Run Attendance System

Run:

```bash
python face_attendance.py
```

* Recognizes student faces
* Marks attendance in `attendance_<date>.xlsx`

---

## 📊 Output Example

After running, an Excel file will be generated:

**attendance\_25-08-2025.xlsx**

| Student ID | Name     | Time        |
| ---------- | -------- | ----------- |
| 101        | WangLing | 09:12:45 AM |
| 102        | Naruto   | 09:13:20 AM |

---

## 🔮 Future Improvements

* Email notifications for parents (free Gmail option)
* SMS alerts (requires paid service like Twilio)
* Dashboard visualization with charts

---

## 📜 License

This project is licensed under the **MIT License** – free to use and modify.

---

👉 Do you want me to also add **sample commands for running on Windows (PowerShell)** separately in the README so it’s beginner-friendly?
