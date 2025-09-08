from django.apps import AppConfig
from fastapi import FastAPI
import lancedb

class LancedbServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lancedb_service'

app = FastAPI()

# Connect to LanceDB inside the container
db = lancedb.connect("/data/lancedb")

@app.get("/")
def root():
    return {"message": "LanceDB API running"}

@app.get("/tables")
def list_tables():
    return {"tables": db.table_names()}
