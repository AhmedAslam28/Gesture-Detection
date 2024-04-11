import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

# Define constants
NUM_CLASSES = 10
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 10
LEARNING_RATE = 0.001

# Function to preprocess video frames
def preprocess_frame(frame):
    frame = cv2.resize(frame, IMAGE_SIZE)
    frame = frame / 255.0  # Normalize pixel values to [0, 1]
    return frame

# Load and preprocess videos from a directory structure
def load_video_dataset(dataset_dir):
    class_dirs = sorted(os.listdir(dataset_dir))
    videos = []
    labels = []

    for label_idx, class_dir in enumerate(class_dirs):
        class_path = os.path.join(dataset_dir, class_dir)
        video_files = os.listdir(class_path)

        for video_file in video_files:
            video_path = os.path.join(class_path, video_file)
            cap = cv2.VideoCapture(video_path)

            frames = []
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = preprocess_frame(frame)
                frames.append(frame)
            
            # Only use videos with at least 16 frames
            if len(frames) >= 16:
                videos.append(frames[:16])  # Use first 16 frames
                labels.append(label_idx)
            
            cap.release()

    return np.array(videos), np.array(labels)

# Define the model architecture
base_model = MobileNetV2(input_shape=(*IMAGE_SIZE, 3), include_top=False, weights='imagenet')
x = GlobalAveragePooling2D()(base_model.output)
x = Dense(128, activation='relu')(x)
outputs = Dense(NUM_CLASSES, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=outputs)

# Compile the model
optimizer = Adam(learning_rate=LEARNING_RATE)
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Load the dataset
dataset_dir = r'C:\Users\Aslam\Gesturedetection\UCF101_Action_detection_splits'

videos, labels = load_video_dataset(dataset_dir)

# Train the model
model.fit(videos, labels, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_split=0.2)

# Save the trained model
model.save('gesture_recognition_model.h5')


