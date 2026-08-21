import re
import streamlit as st
from services.gemini_service import generate_quiz

def render_quiz_tool():
    st.subheader("🧠 MCQ Quiz Generator")

    subject = st.text_input("Subject")
    topic = st.text_input("Topic")
    count = st.number_input(
        "Number of questions",
        min_value=1,
        max_value=10,
        value=5,
    )
    difficulty = st.selectbox(
        "Difficulty",
        ["Beginner", "Intermediate", "Advanced"],
        key="quiz_difficulty",
    )

    if st.button("Generate Quiz 🚀"):
        if not subject.strip() or not topic.strip():
            st.warning("Please enter subject and topic.")
            return

        with st.spinner("Generating quiz..."):
            try:
                raw = generate_quiz(
                    subject,
                    topic,
                    int(count),
                    difficulty,
                )
                st.session_state.quiz_text = raw
            except Exception as e:
                st.error(str(e))

    if "quiz_text" in st.session_state:
        st.markdown("### Generated Quiz")
        st.markdown(st.session_state.quiz_text)
        st.info(
            "For the internship demo, answers and explanations are "
            "included in the generated quiz so you can verify your score."
        )
