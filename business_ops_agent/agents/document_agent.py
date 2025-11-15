from utils.ocr import ocr_bytes_to_text
from agents.extraction_agent import extract_invoice_fields
from memory.invoice_db import save_invoice

def process_document(contents: bytes, filename: str):
    text = ocr_bytes_to_text(contents, filename)
    fields = extract_invoice_fields(text)

    fields["filename"] = filename
    fields["raw_snippet"] = text[:1500]

    result = save_invoice(fields)
    return result
