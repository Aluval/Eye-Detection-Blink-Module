import cv2
import time
from scipy.spatial import distance

# Load pre-trained Haar Cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Function to compute the Eye Aspect Ratio (EAR) using the eye's bounding box coordinates
def simplified_ear(eye):
    w = eye[2]  # width of the bounding box
    h = eye[3]  # height of the bounding box
    ear = h / float(w)  # simplified EAR calculation (height/width ratio)
    return ear

# Threshold for detecting closed eyes
EAR_THRESHOLD = 0.20  # Lower threshold for increased sensitivity
CONSECUTIVE_FRAMES = 48  # Number of consecutive frames eyes need to stay closed

# Initialize variables
blink_count = 0
eyes_closed = False  # Track whether eyes are currently closed

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Region of interest (ROI) for eyes
        roi_gray = gray[y:y + h, x:x + w]

        # Detect eyes in the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            # Sort eyes by x-coordinate to differentiate between left and right eyes
            eyes = sorted(eyes, key=lambda e: e[0])

            # Compute EAR for both eyes
            left_eye = eyes[0]
            right_eye = eyes[1]
            left_ear = simplified_ear(left_eye)
            right_ear = simplified_ear(right_eye)

            # Average EAR for both eyes
            ear = (left_ear + right_ear) / 2.0
            print(f"Left EAR: {left_ear}, Right EAR: {right_ear}, Average EAR: {ear}")

            # Check if EAR is below the threshold (eyes closed)
            if ear < EAR_THRESHOLD:
                if not eyes_closed:  # Eyes just closed
                    eyes_closed = True
                    blink_count += 1
                    print(f"Eyes closed! Blink count: {blink_count}")
                else:
                    print("Eyes still closed.")
            else:
                eyes_closed = False  # Eyes open
                blink_count = 0
                print("Eyes open. Blink count reset.")

            # Alert if eyes are closed for more than 48 frames
            if blink_count >= CONSECUTIVE_FRAMES:
                print("Eyes closed for 2 seconds!")
        else:
            print("Not enough eyes detected.")

    # Add a text overlay: “DEV : ALUVALA EDIGA HARSHA VARDHAN GOUD” on the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "DEV : ALUVALA EDIGA HARSHA VARDHAN GOUD"
    position = (10, frame.shape[0] - 10)  # Position near the bottom-left corner
    cv2.putText(frame, text, position, font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame with the text overlayqq
    frame = cv2.resize(frame, (640, 480))  # Resize frame if necessary
    cv2.imshow("Frame", frame)

    # Exit loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
