cd YOLO(YouOnlyLookOnce)PersonDetection/darknet
make

wget https://pjreddie.com/media/files/yolov3.weights

./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg