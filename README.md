# Face_Recognisation

```markdown
# 🎯 Real-Time Face Recognition using Python and OpenCV

This project performs real-time face recognition using your webcam. It uses `face_recognition`, `OpenCV`, and a folder of known faces to detect and label people in real time.

## 📌 Features

- 📷 Real-time face detection and recognition
- 🧠 Uses deep learning-based face recognition (via `dlib`)
- 🗂 Supports multiple known faces (load from `known_faces/` folder)
- ✅ Keeps names on screen even if detection briefly fails (no blinking)
- 🚪 Press `q` to exit

## 📁 Folder Structure

```

FaceRecognisationF/
├── known\_faces/             # Folder with known person images (e.g., person1.jpg)
├── main.py                  # Main face recognition script
├── README.md                # Project documentation

````

## 🔧 Requirements

Install dependencies using pip:

```bash
pip install opencv-python
pip install face_recognition
````

If dlib errors occur, run:

```bash
pip install cmake
pip install dlib
```

> If scripts (like `cmake.exe`) are not recognized, add the directory to PATH:
> `C:\Users\<YourName>\AppData\Roaming\Python\Python39\Scripts`

## 🚀 How to Run

1. Clone or download this repo.
2. Place clear front-facing images in `known_faces/`.

   * File names (without `.jpg` or `.png`) are used as the display names.
3. Run the program:

```bash
python main.py
```

4. The webcam opens. If a known face is detected, their name is shown on the screen.

## 📝 Notes

* Each face image in `known_faces/` should contain only **one person’s face**
* Ensure proper lighting for better recognition
* Adjust `DISPLAY_DURATION` in code to control how long the name stays visible

## 📸 Example

If you add an image `known_faces/jaheer.jpg`, the program will show **JAHEER** on screen when your face appears in the webcam feed.

## 🤖 Technologies Used

* Python 3.9+
* OpenCV
* face\_recognition
* dlib
* NumPy

## 🙋‍♂️ Author

**Jaheer Ahmed**
🎓 Machine Learning Student
📝 Project Title: Real-Time Face Recognition using ML

## 📄 License

This project is licensed under the MIT License.

```

---

📌 **Paste this directly into your GitHub `README.md`.**  
Let me know if you want help with:
- Adding a `.gitignore`
- Uploading to GitHub step-by-step
- Adding attendance marking
- Creating a GUI interface

Just say the word!
```
