from __future__ import annotations

import os
from typing import Any

from google import genai


# ============================================================
# LEARN IT AI ENGINE
# ============================================================

AI_FEATURES = [
    # AI CORE & PERSONALISATION
    "AI Tutor",
    "AI Teacher",
    "AI Teacher Personalities",
    "AI Student Context",
    "AI Personalised Learning",
    "AI Learning-Path Generator",
    "AI Study-Plan Generator",
    "AI Difficulty Adaptation",
    "AI Weakness Detector",
    "AI Strength Detector",
    "AI Performance Analyst",
    "AI Topic Mastery Predictor",
    "AI Revision Recommender",
    "AI Next-Lesson Recommender",
    "AI Exam Readiness Analyzer",

    # AI LEARNING
    "AI Lesson Generator",
    "AI Topic Explainer",
    "AI Simple Explanation Mode",
    "AI Deep Explanation Mode",
    "AI Step-by-Step Solver",
    "AI Example Generator",
    "AI Practice Generator",
    "AI Homework Helper",
    "AI Assignment Assistant",
    "AI Study Coach",
    "AI Socratic Tutor",
    "AI Mistake Explainer",
    "AI Answer Checker",
    "AI Concept Checker",
    "AI Knowledge Gap Detector",

    # AI NOTES & MEMORY
    "AI Notes Generator",
    "AI Notes Summarizer",
    "AI Note Improver",
    "AI Key-Point Extractor",
    "AI Formula Extractor",
    "AI Definition Generator",
    "AI Study Guide Generator",
    "AI Revision Sheet Generator",
    "AI Memory Assistant",
    "AI Mnemonic Generator",

    # AI QUIZ & ASSESSMENT
    "AI Quiz Generator",
    "AI Adaptive Quiz",
    "AI Quiz Marker",
    "AI Quiz Explainer",
    "AI Difficulty Generator",
    "AI Multiple-Choice Generator",
    "AI True/False Generator",
    "AI Short-Answer Generator",
    "AI Exam Simulator",
    "AI Timed-Test Generator",

    # AI FLASHCARDS
    "AI Flashcard Generator",
    "AI Adaptive Flashcards",
    "AI Flashcard Difficulty System",
    "AI Flashcard Review System",
    "AI Flashcard War AI",

    # AI COMPETITION & GAMES
    "AI Math Death Match",
    "AI English Speed",
    "AI Science Catastrophe",
    "AI STEM Competition",
    "AI Art Merge",
    "AI Business Badge",
    "AI Challenge Generator",
    "AI Competition Opponent",
    "AI Game Difficulty Balancer",
    "AI Game Coach",

    # AI PAST QUESTIONS
    "AI WAEC Question Coach",
    "AI NECO Question Coach",
    "AI JAMB Question Coach",
    "AI BECE Question Coach",
    "AI Past-Question Analyzer",

    # ADDITIONAL AI
    "AI Question Similarity Detector",
    "AI Duplicate Question Detector",
    "AI Question Difficulty Classifier",
    "AI Curriculum Alignment Checker",
    "AI Topic Classification",
    "AI Question Explanation Generator",
    "AI Exam Trend Analyzer",
    "AI Personalized Past-Question Recommender",
    "AI Revision Scheduler",
    "AI Learning Progress Predictor",

    # AI CLASSROOM
    "AI Classroom",
    "AI Teacher Presentation",
    "AI Classroom Lesson",
    "AI Classroom Q&A",
    "AI Interactive Examples",
    "AI Classroom Quiz",
    "AI Classroom Activities",
    "AI Classroom Homework",
    "AI Classroom Assessment",
    "AI Classroom Progress Tracking",
    "AI Classroom Voice Interaction",
    "AI Classroom Participation System",
    "AI Classroom Recap",
    "AI Classroom Assignment Generator",
    "AI Classroom Personalized Help",
]


# ============================================================
# CONFIGURATION
# ============================================================

GEMINI_MODEL = "gemini-3.7-flash"


# ============================================================
# GEMINI CLIENT
# ============================================================

def get_client():
    api_key = os.getenv(AQ.Ab8RN6Iy423fCNeEfm9S_F-EF-xanDIjhpS2T_8ATrES1LeNUw)

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured."
        )

    return genai.Client(api_key=api_key)


# ============================================================
# STUDENT CONTEXT
# ============================================================

def build_student_context(student: dict) -> str:
    return f"""
Student name: {student.get("name", "Student")}
Grade: {student.get("grade", "JSS3")}
Curriculum: {student.get("curriculum", "Nigerian")}
Pathway: {student.get("pathway", "General")}
Subject: {student.get("subject", "")}
Topic: {student.get("topic", "")}
Difficulty: {student.get("difficulty", "normal")}
Weak topics: {student.get("weak_topics", [])}
Strong topics: {student.get("strong_topics", [])}
Recent scores: {student.get("recent_scores", [])}
"""


# ============================================================
# LEARN IT AI INSTRUCTIONS
# ============================================================

SYSTEM_INSTRUCTIONS = """
You are Learn It AI.

You are an educational AI designed to help students learn.

Your goals are:

- explain concepts clearly
- teach step by step
- adapt explanations to the student's level
- encourage understanding rather than copying answers
- provide examples and practice
- identify mistakes and explain them
- help students prepare for examinations
- use the student's learning context when appropriate

IMPORTANT EXAM RULE:

Never claim that an AI-generated question is an official
WAEC, NECO, JAMB, or BECE question.

If you generate a practice question yourself, clearly identify
it as AI-generated practice.

Official examination questions must remain separate from
AI-generated questions.

Use clear, age-appropriate educational language.
"""


# ============================================================
# AI RESPONSE
# ============================================================

def generate_ai_response(
    feature: str,
    student: dict,
    request: str,
) -> dict[str, Any]:

    client = get_client()

    student_context = build_student_context(student)

    prompt = f"""
Student context:
{student_context}

Selected Learn It AI feature:
{feature}

Student request:
{request}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "system_instruction": SYSTEM_INSTRUCTIONS,
        },
    )

    return {
        "feature": feature,
        "status": "success",
        "model": GEMINI_MODEL,
        "response": response.text,
    }


# ============================================================
# MAIN AI ENTRY POINT
# ============================================================

def run_ai(
    feature: str,
    student: dict,
    request: str,
) -> dict[str, Any]:

    if not feature:
        raise ValueError(
            "AI feature is required."
        )

    if feature not in AI_FEATURES:
        raise ValueError(
            f"Unknown AI feature: {feature}"
        )

    return generate_ai_response(
        feature=feature,
        student=student,
        request=request,
    )


# ============================================================
# AI ENGINE STATUS
# ============================================================

def ai_engine_status() -> dict[str, Any]:

    configured = bool(
        os.getenv("GEMINI_API_KEY")
    )

    return {
        "engine": "Learn It AI Engine",
        "status": (
            "ready"
            if configured
            else "waiting_for_api_key"
        ),
        "provider": "Google Gemini",
        "model": GEMINI_MODEL,
        "features": len(AI_FEATURES),
        "entry_point": "run_ai",
    }, AI_FEATURES = [
    "AI Homework Helper",
    "AI Assignment Assistant",
    "AI Study Coach",
    "AI Socratic Tutor",
    "AI Mistake Explainer",
    "AI Answer Checker",
    "AI Concept Checker",
    "AI Knowledge Gap Detector",

    "AI Notes Generator",
    "AI Notes Summarizer",
    "AI Note Improver",
    "AI Key-Point Extractor",
    "AI Formula Extractor",
    "AI Definition Generator",
    "AI Study Guide Generator",
    "AI Revision Sheet Generator",
    "AI Memory Assistant",
    "AI Mnemonic Generator",

    "AI Quiz Generator",
    "AI Adaptive Quiz",
    "AI Quiz Marker",
    "AI Quiz Explainer",
    "AI Difficulty Generator",
    "AI Multiple-Choice Generator",
    "AI True/False Generator",
    "AI Short-Answer Generator",
    "AI Exam Simulator",
    "AI Timed-Test Generator",

    "AI Flashcard Generator",
    "AI Adaptive Flashcards",
    "AI Flashcard Difficulty System",
    "AI Flashcard Review System",
    "AI Flashcard War AI",

    "AI Math Death Match",
    "AI English Speed",
    "AI Science Catastrophe",
    "AI STEM Competition",
    "AI Art Merge",
    "AI Business Badge",
    "AI Challenge Generator",
    "AI Competition Opponent",
    "AI Game Difficulty Balancer",
    "AI Game Coach",

    "AI WAEC Question Coach",
    "AI NECO Question Coach",
    "AI JAMB Question Coach",
    "AI BECE Question Coach",
    "AI Past-Question Analyzer",

    "AI Question Similarity Detector",
    "AI Duplicate Question Detector",
    "AI Question Difficulty Classifier",
    "AI Curriculum Alignment Checker",
    "AI Topic Classification",
    "AI Question Explanation Generator",
    "AI Exam Trend Analyzer",
    "AI Personalized Past-Question Recommender",
    "AI Revision Scheduler",
    "AI Learning Progress Predictor",

    "AI Classroom",
    "AI Teacher Presentation",
    "AI Classroom Lesson",
    "AI Classroom Q&A",
    "AI Interactive Examples",
    "AI Classroom Quiz",
    "AI Classroom Activities",
    "AI Classroom Homework",
    "AI Classroom Assessment",
    "AI Classroom Progress Tracking",
    "AI Classroom Voice Interaction",
    "AI Classroom Participation System",
    "AI Classroom Recap",
    "AI Classroom Assignment Generator",
    "AI Classroom Personalized Help",
]


# ============================================================
# GEMINI CONFIGURATION
# ============================================================

GEMINI_MODEL = "gemini-3.7-flash"


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured."
        )

    return genai.Client(api_key=api_key)


# ============================================================
# STUDENT CONTEXT
# ============================================================

def build_student_context(student: dict) -> str:

    return f"""
Student name: {student.get("name", "Student")}
Grade: {student.get("grade", "JSS3")}
Curriculum: {student.get("curriculum", "Nigerian")}
Pathway: {student.get("pathway", "General")}
Subject: {student.get("subject", "")}
Topic: {student.get("topic", "")}
Difficulty: {student.get("difficulty", "normal")}
"""


# ============================================================
# LEARN IT AI INSTRUCTIONS
# ============================================================

SYSTEM_INSTRUCTIONS = """
You are Learn It AI.

You are an educational AI designed to help students learn.

Your goals are:
- explain concepts clearly
- teach step by step
- adapt explanations to the student's level
- encourage understanding rather than copying answers
- provide examples and practice
- identify mistakes and explain them
- help students prepare for examinations
- keep official examination questions separate from AI-generated practice

The student context supplied to you is important.

Never claim that an AI-generated question is an official
WAEC, NECO, JAMB, or BECE question.

If a question is generated by AI, clearly treat it as
AI-generated practice.

Use clear, age-appropriate educational language.
"""


# ============================================================
# GEMINI RESPONSE
# ============================================================

def generate_ai_response(
    feature: str,
    student: dict,
    request: str,
) -> dict[str, Any]:

    client = get_client()

    student_context = build_student_context(student)

    prompt = f"""
{SYSTEM_INSTRUCTIONS}

Learn It AI feature:
{feature}

Student context:
{student_context}

Student request:
{request}

Respond specifically for the selected Learn It feature.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    return {
        "feature": feature,
        "status": "success",
        "model": GEMINI_MODEL,
        "response": response.text,
    }


# ============================================================
# MAIN AI ENTRY POINT
# ============================================================

def run_ai(
    feature: str,
    student: dict,
    request: str,
) -> dict[str, Any]:

    if not feature:
        raise ValueError(
            "AI feature is required."
        )

    if feature not in AI_FEATURES:
        if not feature.startswith("AI "):
            raise ValueError(
                f"Unknown AI feature: {feature}"
            )

    return generate_ai_response(
        feature=feature,
        student=student,
        request=request,
    )


# ============================================================
# AI ENGINE STATUS
# ============================================================

def ai_engine_status() -> dict[str, Any]:

    configured = bool(
        os.getenv("GEMINI_API_KEY")
    )

    return {
        "engine": "Learn It AI Engine",
        "status": (
            "ready"
            if configured
            else "waiting_for_api_key"
        ),
        "provider": "Google Gemini",
        "model": GEMINI_MODEL,
        "features": len(AI_FEATURES),
        "entry_point": "run_ai",
},    AI_FEATURES = [
    "AI Next-Lesson Recommender",
    "AI Exam Readiness Analyzer",

    "AI Lesson Generator",
    "AI Topic Explainer",
    "AI Simple Explanation Mode",
    "AI Deep Explanation Mode",
    "AI Step-by-Step Solver",
    "AI Example Generator",
    "AI Practice Generator",
    "AI Homework Helper",
    "AI Assignment Assistant",
    "AI Study Coach",
    "AI Socratic Tutor",
    "AI Mistake Explainer",
    "AI Answer Checker",
    "AI Concept Checker",
    "AI Knowledge Gap Detector",

    "AI Notes Generator",
    "AI Notes Summarizer",
    "AI Note Improver",
    "AI Key-Point Extractor",
    "AI Formula Extractor",
    "AI Definition Generator",
    "AI Study Guide Generator",
    "AI Revision Sheet Generator",
    "AI Memory Assistant",
    "AI Mnemonic Generator",

    "AI Quiz Generator",
    "AI Adaptive Quiz",
    "AI Quiz Marker",
    "AI Quiz Explainer",
    "AI Difficulty Generator",
    "AI Multiple-Choice Generator",
    "AI True/False Generator",
    "AI Short-Answer Generator",
    "AI Exam Simulator",
    "AI Timed-Test Generator",

    "AI Flashcard Generator",
    "AI Adaptive Flashcards",
    "AI Flashcard Difficulty System",
    "AI Flashcard Review System",
    "AI Flashcard War AI",

    "AI Math Death Match",
    "AI English Speed",
    "AI Science Catastrophe",
    "AI STEM Competition",
    "AI Art Merge",
    "AI Business Badge",
    "AI Challenge Generator",
    "AI Competition Opponent",
    "AI Game Difficulty Balancer",
    "AI Game Coach",

    "AI WAEC Question Coach",
    "AI NECO Question Coach",
    "AI JAMB Question Coach",
    "AI BECE Question Coach",
    "AI Past-Question Analyzer",

    "AI Question Similarity Detector",
    "AI Duplicate Question Detector",
    "AI Question Difficulty Classifier",
    "AI Curriculum Alignment Checker",
    "AI Topic Classification",
    "AI Question Explanation Generator",
    "AI Exam Trend Analyzer",
    "AI Personalized Past-Question Recommender",
    "AI Revision Scheduler",
    "AI Learning Progress Predictor",

    "AI Classroom",
    "AI Teacher Presentation",
    "AI Classroom Lesson",
    "AI Classroom Q&A",
    "AI Interactive Examples",
    "AI Classroom Quiz",
    "AI Classroom Activities",
    "AI Classroom Homework",
    "AI Classroom Assessment",
    "AI Classroom Progress Tracking",
    "AI Classroom Voice Interaction",
    "AI Classroom Participation System",
    "AI Classroom Recap",
    "AI Classroom Assignment Generator",
    "AI Classroom Personalized Help",
]


# ============================================================
# AI PROVIDER
# ============================================================

def generate_ai_response(
    feature: str,
    student: dict,
    request: str,
) -> dict[str, Any]:
    """
    Temporary AI provider layer.

    This keeps the Learn It architecture ready for the
    actual AI model/API without changing the rest of the app.
    """

    return {
        "feature": feature,
        "status": "ai_ready",
        "message": (
            f"Learn It AI received a request for '{feature}'."
        ),
        "student": {
            "id": student.get("id"),
            "name": student.get("name"),
            "grade": student.get("grade"),
            "curriculum": student.get("curriculum"),
            "pathway": student.get("pathway"),
            "subject": student.get("subject"),
            "topic": student.get("topic"),
            "difficulty": student.get("difficulty"),
        },
        "request": request,
    }


# ============================================================
# MAIN AI ENTRY POINT
# ============================================================

def run_ai(
    feature: str,
    student: dict,
    request: str,
) -> dict[str, Any]:

    if not feature:
        raise ValueError("AI feature is required.")

    if feature not in AI_FEATURES:
        # Classroom/session features can also reach the AI engine.
        if not feature.startswith("AI "):
            raise ValueError(
                f"Unknown AI feature: {feature}"
            )

    return generate_ai_response(
        feature=feature,
        student=student,
        request=request,
    )


# ============================================================
# AI ENGINE STATUS
# ============================================================

def ai_engine_status() -> dict[str, Any]:

    return {
        "engine": "Learn It AI Engine",
        "status": "ready",
        "features": len(AI_FEATURES),
        "entry_point": "run_ai",
}Weak topics: {student.get("weak_topics", [])}
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
