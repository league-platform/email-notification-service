from fastapi import APIRouter, Request, HTTPException
from app.schemas import EmailRequest
from app.service import send_email
from app.models import email_record

router = APIRouter()

@router.post("/send-email", tags=["Email"])
async def send_email_endpoint(email: EmailRequest, request: Request):
    try:
        await send_email(email.to, email.subject, email.body)
        collection = request.app.database["emails"]
        await collection.insert_one(email_record(email.to, email.subject, email.body))
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/ping", tags=["Health"])
async def ping():
    return {"message": "pong"}
