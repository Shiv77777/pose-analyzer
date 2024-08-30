import cv2
from ultralytics import YOLO

from PoseExtractionService import PoseExtractionService

class DetectionService:
    def __init__(self):
        self._model = None
        self._poseExtractor=PoseExtractionService('human')
    
    def Detect(self,image):
        my_file = open("utils/coco.txt", "r")
        data = my_file.read()
        class_list = data.split("\n")
        my_file.close()
        model=YOLO('yolov8n.pt')
        detect_params = model.predict(source=[image], conf=0.7, save=False)
        DP = detect_params[0].numpy()
        if len(DP) != 0:
            boxes = detect_params[0].boxes
            color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            for i in range(len(detect_params[0])):
                box = boxes[i] 
                clsID = box.cls.numpy()[0]
                if(class_list[int(clsID)]=='person'): 
                    bb = box.xyxy.numpy()[0]
                    color_coverted=self._poseExtractor.ExtractPose(color_coverted,(int(bb[0]), int(bb[1]),int(bb[2]), int(bb[3])))
        return color_coverted
            