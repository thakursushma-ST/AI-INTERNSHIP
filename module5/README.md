# 🤖 AI Study Assistant

A professional beginner-friendly AI study assistant built with Python, Streamlit, and Google Gemini.

## Features

- 💬 AI Study Chat
- 💡 AI Explainer
- 📝 Text Summarizer
- 📚 Note Generator
- 🧠 MCQ Quiz Generator
- 🗂️ Flashcard Generator
- 📅 Study Plan Generator
- 💾 Local conversation history
- 📊 Dashboard metrics
- 🔐 Environment-based API key configuration
- 🌙 Modern dashboard-style UI

## Tech Stack

- Python 3.10+
- Streamlit
- Google Gemini API
- python-dotenv
- JSON local storage

## Project Structure

```text
ai-study-assistant/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── config/
│   └── settings.py
├── services/
│   ├── gemini_service.py
│   └── storage_service.py
├── utils/
│   ├── prompts.py
│   ├── helpers.py
│   └── validators.py
├── components/
│   ├── sidebar.py
│   ├── chat.py
│   ├── cards.py
│   └── quiz.py
└── data/
    └── conversations.json
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Gemini API Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-1.5-flash
```

Never upload `.env` to GitHub.

## Run

```bash
streamlit run app.py
```

Then open the local Streamlit URL in your browser.

## Security

API keys are loaded from environment variables. The `.gitignore` file prevents `.env` from being committed.

## Future Improvements

- Full PDF text extraction
- Interactive flashcard flipping
- Quiz scoring with answer controls
- User authentication
- Cloud database
- Voice input/output
- Streamlit Cloud deployment

## Internship Module

**Module 5 — AI Tools & Mini Project**

This project demonstrates how AI can assist with coding, learning, research, productivity, and educational workflows.
