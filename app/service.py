import aiosmtplib
from email.message import EmailMessage
from app.config import settings

async def send_email(to: str, subject: str, body: str):
    message = EmailMessage()
    message["From"] = settings.SMTP_USER
    message["To"] = to
    message["Subject"] = subject
    message.set_content(body)

    print(f"EVENT: email.send -> Sending email to {to}")  # Event simulation

    await aiosmtplib.send(
        message,
        hostname=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        username=settings.SMTP_USER,
        password=settings.SMTP_PASSWORD,
        start_tls=True,
    )
