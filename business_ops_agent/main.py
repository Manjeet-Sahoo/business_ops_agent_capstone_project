import uuid, logging
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from agents.document_agent import process_document
from agents.workflow_agent import get_reminders, mark_sent
from agents.insight_agent import get_insights
from agents.loop_agent import start_daily_loop
from utils.observability import setup_metrics

app = FastAPI(title="Business Ops Agent Suite")

logging.basicConfig(level=logging.INFO)

setup_metrics()  # metrics on port 8001
start_daily_loop()  # background loop agent

@app.middleware("http")
async def add_req_id(request, call_next):
    req_id = str(uuid.uuid4())
    request.state.request_id = req_id
    logging.info(f"[{req_id}] {request.method} {request.url}")
    resp = await call_next(request)
    resp.headers["X-Request-ID"] = req_id
    return resp

@app.post("/upload-invoice")
async def upload_invoice(file: UploadFile = File(...)):
    contents = await file.read()
    result = process_document(contents, file.filename)
    return JSONResponse(result)

@app.get("/reminders")
def reminders():
    return JSONResponse(get_reminders())

@app.post("/send/{rid}")
def send(rid: int):
    return JSONResponse({"sent": mark_sent(rid)})

@app.get("/insights")
def insights():
    return JSONResponse(get_insights())
