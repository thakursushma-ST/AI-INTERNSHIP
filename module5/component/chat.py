import streamlit as st
from services.gemini_service import generate_response
from services.storage_service import (
    load_conversations,
    create_conversation,
    add_message,
)

def _get_current_conversation():
    conversations = load_conversations()
    for conversation in conversations:
        if conversation["id"] == st.session_state.conversation_id:
            return conversation
    return None

def render_chat():
    conversation = _get_current_conversation()

    if conversation is None:
        conversation = create_conversation("New Chat")
        st.session_state.conversation_id = conversation["id"]

    st.subheader("💬 Ask AI")

    for message in conversation["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask anything about your studies...")

    if question:
        add_message(conversation["id"], "user", question)

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    prompt = f"""
You are an AI Study Assistant and patient academic tutor.

Student question:
{question}

Answer clearly and accurately.
Use simple explanations first, then details when useful.
Use Markdown formatting and examples when appropriate.
"""
                    answer = generate_response(prompt)
                    st.markdown(answer)
                    add_message(conversation["id"], "assistant", answer)
                except Exception as e:
                    st.error(str(e))
