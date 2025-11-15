#Problem

Small businesses spend many hours handling invoices. Someone has to open PDFs, read amounts, note dates, check which payment is overdue, calculate what is due soon, and follow up.
This work is slow, boring, and often leads to mistakes.
If one reminder is missed, the business pays late fees.
If one invoice is entered incorrectly, the business loses money.

Many business owners told us they do not have a proper system. They usually save invoices in folders and update payment sheets manually.
This breaks easily when work grows.



#Goal

Create an AI system that handles the entire invoice process without human effort.



#Solution

I built a multi agent AI workflow that reads invoices, extracts details, stores them, creates reminders, checks for overdue bills, gives weekly insights, and logs everything.
The agents work together like a small digital team.



#System agents

• Document Agent: reads PDF or image and turns it into text
• Extraction Agent: pulls fields like invoice number, vendor, date, total amount
• Memory Agent: stores the invoice in long term storage
• Workflow Agent: creates reminders and tracks which ones are sent
• Insight Agent: checks the database and creates business summaries
• Loop Agent: runs daily in the background and updates overdue status
• Observability system: logs, metrics, and request tracing
• Evaluation Agent: tracks quality of extraction (simple rule based check)



#Why agents

Agents split work into small parts.
One agent can fail without breaking the entire system.
The flow becomes easier to test.
Each agent can have its own tool set.
This makes the final system stable and expandable.



#Key course concepts used

• Multi agent system
• MCP style tools
• Long term memory with SQLite
• Session notes and state
• Observability using metrics and logs
• Loop agent that runs daily
• Agent evaluation prompts
• Optional deployment ready with Docker

This covers more than the required three concepts.


#Architecture

When an invoice is uploaded, the Document Agent turns it into text by using OCR.
That text moves to the Extraction Agent which pulls key fields.
The Memory Agent stores the extracted values inside SQLite.
A new reminder is created automatically.
The Workflow Agent lists all pending reminders and marks them when sent.
The Loop Agent runs every day and checks for overdue items.
The Insight Agent scans the stored invoices and gives a summary like
• number of overdue invoices
• number of invoices due soon
• overall status of invoice health

The Observability tools record every request and open a metrics server that can be used by Prometheus.

<img width="1536" height="1024" alt="ai agent capstone project" src="https://github.com/user-attachments/assets/72085ae8-2ec0-4fb0-9c5e-de8a8a1cbdbb" />


#Value

This system gives businesses
• faster invoice management
• clean data storage
• reduced manual errors
• early warning for overdue payments
• a clear weekly health report

A small company can save many hours every month by using this.
A larger company can scale it without extra hiring.


#What I learn

During the AI course I learned how agents work, how to attach tools, how looping can be done, and how memory can be connected.
I applied everything into one clean system that solves a real problem.
I tested the system with sample invoices and verified that extraction and reminders work.
The code is simple for others to understand and extend.

#Next steps

• add email sending for real reminders
• add vendor matching using embeddings
• deploy to Cloud Run for public use
• add a dashboard for insights

#This project shows how agent systems can remove repetitive office work and save real time.
