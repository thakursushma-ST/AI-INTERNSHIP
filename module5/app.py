import streamlit as st
from config.settings import APP_NAME, APP_VERSION
from components.sidebar import render_sidebar
from components.cards import render_dashboard
from components.chat import render_chat
from components.quiz import render_quiz_tool
from services.storage_service import get_stats, clear_all_conversations

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020 0%, #111827 55%, #0b1020 100%);
}
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}
h1 {
    background: linear-gradient(90deg, #a78bfa, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)

if "tool" not in st.session_state:
    st.session_state.tool = "Ask AI"

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

tool = render_sidebar()

st.title("AI Study Assistant")
st.caption("Learn smarter. Understand faster. 🚀")

stats = get_stats()

render_dashboard(stats)

st.divider()

if tool == "Ask AI":
    render_chat()

elif tool == "Create Quiz":
    render_quiz_tool()

elif tool == "AI Explainer":
    from components.cards import render_explainer
    render_explainer()

elif tool == "Summarize":
    from components.cards import render_summarizer
    render_summarizer()

elif tool == "Generate Notes":
    from components.cards import render_notes
    render_notes()

elif tool == "Flashcards":
    from components.cards import render_flashcards
    render_flashcards()

elif tool == "Study Plan":
    from components.cards import render_study_plan
    render_study_plan()

st.divider()
st.caption(f"{APP_NAME} • {APP_VERSION} • Powered by Gemini")
