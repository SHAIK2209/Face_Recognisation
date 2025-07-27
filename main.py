import cv2
import numpy as np
import face_recognition
import os
import time

path = 'known_faces'
images = []
names = []

# Load and encode known faces
for filename in os.listdir(path):
    img = cv2.imread(f'{path}/{filename}')
    images.append(img)
    names.append(os.path.splitext(filename)[0])

def encode_faces(imgs):
    encodings = []
    for img in imgs:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings.append(face_recognition.face_encodings(img_rgb)[0])
    return encodings

known_encodings = encode_faces(images)

# Start camera
cap = cv2.VideoCapture(0)
last_seen_name = "Waiting..."
last_seen_time = time.time()
DISPLAY_DURATION = 5  # seconds to keep showing the name

while True:
    success, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    name_to_display = last_seen_name

    if face_encodings:
        for encode_face, face_loc in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, encode_face)
            face_distances = face_recognition.face_distance(known_encodings, encode_face)
            match_index = np.argmin(face_distances)

            if face_distances[match_index] < 0.45:
                name = names[match_index].upper()
                last_seen_name = name
                last_seen_time = time.time()
            else:
                name = "UNKNOWN"
                last_seen_name = name
                last_seen_time = time.time()

            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = y1 * 2, x2 * 2, y2 * 2, x1 * 2
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, name, (x1, y2 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    else:
        # If no face detected, continue showing previous name for 5 seconds
        if time.time() - last_seen_time < DISPLAY_DURATION:
            cv2.putText(frame, last_seen_name, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)

    cv2.imshow("Face Recognisation", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
