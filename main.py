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
    print(form.firstName, form.lastName, form.email, form.phoneNumber, form.eventName, form.tags)
    form_dict = form.model_dump()
    print("As dictionary:", form_dict)
    return JSONResponse(content={"status": "received", "data": form_dict}, status_code=200)


