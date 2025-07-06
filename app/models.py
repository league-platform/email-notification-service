from datetime import datetime

def email_record(to: str, subject: str, body: str) -> dict:
    return {
        "to": to,
        "subject": subject,
        "body": body,
        "sent_at": datetime.utcnow()
    }
