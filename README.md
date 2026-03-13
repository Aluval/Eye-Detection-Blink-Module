# 👁️ Eye Detection Blink Module

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![License](https://img.shields.io/badge/License-Apache%202.0-orange)
![Status](https://img.shields.io/badge/Project-Educational-brightgreen)

A real-time **Eye Blink Detection System** built using **Python and OpenCV** that detects human faces and eyes from a webcam stream and analyzes blinking using a simplified **Eye Aspect Ratio (EAR)** technique.

The module continuously monitors eye movement and detects **eye closure and blinking behavior** in real time.

---

# 👨‍💻 Developer

**Aluvala Ediga Harsha Vardhan Goud**  
MCA | AI & Machine Learning Enthusiast

---

# 📌 Project Overview

This project implements a **Computer Vision based Eye Blink Detection Module** that monitors eye activity through a webcam.

The system:

1. Detects the **face**
2. Detects **eyes inside the face region**
3. Calculates **Eye Aspect Ratio (EAR)**
4. Identifies **eye closure and blinking events**

If the eyes remain closed for multiple frames, the system can trigger alerts indicating possible fatigue or inactivity.

This module demonstrates how **AI-powered vision systems can monitor human behavior using real-time video analysis**.

---

# ⚙️ Features

- Real-time webcam monitoring
- Face detection using Haar Cascades
- Eye detection within face region
- Blink detection using EAR logic
- Continuous frame analysis
- Lightweight and efficient
- Educational implementation of computer vision concepts

---

# 🧠 Technologies Used

- Python
- OpenCV
- SciPy
- Computer Vision
- Haar Cascade Classifiers

---

# 📦 Python Modules Used

| Module | Purpose |
|------|------|
| `cv2 (OpenCV)` | Image processing and webcam capture |
| `time` | Frame timing and delays |
| `scipy.spatial.distance` | Distance calculations for blink detection |

---

# 🧩 System Workflow

```
Webcam Video → Face Detection → Eye Detection → EAR Calculation → Blink Detection
```

1️⃣ Webcam captures video frames  
2️⃣ Face detection identifies the face region  
3️⃣ Eye detection finds eyes within the face  
4️⃣ EAR is calculated from eye dimensions  
5️⃣ If EAR falls below threshold → **Eyes Closed**  
6️⃣ If closure continues → **Blink / Fatigue alert**

---

# 🌍 Applications / Use Cases

This module can be used in various **AI and safety-related sectors**, such as:

### 🚗 Driver Drowsiness Detection
Detects if drivers close their eyes for long periods and triggers alerts to prevent accidents.

### 🧠 Fatigue Monitoring Systems
Used in workplaces to monitor fatigue in high-risk environments.

### 🔐 Face Liveness Detection
Helps prevent spoofing attacks in **face recognition authentication systems**.

### 👨‍🦯 Assistive Technology
Can support systems designed for **visually impaired individuals**.

### 🤖 Human Computer Interaction
Used for gesture-based interfaces controlled by blinking.

### 🧪 Computer Vision Research
Useful for students and researchers studying **real-time video analysis**.

---

# 📁 Project Structure

```
Eye-Detection-Blink-Module
│
├── eyedetectionblink.py
├── README.md
```

---

# 💻 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/eye-detection-blink-module.git
cd eye-detection-blink-module
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python scipy
```

---

# ▶️ Running the Project

Run the Python script:

```bash
python eyedetectionblink.py
```

The webcam will start and detect **face, eyes, and blinking behavior in real time**.

Press **Q** to exit the program.

---

# 📚 Educational Purpose

This project was developed for **educational and research purposes** to demonstrate:

- Real-time computer vision
- Eye blink detection
- Human behavior monitoring
- Video frame analysis using OpenCV

It is useful for students learning **AI, Machine Learning, and Computer Vision**.

---

# ⚠️ Intellectual Property & Usage Notice

This project was originally developed by:

**Aluvala Ediga Harsha Vardhan Goud**

The code is shared for **educational and learning purposes**.

If you use or modify this project, **proper credit must be given to the original developer**.

Any individual or organization attempting to:

- Claim this code as their own work
- Mislead users regarding authorship
- Sell this code commercially without permission

may face **serious actions including DMCA takedown requests or legal notice where applicable**.

Please respect **open-source ethics and developer attribution**.

---

# ⭐ Support

If you found this project useful, please consider **starring the repository**.
