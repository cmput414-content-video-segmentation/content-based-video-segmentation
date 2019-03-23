import cv2
import os

# Beach Aerial Footage Taken by a Drone.mp4
class ToFrames():

    def __init__(self, filename):
        print("opencv version: "+cv2.__version__)
        self.vidcap = cv2.VideoCapture(filename)

        # imagesize is 800*450*3
        self.success, self.image = self.vidcap.read()
        # count = 0
        # success = True
        # foldername = filename.split('.')[0]
        # if not os.path.exists(foldername):
        #     os.makedirs(foldername)
        # cwd = os.getcwd()
        # directory = cwd + '\\' + foldername
        # while success:
        #     completeName = os.path.join(directory, "frame%d.jpg" % count)
        #     cv2.imwrite(completeName, image)  # save frame as JPEG file
        #     success, image = vidcap.read()
        #     count += 1
        # print("%d frames are generated" % count)
    def GetCurrent(self):

        return self.image

    def GetNext(self):
        self.success, self.image = self.vidcap.read()
        if self.success:
            return self.image
        else:
            return False

# def ToFrames (filename):
#         print("opencv version: "+cv2.__version__)
#         vidcap = cv2.VideoCapture(filename)
#
#         # imagesize is 800*450*3
#         success, image = vidcap.read()
#         count = 0
#         success = True
#         foldername = filename.split('.')[0]
#         if not os.path.exists(foldername):
#             os.makedirs(foldername)
#         cwd = os.getcwd()
#         directory = cwd + '\\' + foldername
#         while success:
#             completeName = os.path.join(directory, "frame%d.jpg" % count)
#             cv2.imwrite(completeName, image)  # save frame as JPEG file
#             success, image = vidcap.read()
#             count += 1
#         print("%d frames are generated" % count)
# if __name__=="__main__":
#     ToFrames('Beach Aerial Footage Taken by a Drone.mp4')