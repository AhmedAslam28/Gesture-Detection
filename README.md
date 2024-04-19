 # Thumbs-Up Gesture Detection

## Overview 
This project focuses on detecting the thumbs-up gesture using basic image processing techniques, particularly contour detection. The goal is to develop a simple yet effective method to recognize the thumbs-up gesture from images or video frames. By utilizing contour detection and other fundamental image processing tools, this project aims to provide a straightforward solution for gesture recognition.

## Key Features:
- Thumbs-up gesture detection using OpenCV and Python.
- Basic image preprocessing and contour extraction techniques.
- Demonstrates how to apply image processing for gesture recognition tasks.
- Includes a web interface for uploading videos to perform real-time gesture detection.

## Web Interface:
- The project provides a web-based interface where users can upload videos to detect the thumbs-up gesture in real time.
- The interface utilizes Flask, a lightweight web framework for Python, to handle video uploads and display the processed results.
  ![Alt Text](https://github.com/AhmedAslam28/Gesture-Detection/blob/ad362786d8976a893fc3b659fb76262e4545cadb/Gesture%20outputs/web%20page.jpg)

## Contour Detection
- Processes input frame to detect thumbs-up gesture.
- Converts frame to grayscale and applies Gaussian blur.
- Thresholds image to create binary representation.
- Identifies contours of objects in binary image.
- Validates largest contour as thumbs-up based on area and aspect ratio.
- Returns position of thumbs-up gesture if detected.
![Alt Text](https://github.com/AhmedAslam28/Gesture-Detection/blob/a16c41d81180d225f4382cb82a56338c156f2a03/Gesture%20outputs/contour%20.jpg)

## Gesture Detetcion Output
-When a thumbs-up gesture is detected in a streamed video, this project displays corresponding text overlay to indicate the recognition result in real time.
-The text appears dynamically on the video feed, providing immediate feedback upon gesture detection.
### Detecion1
![Alt Text](https://github.com/AhmedAslam28/Gesture-Detection/blob/cecc9e83658af1eb76ccb8c6270809982732280f/Gesture%20outputs/detection1.jpg)

### Detection2
![Alt Text](https://github.com/AhmedAslam28/Gesture-Detection/blob/cecc9e83658af1eb76ccb8c6270809982732280f/Gesture%20outputs/detection2.jpg)
