from fastapi import FastAPI
from pydantic import BaseModel

from PoseAnalysisService import PoseAnalysisService

app = FastAPI()

class PoseAnalysisRequest(BaseModel):
    path: str

@app.get("/")
async def hello():
    return {"Hello": "World"}

@app.post("/PoseAnalysis")
async def modeloutput(request: PoseAnalysisRequest):
    poseAnalysis = PoseAnalysisService(request.path)
    return poseAnalysis.ProcessVideo()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)