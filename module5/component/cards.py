import streamlit as st
from services.gemini_service import (
    explain_topic,
    summarize_text,
    generate_notes,
    generate_flashcards,
    generate_study_plan,
)
from utils.helpers import read_txt

def render_dashboard(stats):
    cols = st.columns(4)
    cols[0].metric("Conversations", stats["conversations"])
    cols[1].metric("Questions", stats["questions"])
    cols[2].metric("Messages", stats["messages"])
    cols[3].metric("Avg. Quiz Score", f"{stats['average_score']}%")

def render_explainer():
    st.subheader("💡 AI Explainer")

    topic = st.text_input("Enter a topic")
    level = st.selectbox(
        "Difficulty",
        ["Beginner", "Intermediate", "Advanced"],
    )

    if st.button("Explain Topic 🚀"):
        if not topic.strip():
            st.warning("Please enter a topic.")
            return

        with st.spinner("Creating explanation..."):
            try:
                st.markdown(explain_topic(topic, level))
            except Exception as e:
                st.error(str(e))

def render_summarizer():
    st.subheader("📝 Text Summarizer")

    uploaded = st.file_uploader(
        "Upload TXT or PDF study material",
        type=["txt", "pdf"],
    )

    text = st.text_area(
        "Or paste your study material",
        height=250,
    )

    if st.button("Summarize 🚀"):
        if uploaded:
            if uploaded.name.lower().endswith(".txt"):
                text = read_txt(uploaded)
            else:
                st.warning(
                    "PDF upload is accepted by the interface. "
                    "For this beginner version, please paste the PDF text."
                )
                return

        if not text.strip():
            st.warning("Please provide study material.")
            return

        with st.spinner("Summarizing..."):
            try:
                st.markdown(summarize_text(text))
            except Exception as e:
                st.error(str(e))

def render_notes():
    st.subheader("📚 Note Generator")

    topic = st.text_input("Topic")
    subject = st.text_input("Subject")
    difficulty = st.selectbox(
        "Difficulty Level",
        ["Beginner", "Intermediate", "Advanced"],
        key="notes_difficulty",
    )

    if st.button("Generate Notes 🚀"):
        if not topic.strip() or not subject.strip():
            st.warning("Please enter both subject and topic.")
            return

        with st.spinner("Generating notes..."):
            try:
                st.markdown(
                    generate_notes(topic, subject, difficulty)
                )
            except Exception as e:
                st.error(str(e))

def render_flashcards():
    st.subheader("🗂️ Flashcard Generator")

    topic = st.text_input("Flashcard Topic")
    count = st.number_input(
        "Number of cards",
        min_value=1,
        max_value=20,
        value=5,
    )

    if st.button("Generate Flashcards 🚀"):
        if not topic.strip():
            st.warning("Please enter a topic.")
            return

        with st.spinner("Generating flashcards..."):
            try:
                st.markdown(
                    generate_flashcards(topic, count)
                )
            except Exception as e:
                st.error(str(e))

def render_study_plan():
    st.subheader("📅 Study Plan Generator")

    subject = st.text_input("Subject")
    exam_date = st.date_input("Exam Date")
    hours = st.number_input(
        "Available hours per day",
        min_value=0.5,
        max_value=16.0,
        value=2.0,
        step=0.5,
    )
    topics = st.text_area("Topics to study")

    if st.button("Generate Study Plan 🚀"):
        if not subject.strip() or not topics.strip():
            st.warning("Please enter subject and topics.")
            return

        with st.spinner("Creating your study plan..."):
            try:
                st.markdown(
                    generate_study_plan(
                        subject,
                        str(exam_date),
                        hours,
                        topics,
                    )
                )
            except Exception as e:
                st.error(str(e))
