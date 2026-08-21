import json
import os
import uuid
from datetime import datetime
from config.settings import DATA_FILE

def _ensure_file():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)

def load_conversations():
    _ensure_file()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

def save_conversations(conversations):
    _ensure_file()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(conversations, f, indent=2, ensure_ascii=False)

def create_conversation(title="New Chat"):
    conversations = load_conversations()
    conversation = {
        "id": str(uuid.uuid4()),
        "title": title,
        "date": datetime.now().isoformat(timespec="seconds"),
        "messages": [],
    }
    conversations.insert(0, conversation)
    save_conversations(conversations)
    return conversation

def add_message(conversation_id, role, content):
    conversations = load_conversations()
    for conversation in conversations:
        if conversation["id"] == conversation_id:
            conversation["messages"].append({
                "role": role,
                "content": content,
            })
            if role == "user" and conversation["title"] == "New Chat":
                conversation["title"] = content[:40]
            break
    save_conversations(conversations)

def delete_conversation(conversation_id):
    conversations = [
        c for c in load_conversations()
        if c["id"] != conversation_id
    ]
    save_conversations(conversations)

def clear_all_conversations():
    save_conversations([])

def get_stats():
    conversations = load_conversations()
    total_messages = sum(len(c["messages"]) for c in conversations)
    questions = sum(
        1 for c in conversations
        for m in c["messages"]
        if m["role"] == "user"
    )
    return {
        "conversations": len(conversations),
        "questions": questions,
        "messages": total_messages,
        "quizzes": 0,
        "average_score": 0,
    }
