import cv2
import os

# Beach Aerial Footage Taken by a Drone.mp4

def ToFrames(filename):
    print(cv2.__version__)
    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    count = 0
    success = True
    foldername = filename.split('.')[0]
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    cwd = os.getcwd()
    directory = cwd + '\\'  +foldername
    while success:
        completeName = os.path.join(directory, "frame%d.jpg" % count)
        cv2.imwrite(completeName, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count += 1
    print("%d frames are generated" % count)


if __name__=="__main__":
    ToFrames('Beach Aerial Footage Taken by a Drone.mp4')