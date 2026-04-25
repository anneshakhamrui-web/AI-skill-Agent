import re

def extract_skills(text):
    text = text.lower()

    skill_keywords = [
        # Tech
        "python", "sql", "java", "c++", "machine learning", "deep learning",
        "nlp", "pandas", "numpy", "matplotlib", "scikit-learn",
        
        # Data / Analytics
        "excel", "power bi", "tableau", "data analysis", "statistics",
        
        # Business / Finance
        "marketing", "finance", "sales", "accounting", "business analysis",
        
        # HR / Management
        "recruitment", "training", "employee engagement", "leadership",
        "team management", "communication", "presentation",
        
        # General
        "problem solving", "critical thinking", "time management"
    ]

    found = []

    for skill in skill_keywords:
        if skill in text:
            found.append(skill)

    return list(set(found))


def skill_gap(jd, resume):
    matched = []
    missing = []

    resume_text = " ".join(resume)

    for skill in jd:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    return {
        "matched_skills": list(set(matched)),
        "missing_skills": list(set(missing))
    }

def classify_skill(skill):
    s = skill.lower()

    if any(k in s for k in ["python", "sql", "machine", "coding", "programming"]):
        return "technical"

    elif any(k in s for k in ["excel", "power bi", "tableau"]):
        return "tool"

    elif any(k in s for k in ["communication", "leadership", "management"]):
        return "soft"

    else:
        return "general"
def generate_questions(gap):
    questions = []

    for skill in gap["missing_skills"]:
        questions.append(f"How would you apply {skill} to solve a real-world problem?")
        questions.append(f"Explain a scenario where {skill} can improve decision making.")
        questions.append(f"What challenges might you face while using {skill}, and how would you overcome them?")

    return questions[:5]  # limit to 5 questions


def score_candidate(gap):
    matched = len(gap["matched_skills"])
    total = matched + len(gap["missing_skills"])

    if total == 0:
        return "0"

    score = (matched / total) * 100

    if score > 75:
        level = "Strong Candidate"
    elif score > 50:
        level = "Moderate Candidate"
    else:
        level = "Needs Improvement"

    return f"{score:.2f}/100 — {level}"


def learning_plan(gap):
    plan = ""

    for skill in gap["missing_skills"]:
        category = classify_skill(skill)

        plan += f"\n\n🔹 Skill: {skill.title()}\n"

        if category == "technical":
            plan += "\nWeek 1: Learn fundamentals (YouTube / docs)\n"
            plan += "\nWeek 2: Practice problems (LeetCode / HackerRank)\n"
            plan += "\nWeek 3: Work on real data (Kaggle)\n"
            plan += "\nWeek 4: Build project\n"

        elif category == "tool":
            plan += "\nWeek 1: Learn tool basics\n"
            plan += "\nWeek 2: Practice dashboards/reports\n"
            plan += "\nWeek 3: Case study analysis\n"
            plan += "\nWeek 4: Portfolio project\n"

        elif category == "soft":
            plan += "\nWeek 1: Learn fundamentals\n"
            plan += "\nWeek 2: Daily practice (speaking/presentation)\n"
            plan += "\nWeek 3: Mock interviews\n"
            plan += "\nWeek 4: Feedback & improvement\n"

        else:
            plan += "\nWeek 1: Learn basics\n"
            plan += "\nWeek 2: Practice\n"
            plan += "\nWeek 3: Apply in real scenarios\n"
            plan += "\nWeek 4: Build project\n"

        plan += "\n---------------------------\n"

    return plan