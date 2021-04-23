import cv2
import numpy
from matplotlib import pyplot as plt

def video_splitter(referenceVideo):
    ref_video = cv2.VideoCapture(referenceVideo)
    hist_array = []

    while(ref_video.isOpened() == True):
        didLoad, frame = ref_video.read()
        if(didLoad == True):
            new_histo = cv2.calcHist([frame], [0], None, [256], [0,255])
            hist_array.append(new_histo)
        else:
            break

    cv2.destroyAllWindows()
    return hist_array



if __name__ == "__main__":
    hist_array = video_splitter("tests/test_celeste.mp4")
    img = cv2.imread("tests/test_celeste.png", 0)
    img_hist = cv2.calcHist([img], [0], None, [256], [0, 255])
    similarity = []
    for histogram in hist_array:
        similarity.append(cv2.compareHist(img_hist, histogram, cv2.HISTCMP_CORREL))
    #print(similarity)
    with open("output.txt", "w") as txt_file:
        for line in similarity:
            txt_file.write(str(line) + "\n")
    print(max(similarity))
    print(similarity.index(max(similarity)))
    cap = cv2.VideoCapture("tests/test_celeste.mp4")
    cap.set(1, similarity.index(max(similarity)))
    ret, frame = cap.read() # Read the frame
    cv2.imshow('frame', frame)
    while True:
        ch = 0xFF & cv2.waitKey(1)
        if ch == 27:
            break

