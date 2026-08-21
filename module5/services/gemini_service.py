from google import genai

from config.settings import GEMINI_API_KEY, GEMINI_MODEL


def get_client():
    if not GEMINI_API_KEY:
        raise RuntimeError(
            "Gemini API key is missing. "
            "Add GEMINI_API_KEY to your .env file."
        )

    return genai.Client(
        api_key=GEMINI_API_KEY
    )


def generate_response(prompt: str) -> str:

    client = get_client()

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    if not response.text:
        raise RuntimeError(
            "The AI service returned an empty response."
        )

    return response.text


def explain_topic(topic: str, level: str) -> str:

    return generate_response(
        f"""
You are a patient academic tutor.

Explain this topic for a {level.lower()} student.

Topic:
{topic}

Use:

- Simple explanation
- Key concepts
- One practical example
- Important points
- Short summary
"""
    )


def summarize_text(text: str) -> str:

    return generate_response(
        f"""
Summarize the following study material for a student.

Return:

1. Short summary
2. Important points
3. Key terms
4. Exam-focused notes

Study material:

{text}
"""
    )


def generate_notes(
    topic: str,
    subject: str,
    difficulty: str
) -> str:

    return generate_response(
        f"""
Create structured study notes.

Subject:
{subject}

Topic:
{topic}

Difficulty:
{difficulty}

Include:

- Definition
- Main concepts
- Detailed explanation
- Examples
- Important points
- Exam tips
"""
    )


def generate_quiz(
    subject: str,
    topic: str,
    count: int,
    difficulty: str
) -> str:

    return generate_response(
        f"""
Create exactly {count} multiple-choice questions.

Subject:
{subject}

Topic:
{topic}

Difficulty:
{difficulty}

For every question use this format:

Q1. Question
A. Option
B. Option
C. Option
D. Option
Answer: A
Explanation: Short explanation

Do not add questions outside the requested count.
"""
    )


def generate_flashcards(
    topic: str,
    count: int
) -> str:

    return generate_response(
        f"""
Create {count} study flashcards for:

{topic}

Use this exact format:

CARD 1
Front: term or question
Back: answer or definition

CARD 2
Front: term or question
Back: answer or definition
"""
    )


def generate_study_plan(
    subject: str,
    exam_date: str,
    hours: float,
    topics: str
) -> str:

    return generate_response(
        f"""
Create a practical personalized study plan.

Subject:
{subject}

Exam date:
{exam_date}

Available hours per day:
{hours}

Topics:
{topics}

Include:

- Daily tasks
- Topics
- Revision sessions
- Practice sessions
- Break recommendations
"""
    )