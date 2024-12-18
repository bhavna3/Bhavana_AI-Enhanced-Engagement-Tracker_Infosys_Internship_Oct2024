# -*- coding: utf-8 -*-
"""detect emotions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pio1Ji_jdCgP2eB9MpiomZpcep58MnSo
"""

# Install necessary packages
# pip install opencv-python-headless deepface matplotlib numpy

import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt
import numpy as np

# Function to load an image from file
def load_image(file_path):
    # Read the image
    img = cv2.imread(file_path)
    if img is None:
        raise ValueError(f"Could not load image from {file_path}")
    return img

# Function to draw results on image
def draw_results(image, face_info):
    # Make a copy of the image to draw on
    img_copy = image.copy()

    # Get face rectangle coordinates
    x = face_info['region']['x']
    y = face_info['region']['y']
    w = face_info['region']['w']
    h = face_info['region']['h']

    # Draw rectangle around face
    cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Get emotion probabilities
    emotions = face_info['emotion']
    dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]

    # Create text to display
    text = f"{dominant_emotion}: {emotions[dominant_emotion]:.1f}%"

    # Add text above the rectangle
    cv2.putText(img_copy, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return img_copy, emotions

# Main function
def main():
    # Specify the path to your image file
    file_path = input("Enter the path to the image file: ")

    try:
        # Load the image
        img = load_image(file_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Analyze face
        analysis = DeepFace.analyze(img_rgb,
                                   actions=['emotion'],
                                   detector_backend='opencv',
                                   enforce_detection=True)

        # Handle result whether it's a list or single dictionary
        if isinstance(analysis, list):
            face_info = analysis[0]
        else:
            face_info = analysis

        # Draw results on image
        result_image, emotions = draw_results(img_rgb, face_info)

        # Create figure with two subplots
        plt.figure(figsize=(15, 5))

        # Plot original image
        plt.subplot(1, 2, 1)
        plt.imshow(img_rgb)
        plt.title('Original Image')
        plt.axis('off')

        # Plot result image
        plt.subplot(1, 2, 2)
        plt.imshow(result_image)
        plt.title('Detected Emotion')
        plt.axis('off')

        plt.show()

        # Print emotion probabilities
        print("\nEmotion Probabilities:")
        for emotion, probability in emotions.items():
            print(f"{emotion}: {probability:.1f}%")

    except Exception as e:
        print(f"Error: {str(e)}")

# Run the main function
if __name__ == "__main__":
    main()