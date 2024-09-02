# Hand Gesture Tracker for Fruit Ninja

## Overview

This project uses computer vision to track hand gestures, enabling interaction with games like Fruit Ninja. The program opens the camera, processes video frames, and draws points on detected hand landmarks using MediaPipe. When two specific points on the hand (landmarks 4 and 12) are brought close together, it simulates a left mouse click.

## Libraries Used

- **OpenCV (`cv2`)**: Opens the camera and processes video frames.
- **MediaPipe**: Detects hand landmarks and draws points on the hand.
- **PyAutoGUI**: Resizes frames and simulates mouse movement.
- **Mouse**: Simulates mouse clicks.
- **Math**: Performs mathematical calculations for gesture detection.

## How It Works

![image](https://github.com/user-attachments/assets/f619338e-4b4d-44c2-adc6-be727e65853d)

1. **Camera Initialization**: Opens the camera and reads frames.
2. **Frame Processing**: Copies the current frame for manipulation.
3. **Hand Detection**: Uses MediaPipe to detect hand landmarks.
4. **Gesture Recognition**: Identifies landmarks 4 and 12; if they are close together, triggers a mouse click.
5. **Mouse Interaction**: Simulates mouse actions based on hand gestures.

## Usage

- Run the script to start tracking hand gestures.
- Bring landmarks 4 and 12 close together to simulate a left mouse click.
- Press "q" to exit the program.

## Installation

Ensure you have the required libraries installed:

```bash
pip install opencv-python mediapipe pyautogui mouse
