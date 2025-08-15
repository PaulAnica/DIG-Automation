from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from get_credentials import CREDENTIALS

app = FastAPI()

class GmailFormData(BaseModel):
    firstName: str
    lastName: str
    email: str
    phoneNumber: str
    eventName: str
    tags: str

@app.get("/")
async def root():
    return JSONResponse({"message": "API running"})


@app.post("/form-submission")
async def form_submission(form: GmailFormData):

    return JSONResponse(content={"status": "received"}, status_code=200)


