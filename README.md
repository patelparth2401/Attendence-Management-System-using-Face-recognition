# Attendence-Management-System-using-Face-recognition


##  Project Overview
This is a Python-based **Attendance Management System** that utilizes **face recognition** technology to mark students' attendance automatically. The project is built using the `face-recognition` library and features a **GUI developed with Tkinter**.

##  Features
- **User Authentication:**
  - Login and Signup system.
  - Special authentication for **Admin** and **Teachers**.
- **Attendance Marking Process:**
  1. Capture a **classroom image**.
  2. Extract **student face images** from the classroom image and save them temporarily.
  3. Match each student's face with the database using their **Enrollment Number**.
  4. If a match is found, attendance for the student is marked for that day.

## 🛠 Technologies Used
- **Programming Language:** Python
- **GUI Framework:** Tkinter
- **Face Recognition:** `face-recognition` library
- **Database:** (Specify if any database is used, e.g., SQLite, MySQL)

##  Future Enhancements
- Implement **real-time video-based** attendance marking.
- Integrate **lecture timing and frequency tracking** for accurate attendance marking.
- Improve **model accuracy** for face recognition.

##  Installation & Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/patelparth2401/Attendence-Management-System-using-Face-recognition.git
   cd Attendence-Management-System-using-Face-recognition
   ```
2. **Install required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```sh
   python main.py
   ```

## 📷 Face Recognition Library Setup
Ensure that you have installed the `face-recognition` library and its dependencies:
```sh
pip install face-recognition dlib opencv-python numpy
```

> **Note:** `dlib` requires CMake and Visual Studio Build Tools (for Windows) to be installed.

##  Usage Instructions
1. **Admin/Teacher Login:** Authenticate using your credentials.
2. **Capture Classroom Image:** Take a picture of the class.
3. **Automatic Attendance Marking:** The system will extract student faces, match them, and mark attendance.
4. **View Attendance Records:** Check attendance logs in the system.

## 👨‍💻 Contributors
- **Parth Patel** ([GitHub](https://github.com/patelparth2401))

##  License
This project is open-source and available under the [MIT License](LICENSE).

