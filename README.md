# ADGM Corporate Agent - Document Validator

A Streamlit-based application for validating `.docx` legal documents as per ADGM (Abu Dhabi Global Market) requirements.  
The app checks for the presence of all required documents, detects missing ones, and flags any issues found.

---

## 📌 Features

- **Drag & Drop File Upload**: Upload `.docx` files directly via the UI.
- **Checklist Verification**: Automatically verifies uploaded documents against a required checklist.
- **Red Flag Detection**: Identifies missing sections, incorrect references, and compliance issues.
- **Structured JSON Output**: Displays validation results in a clean JSON format.

---

## 📂 Required Documents

The application expects the following documents:
1. **Resolution**
2. **MoA** – Memorandum of Association
3. **AoA** – Articles of Association
4. **Register** – Members/Directors Register
5. **UBO Form** – Ultimate Beneficial Ownership Declaration

---

## 🖥️ How It Works

1. **Start the Streamlit App**
   ```bash
   streamlit run app.py
