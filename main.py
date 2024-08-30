import uuid
from fastapi import FastAPI

from Exceptions import CustomException
from PoseAnalysisModels import PoseAnalysisRequest,PoseAnalysisResponse
from PoseAnalysisService import PoseAnalysisService
from PublishModels import PublishRequest,PublishResponse

app = FastAPI()

@app.get("/")
async def hello():
    return {"Hello": "World"}

@app.post("/PoseAnalysis")
async def modeloutput(request: PoseAnalysisRequest)->PoseAnalysisResponse:
    correlationId = uuid.uuid4
    res = PoseAnalysisResponse(correlationId=str(correlationId))
    try:
        poseAnalysis = PoseAnalysisService(request.path)
        res=await poseAnalysis.ProcessVideo()
    except CustomException as cex:
        res.Message=cex.message
        res.Status=cex.code
    except Exception as ex:
        res.Message=str(ex)
        res.Status='500'
    finally:
        return res
    
@app.post("/PoseAnalysisDecoupled")
async def decoupledoutput(request: PoseAnalysisRequest)->PoseAnalysisResponse:
    res = PoseAnalysisResponse()
    try:
        poseAnalysis = PoseAnalysisService(request.path)
        pid=uuid.uuid4
        pro = PublishRequest(process='PoseAnalysisDecoupled',pid=pid)
        publish(pro)
        res.Message="queued"
        res.pid=pid
        res.Status='200'
    except Exception as ex:
        res.Message=str(ex)
    finally:
        return res

@app.post("/Publish")
async def publish(request:PublishRequest)->PublishResponse:
    #queueName=getQueueName(request.process)
    #queueObject
    pass
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)