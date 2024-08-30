from mmpose.apis import MMPoseInferencer
from PIL import Image
import numpy as np

class PoseExtractionService:
    def __init__(self,modelname):
        self._modelname=modelname
    
    def ExtractPose(self,frame,bbox):
        pil_image = Image.fromarray(frame)
        region=pil_image.crop(bbox)
        inferencer = MMPoseInferencer(self._modelname)
        result_generator=inferencer(np.asarray(region),return_vis=True)
        result = next(result_generator)
        result_pil=Image.fromarray(result['visualization'][0])
        pil_image.paste(result_pil,bbox)
        final = np.asarray(pil_image)
        return final
        
        