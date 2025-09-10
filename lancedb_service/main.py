from fastapi import FastAPI
import lancedb

app = FastAPI()
db = lancedb.connect("/data/lancedb")

@app.get("/")
def root():
    return {"message": "LanceDB API running"}