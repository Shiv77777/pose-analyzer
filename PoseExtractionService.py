from mmpose.apis import MMPoseInferencer
from PIL import Image
import numpy as np

from Exceptions import CustomException

class PoseExtractionService:
    def __init__(self,modelname):
        self._modelname=modelname
        
    def ToImage(self,arr):
        try:
            return Image.fromarray(arr)
        except Exception as ex:
            raise Exception("Invalid array")
    
    def ExtractPose(self,frame,bbox):
        pil_image = self.ToImage(frame)
        region=pil_image.crop(bbox)
        try:
            inferencer = MMPoseInferencer(self._modelname)
            result_generator=inferencer(np.asarray(region),return_vis=True)
            result = next(result_generator)
        except Exception as ex:
            raise CustomException(message="Error getting pose from bounded region", code='500')
        result_pil=self.ToImage(result['visualization'][0])
        pil_image.paste(result_pil,bbox)
        final = np.asarray(pil_image)
        return final
        
        