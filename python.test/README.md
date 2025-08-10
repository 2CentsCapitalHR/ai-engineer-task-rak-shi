"""
# ADGM Corporate Agent

An AI-powered legal document validator that checks business incorporation compliance for ADGM.

## Features
- Upload `.docx` documents
- Identify legal document types
- Verify against ADGM checklist
- Detect red flags (e.g., wrong jurisdiction, missing signatory)
- Download marked-up review and summary

## Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Output Example
- `results.json`: Summary of issues, missing documents

## TODO
- Add full RAG integration using ADGM PDFs
- Enhance classification with embedding-based method
"""
