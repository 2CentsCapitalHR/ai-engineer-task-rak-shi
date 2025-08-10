REQUIRED_DOCS = ["AoA", "MoA", "Resolution", "UBO Form", "Register"]

def verify_documents(docs):
    uploaded = [v["type"] for v in docs.values()]
    missing = list(set(REQUIRED_DOCS) - set(uploaded))
    summary = f"Uploaded: {len(uploaded)} / {len(REQUIRED_DOCS)} required documents. Missing: {missing}"
    return summary, missing[0] if missing else None