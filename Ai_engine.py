# ai_engine.py

import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

SYSTEM = """
You are Learn It AI, an educational assistant for secondary-school students.

Always adapt responses to:
- grade
- curriculum
- pathway
- subject
- topic
- difficulty
- previous performance
- weak topics

Never claim an AI-generated question is an official WAEC, NECO,
or JAMB past question.

When asked for an official past question, only use a question
provided by the authorized Learn It question database.
"""

def run_ai(feature, student, request):
    context = f"""
Student:
Grade: {student.get("grade")}
Curriculum: {student.get("curriculum")}
Pathway: {student.get("pathway")}
Subject: {student.get("subject")}
Topic: {student.get("topic")}
Difficulty: {student.get("difficulty")}
Weak topics: {student.get("weak_topics", [])}
Recent scores: {student.get("recent_scores", [])}

Learn It feature: {feature}

Student request:
{request}
"""

    response = client.interactions.create(
        model="gemini-3.7-flash",
        input=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": context}
        ]
    )

    return response.output_text
