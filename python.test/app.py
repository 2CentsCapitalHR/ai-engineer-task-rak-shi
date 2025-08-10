import streamlit as st
from doc_parser import parse_docx, identify_document_type
from checklist_verifier import verify_documents
from redflag_detector import detect_red_flags
from rag_engine import get_rag_response
import json

st.title("ADGM Corporate Agent - Document Validator")

uploaded_files = st.file_uploader(
    "Upload your .docx legal documents",
    type=["docx"],
    accept_multiple_files=True
)

if uploaded_files:
    parsed_docs = {}
    for idx, file in enumerate(uploaded_files):
        text = parse_docx(file)
        doc_type = identify_document_type(text)
        parsed_docs[f"{file.name}_{idx}"] = {"text": text, "type": doc_type}

    # Checklist verification
    summary, missing_doc = verify_documents(parsed_docs)
    st.write("## Checklist Verification Result")
    st.write(summary)

    # Red flag detection — ensure all docs appear in output
    issues = []
    for name, data in parsed_docs.items():
        red_flags = detect_red_flags(data["text"], data["type"])
        if red_flags:
            issues.extend(red_flags)
        else:
            issues.append({
                "document": data["type"],
                "section": "N/A",
                "issue": "No issues detected",
                "severity": "Info",
                "suggestion": "Document meets basic checks"
            })

    st.write("## Detected Red Flags / Findings")
    st.json(issues)

    # Create report
    report = {
        "process": "Company Incorporation",
        "documents_uploaded": len(parsed_docs),
        "required_documents": 5,
        "missing_document": missing_doc,
        "issues_found": issues
    }

    # Save JSON output
    with open("outputs/results.json", "w") as f:
        json.dump(report, f, indent=2)

    # Download button with unique key
    st.download_button(
        "Download Report (JSON)",
        data=json.dumps(report, indent=2),
        file_name="results.json",
        key=f"download_report_{len(parsed_docs)}"
    )
