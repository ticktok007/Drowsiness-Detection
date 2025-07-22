Drowsiness Detection
Table of Contents
About the Project

Features

How It Works

Prerequisites

Installation

Usage

Contributing

License

Contact

About the Project
This project implements a real-time drowsiness detection system using computer vision techniques. It primarily monitors a person's eyes to detect signs of fatigue, such as prolonged eye closure (blinking). When drowsiness is detected, an audible alarm is triggered to alert the user. This system can be particularly useful for drivers, students studying late, or anyone who needs to maintain alertness.

Features
Real-time Monitoring: Continuously analyzes video feed from a webcam.

Eye Blink Detection: Calculates the Eye Aspect Ratio (EAR) to determine if eyes are closed for an extended period.

Audible Alarm: Triggers a system beep when drowsiness is detected (e.g., eyes closed for too long).

User-friendly: Simple to set up and run.

How It Works
The system leverages the following computer vision concepts:

Facial Landmark Detection: Uses the dlib library's pre-trained facial landmark predictor to locate 68 key points on the face, specifically focusing on the eyes.

Eye Aspect Ratio (EAR): A metric derived from the eye landmarks to quantify the openness of the eyes. When the EAR falls below a certain threshold for a specified number of consecutive frames, it indicates a blink or eye closure.

Consecutive Frame Analysis: To avoid false positives from natural blinks or brief movements, the system checks if the eye closure condition persists for a predefined number of frames before triggering an alarm.

Alarm System: When the drowsiness criteria are met, a system beep is played to alert the user.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.7+

pip (Python package installer)

Windows Operating System (for the winsound module used for the alarm)

Installation
Follow these steps to get your development environment set up:

Clone the repository:

git clone https://github.com/ticktok007/drowsiness-detection.git
cd drowsiness-detection

Create a virtual environment (recommended):

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS: (Note: This project's alarm uses winsound, which is Windows-specific.)
source venv/bin/activate

Install the required Python packages:

pip install -r requirements.txt

The requirements.txt file should contain:

opencv-python
dlib
scipy
imutils

Note: dlib might require CMake and a C++ compiler to be installed on your system. Refer to dlib's official documentation for specific installation instructions if you encounter issues.

Download dlib's facial landmark predictor:
You'll need the shape_predictor_68_face_landmarks.dat file. You can download it from:
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
Extract the .bz2 file and place shape_predictor_68_face_landmarks.dat in the root directory of your project.

Usage
To run the drowsiness detection system, execute the main Python script:

python drowsiness_detection.py
The system will start capturing video from your default webcam. Press q to quit the application.

Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. Don't forget to give the project a star!

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request
Project Link: https://github.com/ticktok007/drowsiness-detection
