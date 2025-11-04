# Estate Document Summarizer

A simple Streamlit web app that uses **OpenAI GPT** to summarize estate or legal PDF documents.  
It automatically generates a short, professional summary and extracts key details (grantor, trustee, beneficiaries, etc.) into structured JSON.

---

## Features
- Upload a PDF file  
- AI-powered document summarization  
- Extracts key fields like names, dates, and jurisdictions  
- Clean and minimal Streamlit interface  

---

## How It Works
1. The PDF text is read using **PyPDF2**  
2. The text is processed through **OpenAI GPT-4o-mini**  
3. The model returns:
   - A concise summary  
   - Extracted information in valid JSON  

All summaries are generated dynamically and displayed in the app.

---

## Tech Stack
- Python 3.10+  
- Streamlit  
- OpenAI GPT-4o-mini  
- PyPDF2  
- dotenv  

---

## Run Locally
```bash
pip install -r requirements.txt
streamlit run src/app.py
```
On Streamlit Cloud, the API key is securely stored in app secrets, no local .env file needed.
