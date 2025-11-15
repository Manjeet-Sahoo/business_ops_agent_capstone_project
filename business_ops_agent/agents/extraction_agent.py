import re
import dateparser

def normalize_date(s):
    if not s:
        return None
    dt = dateparser.parse(s)
    return dt.date().isoformat() if dt else None

def extract_invoice_fields(text: str):
    out = {}

    m = re.search(r"(invoice|inv)[\s#:]*([A-Z0-9\-]{3,40})", text, re.I)
    if m:
        out["invoice_id"] = m.group(2)

    m = re.search(r"(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})", text)
    if m:
        out["date"] = m.group(1)

    m = re.search(r"(total|amount due)[:\s]*₹?([0-9\.,]+)", text, re.I)
    if m:
        out["total"] = m.group(2).replace(",", "")

    m = re.search(r"(from|vendor|bill to)[:\s]*([A-Za-z0-9 \.,&\-]{3,80})", text, re.I)
    if m:
        out["vendor"] = m.group(2).strip()

    out["date_normalized"] = normalize_date(out.get("date"))
    return out
