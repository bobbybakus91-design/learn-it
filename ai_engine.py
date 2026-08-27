# ai_engine.py
#
# LEARN IT AI ENGINE
# ==================
# Central AI layer for all Learn It AI features.
#
# learn_it_engine.py calls:
#
#     run_ai(feature, student, request)
#
# This file is responsible for deciding what AI capability
# should handle the request.

from __future__ import annotations

from typing import Any


# ============================================================
# AI FEATURE REGISTRY
# ============================================================

AI_FEATURES = [
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
