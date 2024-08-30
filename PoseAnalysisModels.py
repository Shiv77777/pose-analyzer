from typing import Optional
from pydantic import BaseModel

class PoseAnalysisRequest(BaseModel):
    path: str
    
class PoseAnalysisResponse(BaseModel):
    Message: Optional[str] = None
    Status: Optional[str] = None
    correlationId:str