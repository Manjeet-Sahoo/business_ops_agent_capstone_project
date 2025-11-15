from PIL import Image
import pytesseract, io
from pdf2image import convert_from_bytes

def ocr_bytes_to_text(b: bytes, filename=""):
    name = filename.lower()

    try:
        if name.endswith(".pdf") or b[:4] == b"%PDF":
            pages = convert_from_bytes(b, dpi=200)
            texts = [pytesseract.image_to_string(pg.convert("L")) for pg in pages]
            return "\n".join(texts)

        img = Image.open(io.BytesIO(b)).convert("L")
        return pytesseract.image_to_string(img)

    except:
        return ""
