import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def check_inventory(beds: int) -> str | None:
    # Stub function to simulate checking unit availability
    # In a real app, this would query a database
    if 1 <= beds <= 3:
        return f"UNIT-{beds}0{beds}"
    return None

def send_tour_confirmation_email(recipient_email: str, name: str, unit_id: str, property_address: str):

    subject = "Your Tour Confirmation"
    body = f"""
    Hi {name},

    Your tour is confirmed!

    Property: {property_address}
    Unit: {unit_id}
    Suggested Tour Slot: Tuesday at 2:00 PM.

    Please let us know if you need to reschedule.

    Thanks,
    The Homewiz Team
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = os.getenv("GMAIL_USER")
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.getenv("GMAIL_USER"), os.getenv("GMAIL_PASS"))
            smtp.send_message(msg)
            print(f"Email sent to {recipient_email}")
    except Exception as e:
        # In a real app, log this error properly
        print(f"Failed to send email: {e}")