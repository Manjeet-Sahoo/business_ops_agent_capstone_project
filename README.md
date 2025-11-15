#Business Operations AI Agent Suite

An intelligent multi agent workflow that reads invoices, extracts key fields, stores structured records, generates reminders, and produces real-time business insights with zero manual work.

Designed specifically for the Enterprise Agents Track of the Google × Kaggle AI Agents Capstone.

This repository demonstrates how AI agents can automate real business operations at a production-ready level.


#Why This Project Matters

Modern businesses run on documents.
Invoices, bills, receipts, payment reminders.
Yet most companies still process them manually.

That leads to
• wasted hours
• lost invoices
• late fees
• inconsistent records
• no overview of financial health

This project replaces that entire manual workflow with an autonomous agent system that behaves like a trained operations team.

Upload an invoice and the agents take over.
The accuracy, speed, and traceability are significantly better than traditional workflows.


#Key Capabilities

This system is built to demonstrate real enterprise value.

• Fully automated invoice extraction (PDF or image)
• OCR powered text understanding
• LLM assisted field extraction (invoice id, vendor, date, amount)
• Long-term invoice storage
• Auto-generated reminders with due dates
• Daily agent loop that updates overdue status
• Weekly insight engine for business financial health
• Full observability layer for logs and metrics
• MCP styled custom tools for agent interoperability
• Containerized deployment with Docker

Every component mirrors real business use cases and directly applies course concepts.


#Enterprise-Grade Agent Architecture

Below is the high-level system design (matches the image you will upload on Kaggle)

Flow Overview
• User uploads an invoice
• Document Agent runs OCR
• Extraction Agent identifies structured fields
• Memory Agent saves the record
• Workflow Agent creates reminders
• Loop Agent checks overdue items daily
• Insight Agent produces actionable summaries
• Observability tools monitor activity

#Agent Roles
• Document Agent → Vision and OCR
• Extraction Agent → Structured field parsing
• Workflow Agent → Business operations logic
• Insight Agent → Analytics and forecasting
• Notification Agent → Action triggers
• Loop Agent → Automation and scheduling
• Evaluation Agent → Quality feedback

This structure shows a complete enterprise multi agent system, not a single-model solution.


<img width="1536" height="1024" alt="ai agent capstone project" src="https://github.com/user-attachments/assets/241afbd2-34f6-453c-9b32-c93815efeddc" />



#Folder Structure
business_ops_agent/
│
├── main.py               
├── requirements.txt      
├── Dockerfile            
├── docker-compose.yml    

├── agents/               
   ├── document_agent.py
   ├── extraction_agent.py
   ├── workflow_agent.py
   ├── insight_agent.py
   ├── notification_agent.py
   ├── loop_agent.py
   ├── evaluation_agent.py
   └── mcp_tools.json

├── memory/
   └── invoice_db.py

├── utils/
   ├── ocr.py
   ├── observability.py
   └── tracing.py

 └── samples/

The structure remains clean, modular, and extendable.


#Installation and Setup
• Step 1

Install Python 3.10 or newer.

• Step 2

Install project dependencies:

pip install -r requirements.txt

• Step 3

Start the API server:

uvicorn main:app --reload --port 8000


Open the interactive API:

http://localhost:8000/docs


#How to Use
1. Upload an invoice

Endpoint
POST /upload-invoice

Select a PDF or image of an invoice.
The system extracts fields and stores records automatically.

2. View reminders

GET /reminders
Shows all invoices that require action.

3. Mark reminder as sent

POST /send/{id}
Closes a pending reminder.

4. Generate insights

GET /insights
Summaries include
• overdue invoices
• invoices due soon
• upcoming cashflow concerns


Daily Loop Automation

A background agent runs every 24 hours to
• detect overdue invoices
• update reminder states
• keep the system always current

This simulates real scheduling inside enterprise workflows.


#Observability and Metrics

The metrics server runs on port 8001.
It exposes system level data suitable for dashboards and monitoring tools like Prometheus or Grafana.

Logs include
• request id tracing
• time stamps
• extraction status
• reminder operations

This matches real industry observability standards.


Docker Deployment

Enterprise environments use containers.
This project is fully container-ready.

Build:

docker build -t business_ops .


Run:

docker run -p 8000:8000 business_ops


Then open the API at
http://localhost:8000/docs


