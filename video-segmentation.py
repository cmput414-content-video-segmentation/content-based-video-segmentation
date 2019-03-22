# video from
# https://videos.pexels.com/videos/beach-aerial-footage-taken-by-a-drone-854218
from VideoHandler import ToFrames
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
CV_COMP_CORREL = 0
colors = ('b','g','r')
Threshold = 35
def videoSegment(filename):
    frames = ToFrames(filename)
    prev = frames.GetCurrent()
    image = frames.GetNext()
    sub = []
    total = []
    gray_sub = []
    gray_total = []
    histgrams = []
    # histb = []
    g_prev = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    g_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # tempout = temp
    # cv2.equalizeHist(temp,tempout)
    # histgrams.append(tempout)
    # histb.append( cv2.calcHist([image], [0], None, [256], [0, 256]))

    # print(len(image.ravel()))
    # # plt.hist(image.ravel(), 256, [0, 256])
    # histg = cv2.calcHist([image], [0], None, [256], [0, 256])
    # print(len(histg[0]))
    # plt.plot(histg)
    #
    # plt.xlim([0, 256])
    # # cv2.compareHist(prev,image,method=CV_COMP_CORREL)
    # plt.show()


    while(type(image) == np.ndarray):
        g_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        total.append(int(image.sum()))
        gray_total.append(int(g_image.sum()))
        dif = np.absolute(prev - image)
        sub.append(int(dif.sum()))
        gdif = np.absolute(g_prev - g_image)
        gray_sub.append(int(gdif.sum()))
        prev = image
        g_prev = g_image
        image = frames.GetNext()

        # grayscale.append(temp)
        # tempout = temp
        # cv2.equalizeHist(temp, tempout)
        # histgrams.append(tempout)
        # histb.append(cv2.calcHist([image], [0], None, [256], [0, 256]))

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
    plt.show()

    plt.figure(2)
    plt.subplot(211)
    plt.plot(gray_sub)
    plt.ylabel('gray difference')
    plt.xlabel('frames')
    plt.subplot(212)
    plt.plot(gray_total)
    plt.ylabel('gray values')
    plt.xlabel('frames')
    plt.show()





if __name__=="__main__":
    videoSegment('Beach Aerial Footage Taken by a Drone.mp4')