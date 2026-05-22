import cv2
import mediapipe as mp
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
# kamera
camera = cv2.VideoCapture(0)

# model
base_options = python.BaseOptions(
    model_asset_path="hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)
last_x = None

last_update = time.time()
last_move_time = time.time()
video_active = False
video_timer = time.time()

moves = []
pattern = [0,1,0,1]
pattern2 = [1,0,1,0]
while True:
    current_time = time.time()

    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

#PLAYER 
    if video_active:
        ret, video_frame = video.read()

        if ret:

            cv2.imshow("SCUBA CAT", video_frame)

        else:

            video_active = False

            video.release()



#-----------------------
    if result.hand_landmarks:
        
        for hand in result.hand_landmarks:
            
            pointer = hand[8]
            h, w, _ = frame.shape

            x = int(pointer.x * w)
            y = int(pointer.y * h)
            current_time = time.time()
            if current_time - last_update > 0.2:
                if last_x is not None:

                    movement = x - last_x
                    if current_time - last_move_time >= 2:
                        moves.clear()
                    if movement > 30:
                        print("➡️ PRAWO")
                        moves.append(0)
                    elif movement < -30:
                        print("⬅️ LEWO")
                        moves.append(1)

                    if len(moves) > 6:
                        moves.pop(0)
                    #filmik
                    if moves[-4:] == pattern or moves[-4:] == pattern2:
                        if not video_active:
                            print("SCUBA CAT ACTIVATED")

                            video_active = True

                            video = cv2.VideoCapture("scubacat.mp4")


                last_update = current_time
                last_x = x
                last_move_time = current_time
            for landmark in hand:

                h, w, _ = frame.shape

                x = int(landmark.x * w)
                y = int(landmark.y * h)

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()