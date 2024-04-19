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

## Contour Detection
- Processes input frame to detect thumbs-up gesture.
- Converts frame to grayscale and applies Gaussian blur.
- Thresholds image to create binary representation.
- Identifies contours of objects in binary image.
- Validates largest contour as thumbs-up based on area and aspect ratio.
- Returns position of thumbs-up gesture if detected.
