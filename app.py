from fastapi import FastAPI
import uvicorn, sys, os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.TextSummarizer.pipeline.prediction import PredictionPipeline

text: str = "What is Text Summarization?"

app = FastAPI()

@app.get('/', tags=["authetication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Successful !!")

    except Exception as e:
        return Response(f"Error occured! {e}")
    

@app.get("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3000)
