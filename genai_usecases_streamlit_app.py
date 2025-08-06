
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="GenAI Use Cases Showcase", layout="centered")

# Initialize LLM
llm = ChatGroq(model_name="llama-3.3-70b-versatile")

# Sidebar
use_case = st.sidebar.selectbox("Select a Use Case", [
    "Customer Support Ticket Classifier",
    "Meeting Action Item Extractor",
    "Resume Evaluator"
])

st.title(f"🧠 {use_case}")

# Define UI and logic per use-case
if use_case == "Customer Support Ticket Classifier":
    ticket = st.text_area("Enter Support Ticket Description")
    if st.button("Classify"):
        prompt = PromptTemplate.from_template("""
        Classify the issue into one of these categories:
        Login Issue, Payment Problem, Order Delay, Feedback, Bug Report

        Ticket: "Am unable to login to the server"
        Category: "Login Issue"

        Ticket: "my amount was debited, but shows status transaction failed"
        Category: "Payment Issue"

        Ticket: "I see status in transit, but still i didnt get my product deivered"
        Category: "Order Delay"

        Ticket: "It's an amazing product, I love to use it"
        Category: "Feedback"

        Ticket: "when i select checkout, my cart is getting empty instead of proceeding to payment"
        Category: "Bug Report"


        Ticket: "{ticket}"
        Category:
        """)
        chain = prompt | llm
        result = chain.invoke({"ticket": ticket})
        st.success(f"Predicted Category: {result.content.strip()}")

elif use_case == "Meeting Action Item Extractor":
    transcript = st.text_area("Paste Meeting Transcript")
    if st.button("Extract Action Items"):
        prompt = PromptTemplate.from_template("""
        Extract action items as JSON containing the following keys: task, owner, deadline.

        Only return the valid JSON. No preamble.


        Transcript: "{transcript}"
        Output:
        """)
        chain = prompt | llm
        result = chain.invoke({"transcript": transcript})
        st.json(result.content)

elif use_case == "Resume Evaluator":
    jd = st.text_area("Paste Job Description")
    resume = st.text_area("Paste Resume")
    if st.button("Evaluate"):
        prompt = PromptTemplate.from_template("""
        Compare the resume to job description. Output:
        - Fit Score (0-100)
        - Matched Skills
        - Missing Skills
        - Recommendation

        Job Description:
        {jd}

        Resume:
        {resume}

        Output:
        """)
        chain = prompt | llm
        result = chain.invoke({"jd": jd, "resume": resume})
        st.markdown(result.content)

