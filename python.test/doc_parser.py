from docx import Document

def parse_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def identify_document_type(text):
    t = text.lower()
    if "articles of association" in t:
        return "AoA"
    elif "memorandum of association" in t:
        return "MoA"
    elif "board resolution" in t or "shareholder resolution" in t or "resolution" in t:
        return "Resolution"
    elif "ubo" in t or "ultimate beneficial owner" in t:
        return "UBO Form"
    elif "register of members" in t or "register of directors" in t:
        return "Register"
    else:
        return "Unknown"
