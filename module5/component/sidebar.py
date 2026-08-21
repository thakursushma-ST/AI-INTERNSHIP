import streamlit as st
from services.storage_service import (
    load_conversations,
    create_conversation,
    delete_conversation,
    clear_all_conversations,
)

def render_sidebar():
    with st.sidebar:
        st.markdown("## 🤖 AI Study Assistant")
        st.caption("Learn smarter. Understand faster.")

        if st.button("➕ New Chat", use_container_width=True):
            conversation = create_conversation()
            st.session_state.conversation_id = conversation["id"]
            st.session_state.tool = "Ask AI"
            st.rerun()

        st.divider()

        st.markdown("### Study Tools")

        tools = [
            "Ask AI",
            "AI Explainer",
            "Summarize",
            "Generate Notes",
            "Create Quiz",
            "Flashcards",
            "Study Plan",
        ]

        selected = st.radio(
            "Choose a tool",
            tools,
            index=tools.index(st.session_state.get("tool", "Ask AI")),
            label_visibility="collapsed",
        )

        st.session_state.tool = selected

        st.divider()

        st.markdown("### Chat History")

        conversations = load_conversations()

        for conversation in conversations[:10]:
            if st.button(
                conversation["title"][:30],
                key=f"open_{conversation['id']}",
                use_container_width=True,
            ):
                st.session_state.conversation_id = conversation["id"]
                st.session_state.tool = "Ask AI"
                st.rerun()

        st.divider()

        if st.button("🗑️ Clear History", use_container_width=True):
            clear_all_conversations()
            st.session_state.conversation_id = None
            st.success("History cleared.")
            st.rerun()

        st.markdown("### About")
        st.caption(
            "A portfolio-ready AI learning assistant built with "
            "Python, Streamlit, and Google Gemini."
        )

    return selected
