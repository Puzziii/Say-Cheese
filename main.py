from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from routes.analyze import router 

load_dotenv()

app = FastAPI(title="Say Cheese")

app.include_router(router,prefix="/api")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")