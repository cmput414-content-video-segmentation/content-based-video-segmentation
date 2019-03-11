# video from
# https://videos.pexels.com/videos/beach-aerial-footage-taken-by-a-drone-854218
from VideoHandler import ToFrames
import numpy as np
import matplotlib.pyplot as plt
Threshold = 0.65
def videoSegment(filename):
    frames = ToFrames(filename)
    prev = frames.GetCurrent()
    image = frames.GetNext()
    sub = []
    total = []
    while(type(image) == np.ndarray):
        total.append(int(image.sum()))
        dif = np.absolute(prev - image)
        sub.append(int(dif.sum()))
        prev = image
        image = frames.GetNext()
    sublen = len(sub)
    numframes = 1
    avg = sub[0]
    for i in range(1,sublen):
        # difference = abs(sub[i] - sub[i-1])
        difference = abs(sub[i] - avg)
        numframes = numframes+1
        per = 1/numframes
        avg = avg*(1-per) + per*sub[i]
        if difference/avg>Threshold:
            print(i)
            print(difference/avg)
            numframes = 1
            avg = sub[i]
        if i == 281:
            print(i)
            print(difference / avg)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(sub)
    plt.ylabel('difference')
    plt.xlabel('frames')

    # plt.show()
    plt.subplot(212)

    plt.plot(total)
    plt.ylabel('values')
    plt.xlabel('frames')

    plt.show()

if __name__=="__main__":
    videoSegment('Beach Aerial Footage Taken by a Drone.mp4')