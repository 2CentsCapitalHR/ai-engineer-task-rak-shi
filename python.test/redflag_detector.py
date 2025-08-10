def detect_red_flags(text, doc_type):
    issues = []
    text_lower = text.lower()

    # --- Jurisdiction check ---
    if "uae federal court" in text_lower:
        issues.append({
            "document": doc_type,
            "section": "Unknown",
            "issue": "Incorrect jurisdiction reference",
            "severity": "High",
            "suggestion": "Change to ADGM Courts as per ADGM Companies Regulations 2020"
        })

    # --- Signature check ---
    signature_keywords = [
        "signatory",
        "signed by",
        "authorized signature",
        "approved by"
    ]
    if not any(keyword in text_lower for keyword in signature_keywords):
        issues.append({
            "document": doc_type,
            "section": "Unknown",
            "issue": "Missing signatory section",
            "severity": "Medium",
            "suggestion": "Add signatory block with name, designation, and date"
        })

    return issues
