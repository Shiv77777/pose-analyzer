import cv2

from DetectionService import DetectionService
from Exceptions import CustomException
from PoseAnalysisModels import PoseAnalysisResponse
from ObjectDetectionModels import ObjectDetectionResponse

class PoseAnalysisService:
    def __init__(self,path):
        self._vidPath = path
        self._objDetector = DetectionService()
        self._outDir = './output/'
        
    async def ProcessVideo(self):
        try:
            cap = cv2.VideoCapture(self._vidPath)
        except Exception as ex:
            raise CustomException(message='invalid file path',code='400')
        
        i=0
        while True:
            ret,frame = cap.read()
            if not ret:
                break
            cv2.resize(frame,(640,360))
            detectionResult=self._objDetector.Detect(frame)
            op = ObjectDetectionResponse(imageArray=detectionResult)
            fpath = f"{self._outDir}frame_{i}.png"
            cv2.imwrite(fpath,op)
            i=i+1   
        cap.release()
        cv2.destroyAllWindows()
        res=PoseAnalysisResponse(Status='200',Message=f"saved video to {self._outDir}")  
        return res