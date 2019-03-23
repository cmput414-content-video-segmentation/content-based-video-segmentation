# video from
# https://videos.pexels.com/videos/beach-aerial-footage-taken-by-a-drone-854218
from VideoHandler import ToFrames
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
CV_COMP_CORREL = 0
COLORS = ('b','g','r')
Threshold = 35

def traditional_method(image, hist_mean, hist_previous):
    summean = 0
    sumprev = 0
    currenthist = []

    for i, col in enumerate(COLORS):
        histr = cv2.calcHist([image], [i], None, [256], [0, 256])
        summean = summean + abs(hist_mean[i] - histr)
        sumprev = sumprev + abs(hist_previous[i] - histr)
        currenthist.append(histr)

    return summean, sumprev, currenthist

def Otsu(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
    return ret, thr


def videoSegment(filename):
    frames = ToFrames(filename)
    prev = frames.GetCurrent()
    image = frames.GetNext()
    sub = []
    total = []
    hist_mean = []
    hist_previous = []
    threasholds = []
    Otsudifference = []
    threas, Otsuprev = Otsu(prev)
    threasholds.append(threas)
    # initialize hist_previous and hist_mean
    for i, col in enumerate(COLORS):
        histr = cv2.calcHist([prev], [i], None, [256], [0, 256])
        hist_mean.append(histr)
        hist_previous.append(histr)


    while(type(image) == np.ndarray):
        total.append(int(image.sum()))
        dif = np.absolute(prev - image)
        sub.append(int(dif.sum()))
        prev = image
        # summean, sumprev, currenthist = traditional_method(image, hist_mean, hist_previous)
        # hist_previous = currenthist
        threas, Otsucurrent = Otsu(image)
        threasholds.append(threas)
        dif = np.absolute(Otsucurrent - Otsuprev)
        Otsudifference.append(int(dif.sum()))
        Otsuprev = Otsucurrent
        image = frames.GetNext()


    # sublen = len(sub)
    # numframes = 1
    # avg = sub[0]
    # for i in range(1,sublen):
    #     # difference = abs(sub[i] - sub[i-1])
    #     difference = abs(sub[i] - avg)
    #     numframes = numframes+1
    #     per = 1/numframes
    #     avg = avg*(1-per) + per*sub[i]
    #     if difference/avg>Threshold:
    #         print(i)
    #         print(difference/avg)
    #         numframes = 1
    #         avg = sub[i]
    #     if i == 281:
    #         print(i)
    #         print(difference / avg)
    totlen = len(total)
    # numframes = 1
    predifference = total[0]

    for i in range(1,totlen):
        difference = abs(total[i] - total[i-1])

        # if difference>math.exp(10):
        #     print(i)
        if difference>predifference:
            predifference = difference

    # cv2.imshow("equalizeHist", histgrams[0])
    # cv2.imshow("grayscale", grayscale[0])
    # plt.hist(grayscale[0].ravel(), 256, [0, 256], color='r')
    # plt.legend('histogram')
    # plt.show()
    #     8
#     9
#
#
#
# 10
#
# 11
# 12
# plt.plot(cdf_normalized, color='b')
# 13
# plt.hist(img.flatten(), 256, [0, 256], color='r')
# 14
# plt.xlim([0, 256])
# 15
# plt.legend(('cdf', 'histogram'), loc='upper left')
# 16
# plt.show()


    print(predifference)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(sub)
    plt.ylabel('difference')
    plt.xlabel('frames')
    plt.subplot(212)
    plt.plot(total)
    plt.ylabel('values')
    plt.xlabel('frames')

    plt.figure(2)
    plt.subplot(211)
    plt.plot(Otsudifference)
    plt.ylabel('gray difference')
    plt.xlabel('frames')
    plt.subplot(212)
    plt.plot(threasholds)
    plt.ylabel('gray values')
    plt.xlabel('frames')


    dx = 1
    dy = np.diff(total)/dx
    dsub = np.diff(sub)/dx
    plt.figure(3)
    plt.subplot(211)
    plt.plot(dsub)
    plt.ylabel('gray difference')
    plt.xlabel('frames')
    plt.subplot(212)
    plt.plot(dy)
    plt.ylabel('gray values')
    plt.xlabel('frames')

    dy = np.diff(threasholds)/dx
    dsub = np.diff(Otsudifference)/dx
    plt.figure(4)
    plt.subplot(211)
    plt.plot(dsub)
    plt.ylabel('gray difference')
    plt.xlabel('frames')
    plt.subplot(212)
    plt.plot(dy)
    plt.ylabel('gray values')
    plt.xlabel('frames')
    plt.show()

if __name__=="__main__":
    videoSegment('Beach Aerial Footage Taken by a Drone.mp4')