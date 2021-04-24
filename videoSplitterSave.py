import cv2
import numpy
from matplotlib import pyplot as plt

def video_splitter(referenceVideo):
    ref_video = cv2.VideoCapture(referenceVideo)
    hist_array = []
    count = 0

    while(ref_video.isOpened() == True):
        didLoad, frame = ref_video.read()
        if(didLoad == True):

            cv2.imwrite("frame%d.png" % count, frame)

            #success, image = ref_video.read()
            #print(success)

            count+=1
        else:
            break

    for each in range(count):
        currFrame = cv2.imread("frame" + str(each) + ".png", 0)
        new_histo = cv2.calcHist([currFrame], [0], None, [256], [0,256])
        hist_array.append(new_histo)

    #cv2.destroyAllWindows()
    return hist_array


if __name__ == "__main__":
    hist_array = video_splitter("/Users/lukemartin/PycharmProjects/yrrhacks2021/tests/im.mp4")
    print(len(hist_array))

    fml = cv2.imread("/Users/lukemartin/PycharmProjects/yrrhacks2021/tests/test_gbf.png",0)
    bruh = cv2.calcHist([fml], [0], None, [256], [0,256])

    """sim = []

    for each in hist_array:
        sim.append(cv2.compareHist(bruh, each, cv2.HISTCMP_CORREL))

    print(max(sim))
    print(sim.index(max(sim)))"""