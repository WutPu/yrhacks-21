import cv2
import numpy as np
from matplotlib import pyplot as plt
import datetime
import argparse

similarity = []
frame_count = 0

img = cv2.imread("tests/test_celeste.png", 0)
cap = cv2.VideoCapture("tests/test_celeste.mp4")
video_width, video_height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_fps = int(cap.get(cv2.CAP_PROP_FPS))
img = cv2.resize(img, (video_width, video_height))

while(cap.isOpened() == True):
    did_load, frame = cap.read()
    if(did_load == True):
        if(frame_count % video_fps == 0):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            value = float(cv2.matchTemplate(frame, img, cv2.TM_CCORR_NORMED)[0])
            similarity.append((frame_count, value))
        frame_count += 1
    else:
        break

similarity.sort(key = lambda x : x[1], reverse = True)
highest_value = similarity[0][1]
similarity[:] = [x for x in similarity if x[1]/highest_value >= 0.995]
print(similarity)

fig = plt.figure("Frames")

for i in range(len(similarity)):
    frame, value = similarity[i]
    cap.set(1, frame)
    _, image = cap.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    seconds = frame / video_fps
    timestamp = datetime.timedelta(seconds = seconds)
    show_image = fig.add_subplot(1, len(similarity), i + 1)
    show_image.set_title(timestamp)
    plt.axis("off")
    plt.imshow(image)

plt.show()