import datetime
from memory.invoice_db import list_pending, set_reminder_sent

def get_reminders():
    return list_pending()

def mark_sent(rid: int):
    return set_reminder_sent(rid)
