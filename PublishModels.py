from pydantic import BaseModel

class PublishResponse(BaseModel):
    ProcessStatus:str

class PublishRequest(BaseModel):
    process: str
    correlationId:str