import cv2
import mediapipe as mp
import pyautogui
import mouse
import math

#find hands in image
def find(img):
    results = hands.process(img)
    return results

def find_X_Y_fingers(results, W, H):
    finger_x, finger_y = results.x * W, results.y * H
    return finger_x, finger_y

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    W_H = pyautogui.size()

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    while True:
        success, img = cap.read()

        img = img[:, ::-1]

        img = cv2.resize(img, W_H)

        img_copy = img.copy()

        results = find(img[:, :, ::-1])

        if results.multi_hand_landmarks:
            finger_x_one , finger_y_one = find_X_Y_fingers(results.multi_hand_landmarks[0].landmark[12], W_H[0], W_H[1])

            finger_x_two , finger_y_two = find_X_Y_fingers(results.multi_hand_landmarks[0].landmark[2], W_H[0], W_H[1])

            cv2.circle(img_copy, (int(finger_x_one), int(finger_y_one)), 50, (255, 0, 0), -1)

            cv2.circle(img_copy, (int(finger_x_two), int(finger_y_two)), 50, (255, 0, 0), -1)

            cv2.circle(img_copy, (int(finger_x_two+((finger_x_one - finger_x_two) / 2)), int(finger_y_one + ((finger_y_two - finger_y_one) / 2))), 20, (0, 0, 255), -1)

            X = finger_x_one - finger_x_two if finger_x_one - finger_x_two > 0 else finger_x_two - finger_x_one
            Y = finger_y_one - finger_y_two if finger_y_one - finger_y_two > 0 else finger_y_two - finger_y_one

            if X < 170 and Y < 170:
                mouse.press()
                mouse.move(finger_x_one+((finger_x_two - finger_x_one) / 2) +10, finger_y_one + ((finger_y_two - finger_y_one) / 2) +25)

            else:
                mouse.release()
                mouse.move(finger_x_one + ((finger_x_two - finger_x_one) / 2) + 10, finger_y_one + ((finger_y_two - finger_y_one) / 2) + 25)

        img_copy = cv2.resize(img_copy, (640, 480))
        cv2.imshow('img_copy', img_copy)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    cap.release()
    cv2.destroyAllWindows()