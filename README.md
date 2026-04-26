# AI Skill Assessment Agent

##  Live Demo

👉 https://ai-skill-agent-4lsk5vug66zmntrfgz4fry.streamlit.app/

---

## Overview

This project is a web-based tool that compares a Job Description (JD) with a candidate’s resume to evaluate job readiness.

It identifies skill gaps, measures how well the candidate matches the role, and provides a structured learning plan along with practical recommendations for improvement.

---

## Key Features

* Extracts skills from both Job Description and Resume
* Identifies matched and missing skills
* Calculates a candidate score based on skill alignment
* Generates a structured learning plan tailored to missing skills
* Provides recommendations based on the type of skills (technical, tools, soft skills)
* Works across multiple domains such as data roles, business roles, and HR

---

## How It Works

1. The user inputs a Job Description and a Resume
2. The system extracts relevant skills using text parsing
3. It compares both sets of skills to identify gaps
4. Based on the analysis, it generates:

   * Skill gap breakdown
   * Candidate score
   * Learning roadmap
   * Recommendations

---

## Scoring Logic

The candidate score is calculated using:

Score = (Matched Skills / Total Required Skills) × 100

Based on the score:

* Above 75% → Strong Candidate
* 50% – 75% → Moderate Candidate
* Below 50% → Needs Improvement

---

## Learning Plan Logic

The learning plan is generated based on missing skills and adapts depending on the skill type:

* Technical skills → concept learning, coding practice, and projects
* Tools → dashboard creation and practical use cases
* Soft skills → communication practice, mock interviews, and real-world application

---

## System Design (Architecture)

User Input (JD + Resume)
→ Skill Extraction
→ Skill Gap Analysis
→ Scoring Module
→ Learning Plan Generation
→ Recommendation Engine
→ Streamlit Interface

---

## Example

**Input:**
       JD: Python, SQL, Communication

Resume: Python, Excel


**Output:**
         Matched Skills: Python

Missing Skills: SQL, Communication

Score: ~33%

Learning Plan: Structured roadmap for improvement

---

## Notes

* This project uses a rule-based approach for reliability and clarity
* It supports free-text job descriptions instead of fixed formats
* It can be extended with AI/LLM models for deeper semantic understanding

---

## Author

Annesha Khamrui

Master’s in Operational Research

University of Delhi
