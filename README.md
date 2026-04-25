# AI Skill Assessment Agent

## About the Project

This project is a simple web-based tool that compares a Job Description (JD) with a candidate’s resume. It helps in identifying skill gaps and gives suggestions on how to improve.

The main idea is that resumes often show what someone claims to know, but not how well they match a specific job. This tool tries to bridge that gap.

---

## What It Does

* Extracts skills from both Job Description and Resume
* Compares them to find matching and missing skills
* Gives a score based on how well the candidate fits
* Generates a learning plan to improve missing skills
* Suggests what to focus on next

---

## Features

* Works for different roles (Data, HR, Business, etc.)
* Skill-based comparison system
* Simple scoring method
* Personalized learning roadmap
* Basic recommendations for improvement

---

## How It Works

1. User pastes Job Description and Resume
2. The system extracts skills from both
3. It compares them and finds gaps
4. Based on gaps, it generates:

   * Score
   * Learning plan
   * Suggestions

---

## Tech Used

* Python
* Streamlit

---

## How to Run

1. Install Python

2. Install Streamlit:
   pip install streamlit

3. Run the app:
   streamlit run app.py

4. Open in browser:
   http://localhost:8501

---

## Example

Input:
JD: Python, SQL, Excel
Resume: Python, Excel

Output:
Matched: Python, Excel
Missing: SQL
Score: ~66%

---

## Notes

* This is a rule-based system (not using external AI APIs)
* Can be extended with LLMs in future
* Designed to be simple, understandable, and easy to improve

---

## Author

Annesha Khamrui
Master’s in Operational Research
University of Delhi
