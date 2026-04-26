import streamlit as st
from utils import *

st.title("🤖 AI Skill Assessment Agent")

jd = st.text_area("📄 Paste Job Description")
resume = st.text_area("📑 Paste Resume")

if st.button("Analyze Candidate"):
    if jd and resume:
        st.success("Processing...")

        jd_skills = extract_skills(jd)
        resume_skills = extract_skills(resume)

        gap = skill_gap(jd_skills, resume_skills)
        questions = generate_questions(gap)
        score = score_candidate(gap)
        plan = learning_plan(gap)

        st.subheader("📊 Skill Gap Analysis")

        st.markdown("### ✅ Matched Skills")
        st.write(", ".join(gap["matched_skills"]))

        st.markdown("### ❌ Missing Skills")
        st.write(", ".join(gap["missing_skills"]))


        st.subheader("🧠 Assessment Questions")
        for q in questions:
            st.markdown(f"- {q}")


        st.subheader("📈 Candidate Score")
        st.success(score)


        st.subheader("🗺️ Personalized Learning Plan")
        st.success("Personalized roadmap generated based on your skill gaps ✅")
        st.write(plan)
        
        st.subheader("💡 Smart Recommendations")

        for skill in gap["missing_skills"]:
            s = skill.lower()

            # 🔵 Technical skills
            if any(word in s for word in ["python", "sql", "machine", "learning", "data", "analysis", "coding", "programming", "ai", "ml"]):
                st.info(f"📌 {skill.title()}: Focus on strong fundamentals and hands-on practice. Work on real datasets and build projects to gain practical experience.")

            # 🟢 Tools / Software
            elif any(word in s for word in ["excel", "power bi", "tableau", "dashboard", "tools"]):
                st.info(f"📌 {skill.title()}: Practice by creating dashboards and analyzing real-world data. Build portfolio projects to showcase your skills.")

            # 🟡 Soft skills
            elif any(word in s for word in ["communication", "presentation", "team", "leadership", "management"]):
                st.info(f"📌 {skill.title()}: Improve through daily practice, mock interviews, and real-world interaction. Focus on clarity and confidence.")

            # ⚪ General / Unknown skills
            else:
                st.info(f"📌 {skill.title()}: Start with basics, explore real-world applications, and gradually move to advanced concepts with hands-on practice.")
