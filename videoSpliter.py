import cv2
import numpy
from matplotlib import pyplot as plt

def videoSplitter(referenceVideo):
    ref_video = cv2.VideoCapture(referenceVideo)
    hista_array = []

    while(ref_video.isOpened() == True):
        didLoad, frame = ref_video.read()
        if(didLoad == True):

            new_histo = cv2.calcHist([frame], [0], None, [256], [0,255])

            hista_array.append(new_histo)

        else:
            break

    cv2.destroyAllWindows()

    return hista_array



if __name__ == "__main__":
    hista_array = videoSplitter("/Users/lukemartin/PycharmProjects/yrrhacks2021/tests/test_celeste.mp4")