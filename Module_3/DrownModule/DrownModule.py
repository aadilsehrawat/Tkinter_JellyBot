import cv2

def main_drownModule(name):
    videoName = 'data/videos/'+name #'DJI_0209.MP4'

    #create a videoCapture Object (this allow to read frames one by one)
    video = cv2.VideoCapture(videoName)
    #check it's ok
    if video.isOpened():
        print('Video Succefully opened')
    else:
        print('Something went wrong check if the video name and path is correct')


    #define a scale lvl for visualization
    scaleLevel = 1 #it means reduce the size to 0**(scaleLevel-1)


    windowName = 'Video Reproducer'
    cv2.namedWindow(windowName )
    #let's reproduce the video
    while True:
        ret,frame = video.read() #read a single frame 
        if not ret: #this mean it could not read the frame 
            print("Could not read the frame")   
            cv2.destroyWindow(windowName)
            break

        reescaled_frame  = frame
        for i in range(scaleLevel-1):
            reescaled_frame = cv2.pyrDown(reescaled_frame)

        cv2.imshow(windowName, reescaled_frame )

        waitKey = (cv2.waitKey(1) & 0xFF)
        if  waitKey == ord('q'): #if Q pressed you could do something else with other keypress
            print("closing video and exiting")
            cv2.destroyWindow(windowName)
            video.release()
            break