import os
import cv2

from DetectionService import DetectionService

class PoseAnalysisService:
    def __init__(self,path):
        self._vidPath = path
        self._objDetector = DetectionService()
        
    def ProcessVideo(self):
        cap = cv2.VideoCapture(self._vidPath)
        i=0
        while True:
            ret,frame = cap.read()
            if not ret:
                break
            cv2.resize(frame,(640,360))
            op=self._objDetector.Detect(frame)
            
            cv2.imwrite(f"output/frame_{i}.png",op)
            i=i+1   
        cap.release()
        cv2.destroyAllWindows()  
        return "saved video"