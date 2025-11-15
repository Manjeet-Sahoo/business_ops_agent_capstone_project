import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///./invoices.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    invoice_id = Column(String)
    vendor = Column(String)
    date = Column(String)
    total = Column(Float)
    filename = Column(String)
    snippet = Column(String)
    created = Column(DateTime, default=datetime.datetime.utcnow)

class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(Integer, primary_key=True)
    invoice_id = Column(String)
    due_date = Column(String)
    sent = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

def save_invoice(f):
    s = Session()

    iid = f.get("invoice_id") or f"inv_{int(time.time())}"

    inv = Invoice(
        invoice_id=iid,
        vendor=f.get("vendor"),
        date=f.get("date_normalized"),
        total=float(f.get("total") or 0),
        filename=f.get("filename"),
        snippet=f.get("raw_snippet")
    )
    s.add(inv)
    s.commit()

    # create reminder
    due = datetime.date.today() + datetime.timedelta(days=30)
    r = Reminder(invoice_id=iid, due_date=due.isoformat())
    s.add(r)
    s.commit()
    s.close()

    return {"status":"saved","invoice_id":iid,"due_date":due.isoformat()}

def list_pending():
    s = Session()
    rows = s.query(Reminder).filter(Reminder.sent == False).all()
    s.close()
    return [{"id":r.id,"invoice":r.invoice_id,"due":r.due_date} for r in rows]

def set_reminder_sent(rid):
    s = Session()
    r = s.query(Reminder).filter(Reminder.id==rid).first()
    if not r:
        s.close()
        return False
    r.sent = True
    s.commit()
    s.close()
    return True

def summary_stats():
    s = Session()
    today = datetime.date.today().isoformat()

    overdue = s.query(Reminder).filter(Reminder.sent==False, Reminder.due_date < today).count()

    t7 = (datetime.date.today()+datetime.timedelta(days=7)).isoformat()
    soon = s.query(Reminder).filter(Reminder.sent==False, Reminder.due_date.between(today,t7)).count()

    s.close()
    return {"overdue": overdue, "due_soon": soon}

def auto_overdue_update():
    # here you can expand logic later
    pass
