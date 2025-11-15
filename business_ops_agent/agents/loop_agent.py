import threading
import time
from memory.invoice_db import auto_overdue_update

def loop():
    while True:
        auto_overdue_update()
        time.sleep(86400)  # 24 hours

def start_daily_loop():
    t = threading.Thread(target=loop, daemon=True)
    t.start()
