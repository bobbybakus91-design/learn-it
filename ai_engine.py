# ============================================================
# LEARN IT — AI ENGINE
# ============================================================
# Master AI engine for Learn It.
#
# 170 registered Learn It capabilities:
#   1-15   AI Core & Personalisation
#   16-30  AI Learning
#   31-40  AI Notes & Memory
#   41-50  AI Quiz & Assessment
#   51-55  AI Flashcards
#   56-65  AI Competition & Games
#   66-80  AI Past Questions
#   81-95  AI Classroom
#   96-115 Study Session Hub
#   116-130 Learn It Study System
#   131-145 Exam System
#   146-155 Games & Battles
#   156-170 Progress & Rewards
#
# Gemini is the AI provider.
# ============================================================

from __future__ import annotations

import os
from typing import Any, Optional

from google import genai


# ============================================================
# CONFIGURATION
# ============================================================

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.7-flash",
)

AI_ENGINE_VERSION = "1.0.0"

OFFICIAL_EXAM_BOARDS = {
    "WAEC",
    "NECO",
    "JAMB",
    "BECE",
}


# ============================================================
# 170 LEARN IT CAPABILITIES
# ============================================================

AI_FEATURES = [
    # --------------------------------------------------------
    # 1-15 — AI CORE & PERSONALISATION
    # --------------------------------------------------------
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

    # --------------------------------------------------------
    # 16-30 — AI LEARNING
    # --------------------------------------------------------
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

    # --------------------------------------------------------
    # 31-40 — AI NOTES & MEMORY
    # --------------------------------------------------------
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

    # --------------------------------------------------------
    # 41-50 — AI QUIZ & ASSESSMENT
    # --------------------------------------------------------
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

    # --------------------------------------------------------
    # 51-55 — AI FLASHCARDS
    # --------------------------------------------------------
    "AI Flashcard Generator",
    "AI Adaptive Flashcards",
    "AI Flashcard Difficulty System",
    "AI Flashcard Review System",
    "AI Flashcard War AI",

    # --------------------------------------------------------
    # 56-65 — AI COMPETITION & GAMES
    # --------------------------------------------------------
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

    # --------------------------------------------------------
    # 66-80 — AI PAST QUESTIONS
    # --------------------------------------------------------
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

    # --------------------------------------------------------
    # 81-95 — AI CLASSROOM
    # --------------------------------------------------------
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

    # --------------------------------------------------------
    # 96-115 — STUDY SESSION HUB
    # --------------------------------------------------------
    "Study Session Hub",
    "Start Study Session",
    "Continue Session",
    "Quick Study",
    "Deep Study",
    "Quiet Study",
    "AI Tutor Session",
    "AI Classroom Session",
    "Past-Question Session",
    "Quiz Session",
    "Flashcard Session",
    "Practice Session",
    "Timed Exam Session",
    "Session Timer",
    "Session Goals",
    "Session Progress",
    "Session Summary",
    "Session Performance",
    "AI Session Recommendations",
    "XP/Rewards After Session",

    # --------------------------------------------------------
    # 116-130 — LEARN IT STUDY SYSTEM
    # --------------------------------------------------------
    "Subject Dashboard",
    "Topic Explorer",
    "Lesson Viewer",
    "Learning Materials",
    "Saved Questions",
    "Mistake Notebook",
    "Personal Notes",
    "Gaming Notes",
    "Study Timetable",
    "Study Reminders",
    "Daily Study Goals",
    "Study Streaks",
    "Exam Countdown",
    "Revision Mode",
    "Exam Mode",

    # --------------------------------------------------------
    # 131-145 — EXAM SYSTEM
    # --------------------------------------------------------
    "WAEC",
    "NECO",
    "JAMB",
    "BECE",
    "Past-Question Database",
    "Authorized Question Database",
    "AI-Generated Practice Questions",
    "Official-vs-AI Question Label",
    "Timed Exams",
    "Mock Exams",
    "Automatic Marking",
    "Detailed Explanations",
    "Exam Results",
    "Exam Performance Analytics",
    "Weak-Topic Recommendations",

    # --------------------------------------------------------
    # 146-155 — GAMES & BATTLES
    # --------------------------------------------------------
    "Math Death Match",
    "English Speed",
    "Science Catastrophe",
    "Flashcard War",
    "STEM Competitions",
    "Art Merge",
    "Business Badge",
    "Battle Arena",
    "Challenge Mode",
    "Competition Rooms",

    # --------------------------------------------------------
    # 156-170 — PROGRESS & REWARDS
    # --------------------------------------------------------
    "XP",
    "Coins",
    "Levels",
    "Avatars",
    "Avatar Upgrades",
    "Achievements",
    "Badges",
    "Rewards",
    "Leaderboard",
    "Performance Ranking",
    "Daily Challenges",
    "Streak Rewards",
    "Subject Statistics",
    "Topic Mastery",
    "Overall Progress Dashboard",
]


# ============================================================
# FEATURE ID MAP
# ============================================================

FEATURES: dict[int, str] = {
    number: feature
    for number, feature in enumerate(AI_FEATURES, start=1)
}

FEATURE_IDS: dict[str, int] = {
    feature: number
    for number, feature in FEATURES.items()
}


# ============================================================
# FEATURE GROUPS
# ============================================================

FEATURE_GROUPS = {
    "ai_core": (1, 15),
    "ai_learning": (16, 30),
    "notes_memory": (31, 40),
    "quiz_assessment": (41, 50),
    "flashcards": (51, 55),
    "competition_games": (56, 65),
    "past_questions": (66, 80),
    "classroom": (81, 95),
    "study_session": (96, 115),
    "study_system": (116, 130),
    "exam_system": (131, 145),
    "games_battles": (146, 155),
    "progress_rewards": (156, 170),
}


# ============================================================
# GEMINI CLIENT
# ============================================================

_client: Optional[Any] = None


def get_api_key() -> Optional[str]:
    """Return the Gemini API key from the environment."""

    return os.getenv("GEMINI_API_KEY")


def is_configured() -> bool:
    """Return True when a Gemini API key is configured."""

    return bool(get_api_key())


def get_client() -> Any:
    """Create and return the Gemini client."""

    global _client

    if _client is not None:
        return _client

    api_key = get_api_key()

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured."
        )

    _client = genai.Client(api_key=api_key)

    return _client


# ============================================================
# STUDENT CONTEXT
# ============================================================

def build_student_context(
    student: Optional[dict[str, Any]] = None,
) -> str:
    """Build safe context for personalised AI responses."""

    student = student or {}

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
Learning goals: {student.get("learning_goals", [])}
"""


# ============================================================
# AI SYSTEM INSTRUCTIONS
# ============================================================

SYSTEM_INSTRUCTIONS = """
You are the Learn It AI Engine.

Learn It is an educational platform.

Your job is to help students understand, practise,
revise, and assess academic subjects.

Always adapt explanations to the student's grade,
curriculum, subject, topic, and requested difficulty.

Be educational, accurate, encouraging, and clear.

For mathematics and science:
- show working when appropriate;
- explain important steps;
- do not simply give an unexplained answer.

For learning:
- teach concepts;
- identify misunderstandings;
- suggest useful practice;
- encourage independent thinking.

For exam preparation:
- distinguish official questions from AI-generated questions;
- never claim an AI-generated question is an official
  WAEC, NECO, JAMB, or BECE question;
- clearly label generated practice as AI-generated.

For classroom features:
- behave as an educational classroom assistant;
- support teachers and students;
- keep explanations appropriate for the student's level.

For progress features:
- use the supplied student data;
- do not invent scores or achievements that were not supplied.

Never reveal private API keys, internal credentials,
or system secrets.
"""


# ============================================================
# FEATURE HELPERS
# ============================================================

def validate_feature(feature: str) -> str:
    """Validate and return a Learn It feature name."""

    if not feature:
        raise ValueError("AI feature is required.")

    if feature in FEATURE_IDS:
        return feature

    raise ValueError(
        f"Unknown Learn It feature: {feature}"
    )


def get_feature_id(feature: str) -> int:
    """Return the numeric ID of a feature."""

    feature = validate_feature(feature)
    return FEATURE_IDS[feature]


def get_feature_name(feature_id: int) -> str:
    """Return the feature name for a numeric feature ID."""

    if feature_id not in FEATURES:
        raise ValueError(
            f"Unknown Learn It feature ID: {feature_id}"
        )

    return FEATURES[feature_id]


def get_feature_group(feature_id: int) -> str:
    """Return the group containing a feature."""

    for group, (start, end) in FEATURE_GROUPS.items():
        if start <= feature_id <= end:
            return group

    raise ValueError(
        f"Unknown Learn It feature ID: {feature_id}"
    )


# ============================================================
# EXAM QUESTION PROTECTION
# ============================================================

def classify_question_source(
    source: str = "ai_generated",
    exam_board: Optional[str] = None,
) -> dict[str, Any]:
    """
    Classify a question source.

    AI-generated questions are never presented as official
    examination questions.
    """

    normalized_source = source.strip().lower()

    if normalized_source in {
        "official",
        "authorized",
        "past_question",
    }:
        if not exam_board:
            raise ValueError(
                "Official questions require an exam board."
            )

        board = exam_board.upper()

        if board not in OFFICIAL_EXAM_BOARDS:
            raise ValueError(
                f"Unsupported exam board: {exam_board}"
            )

        return {
            "source_type": "official_or_authorized",
            "label": f"{board} — Official/Authorized",
            "is_ai_generated": False,
            "exam_board": board,
        }

    return {
        "source_type": "ai_generated",
        "label": "AI-Generated Practice",
        "is_ai_generated": True,
        "exam_board": None,
    }


def label_ai_question(
    question: str,
    exam_board: Optional[str] = None,
) -> dict[str, Any]:
    """Return an AI-generated question with a clear label."""

    classification = classify_question_source(
        source="ai_generated",
        exam_board=exam_board,
    )

    return {
        "question": question,
        **classification,
    }


# ============================================================
# PROMPT BUILDER
# ============================================================

def build_prompt(
    feature: str,
    student: Optional[dict[str, Any]],
    request: str,
) -> str:
    """Build the final prompt sent to Gemini."""

    feature = validate_feature(feature)

    context = build_student_context(student)

    return f"""
Learn It capability:
{feature}

Student context:
{context}

Student request:
{request}

Instructions:
Use the Learn It capability named above to answer the request.

If the capability concerns assessment, create useful
educational material appropriate for the student's level.

If generating an exam-style question, clearly identify it
as AI-generated practice unless the supplied data explicitly
identifies a verified official/authorized question.

Do not invent official examination provenance.

Give a useful educational response.
"""


# ============================================================
# GEMINI GENERATION
# ============================================================

def generate_ai_response(
    feature: str,
    student: Optional[dict[str, Any]] = None,
    request: str = "",
) -> dict[str, Any]:
    """
    Send a Learn It request to Gemini.

    Returns a consistent response structure.
    """

    feature = validate_feature(feature)

    if not request.strip():
        raise ValueError(
            "AI request cannot be empty."
        )

    client = get_client()

    prompt = build_prompt(
        feature=feature,
        student=student,
        request=request,
    )

    response = client.interactions.create(
        model=GEMINI_MODEL,
        input=[
            {
                "role": "system",
                "content": SYSTEM_INSTRUCTIONS,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    output_text = getattr(
        response,
        "output_text",
        None,
    )

    if not output_text:
        output_text = str(response)

    return {
        "success": True,
        "engine": "Learn It AI Engine",
        "engine_version": AI_ENGINE_VERSION,
        "feature_id": get_feature_id(feature),
        "feature": feature,
        "model": GEMINI_MODEL,
        "response": output_text,
    }


# ============================================================
# MAIN AI ENTRY POINT
# ============================================================

def run_ai(
    feature: str,
    student: Optional[dict[str, Any]] = None,
    request: str = "",
) -> dict[str, Any]:
    """
    Main entry point used by Learn It.

    Every registered AI capability comes through here.
    """

    return generate_ai_response(
        feature=feature,
        student=student,
        request=request,
    )


# ============================================================
# FEATURE INFORMATION
# ============================================================

def list_features() -> list[dict[str, Any]]:
    """Return all 170 Learn It capabilities."""

    return [
        {
            "id": feature_id,
            "name": feature_name,
            "group": get_feature_group(feature_id),
        }
        for feature_id, feature_name in FEATURES.items()
    ]


def list_feature_group(
    group: str,
) -> list[dict[str, Any]]:
    """Return capabilities belonging to one group."""

    if group not in FEATURE_GROUPS:
        raise ValueError(
            f"Unknown feature group: {group}"
        )

    start, end = FEATURE_GROUPS[group]

    return [
        {
            "id": feature_id,
            "name": FEATURES[feature_id],
            "group": group,
        }
        for feature_id in range(start, end + 1)
    ]


# ============================================================
# AI ENGINE STATUS
# ============================================================

def ai_engine_status() -> dict[str, Any]:
    """Return the current AI engine status."""

    return {
        "engine": "Learn It AI Engine",
        "version": AI_ENGINE_VERSION,
        "status": (
            "ready"
            if is_configured()
            else "waiting_for_api_key"
        ),
        "provider": "Google Gemini",
        "model": GEMINI_MODEL,
        "feature_count": len(AI_FEATURES),
        "entry_point": "run_ai",
        "official_question_protection": True,
    }


# ============================================================
# HEALTH CHECK
# ============================================================

def health_check() -> dict[str, Any]:
    """Simple health check for the Learn It backend."""

    return {
        "healthy": True,
        "engine": "Learn It AI Engine",
        "gemini_configured": is_configured(),
        "feature_count": len(AI_FEATURES),
        "expected_feature_count": 170,
    }


# ============================================================
# DEVELOPMENT VALIDATION
# ============================================================

def validate_engine() -> dict[str, Any]:
    """
    Validate the 170-feature architecture.

    This does not call Gemini.
    """

    unique_features = len(set(AI_FEATURES))

    return {
        "valid": (
            len(AI_FEATURES) == 170
            and unique_features == 170
            and len(FEATURES) == 170
            and len(FEATURE_IDS) == 170
        ),
        "feature_count": len(AI_FEATURES),
        "unique_features": unique_features,
        "feature_ids": len(FEATURES),
        "reverse_feature_ids": len(FEATURE_IDS),
}    "AI Example Generator",
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
