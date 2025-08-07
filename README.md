# 🤖 GenAI Use Case App – LangChain + Groq +  Streamlit

A Streamlit web app that showcases **3 real-world GenAI applications** across support, PMO and HR. Built using **LangChain**, powered by **LLMs from Groq**, this app helps you test, demo, and present generative AI use cases in an interactive UI.

---

## 🚀 Live Use Cases Included

| Use Case                             | Description |
|-------------------------------------|-------------|
| 1️⃣ Customer Support Classifier      | Classifies support tickets into categories like login issue, payment problem, etc. |
| 2️⃣ Meeting Action Item Extractor    | Extracts task, owner, and deadline from meeting transcripts |
| 3️⃣ Resume Evaluator for Job Fit     | Compares resumes against job descriptions and outputs fit score |

---

## 🧰 Tech Stack

- LangChain
- Groq LLMs
- Prompt Engineering
- Python
- Streamlit

---

## 📽️ Demo Video

👉 [Watch the demo video](https://drive.google.com/file/d/1Qk31c8t6Mq5RH4aD3vbLnyWevQB7GIWg/view?usp=drive_link)  

---

## 📁 Folder Structure

```bash
.
├── genai_usecases_streamlit_app.py     # Main Streamlit app
├── .env                                # Store your GROQ_API_KEY here
├── requirements.txt                    # Python dependencies
└── README.md
```
## 🚀 Setup & Run the App

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/AkhilCh308/genAI-usecases-app.git
cd genai-usecases-app
```
### ✅ Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ Step 3: Add your Groq API key

### Create a .env file:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
### Or export via terminal:
```bash
export GROQ_API_KEY=your_groq_api_key_here  # for Mac/Linux
set GROQ_API_KEY=your_groq_api_key_here     # for Windows
```

### ✅ Step 4: Run the app

```bash
streamlit run genai_usecases_streamlit_app.py
```
