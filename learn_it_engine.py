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
}
# ============================================================
# EXISTING AI ENGINE
# ============================================================

try:
    from ai_engine import run_ai
    AI_ENGINE_AVAILABLE = True
except ImportError:
    AI_ENGINE_AVAILABLE = False

    def run_ai(feature, student, request):
        raise RuntimeError(
            "ai_engine.py was not found. "
            "Place your existing ai_engine.py beside learn_it_engine.py."
        )


# ============================================================
# APPLICATION
# ============================================================

app = FastAPI(
    title="Learn It Core Engine",
    description="Core engine powering all 170 Learn It features.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# DATABASE
# ============================================================

DATABASE = "learn_it.db"


def connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def initialize_database():

    conn = connection()

    conn.executescript(
        """

        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            grade TEXT DEFAULT 'JSS3',
            curriculum TEXT DEFAULT 'Nigerian',
            pathway TEXT DEFAULT 'General',
            subject TEXT DEFAULT '',
            topic TEXT DEFAULT '',
            difficulty TEXT DEFAULT 'normal',

            xp INTEGER DEFAULT 0,
            coins INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            streak INTEGER DEFAULT 0,

            weak_topics TEXT DEFAULT '[]',
            strong_topics TEXT DEFAULT '[]',
            recent_scores TEXT DEFAULT '[]',

            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS study_sessions (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            subject TEXT,
            topic TEXT,
            mode TEXT,

            goal TEXT,
            status TEXT DEFAULT 'active',

            progress REAL DEFAULT 0,
            score REAL DEFAULT 0,

            started_at TEXT NOT NULL,
            ended_at TEXT
        );

        CREATE TABLE IF NOT EXISTS classrooms (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            subject TEXT,
            topic TEXT,

            teacher_personality TEXT DEFAULT 'standard',

            status TEXT DEFAULT 'active',

            created_at TEXT NOT NULL,
            ended_at TEXT
        );

        CREATE TABLE IF NOT EXISTS quizzes (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            subject TEXT,
            topic TEXT,
            difficulty TEXT,

            questions TEXT DEFAULT '[]',
            answers TEXT DEFAULT '[]',
            correct_answers TEXT DEFAULT '[]',

            score REAL DEFAULT 0,
            completed INTEGER DEFAULT 0,

            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS exams (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            exam_type TEXT,
            subject TEXT,
            year INTEGER,

            questions TEXT DEFAULT '[]',
            answers TEXT DEFAULT '[]',

            score REAL DEFAULT 0,
            status TEXT DEFAULT 'created',

            created_at TEXT NOT NULL,
            completed_at TEXT
        );

        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            exam_type TEXT NOT NULL,
            subject TEXT NOT NULL,
            topic TEXT,

            year INTEGER,

            source_type TEXT NOT NULL,

            prompt TEXT NOT NULL,
            options TEXT DEFAULT '[]',
            answer TEXT,
            explanation TEXT,

            authorized INTEGER DEFAULT 0,

            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS notes (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            title TEXT,
            body TEXT,

            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS flashcards (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            subject TEXT,
            topic TEXT,

            front TEXT,
            back TEXT,

            difficulty TEXT DEFAULT 'normal',
            confidence INTEGER DEFAULT 0,

            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_id TEXT,
            feature_id INTEGER,
            event TEXT,

            payload TEXT DEFAULT '{}',

            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS achievements (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            name TEXT,
            description TEXT,

            unlocked_at TEXT
        );

        CREATE TABLE IF NOT EXISTS games (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            game TEXT,
            mode TEXT,

            score INTEGER DEFAULT 0,
            opponent TEXT,

            status TEXT DEFAULT 'active',

            created_at TEXT NOT NULL,
            ended_at TEXT
        );

        """
    )

    conn.commit()
    conn.close()


initialize_database()


# ============================================================
# 170 FEATURE REGISTRY
# ============================================================

FEATURE_NAMES = [
    # 1-15 AI CORE
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

    # 16-30 AI LEARNING
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

    # 31-40 AI NOTES
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

    # 41-50 AI QUIZ
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

    # 51-55 AI FLASHCARDS
    "AI Flashcard Generator",
    "AI Adaptive Flashcards",
    "AI Flashcard Difficulty System",
    "AI Flashcard Review System",
    "AI Flashcard War AI",

    # 56-65 AI GAMES
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

    # 66-70 AI PAST QUESTIONS
    "AI WAEC Question Coach",
    "AI NECO Question Coach",
    "AI JAMB Question Coach",
    "AI BECE Question Coach",
    "AI Past-Question Analyzer",

    # 71-80 ADDITIONAL AI
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

    # 81-95 AI CLASSROOM
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

    # 96-115 STUDY SESSION HUB
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

    # 116-130 STUDY SYSTEM
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

    # 131-145 EXAMS
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

    # 146-155 GAMES
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

    # 156-170 PROGRESS / REWARDS
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


assert len(FEATURE_NAMES) == 170


# ============================================================
# FEATURE CLASSIFICATION
# ============================================================

AI_FEATURE_IDS = set(range(1, 96))

HYBRID_FEATURE_IDS = {
    96,
    102,
    103,
    114,
}

CORE_FEATURE_IDS = (
    set(range(96, 171)) - HYBRID_FEATURE_IDS
)


def feature_info(feature_id: int):

    if feature_id < 1 or feature_id > 170:
        raise ValueError("Feature ID must be between 1 and 170.")

    if feature_id in HYBRID_FEATURE_IDS:
        mode = "hybrid"
    elif feature_id in AI_FEATURE_IDS:
        mode = "ai"
    else:
        mode = "core"

    return {
        "id": feature_id,
        "name": FEATURE_NAMES[feature_id - 1],
        "mode": mode,
        "enabled": True,
    }


FEATURES = {
    feature_id: feature_info(feature_id)
    for feature_id in range(1, 171)
}


# ============================================================
# STUDENT ENGINE
# ============================================================

class StudentEngine:

    @staticmethod
    def create(data: dict):

        student_id = data.get("id") or str(uuid.uuid4())

        timestamp = utc_now()

        conn = connection()

        conn.execute(
            """
            INSERT OR REPLACE INTO students
            (
                id,
                name,
                grade,
                curriculum,
                pathway,
                subject,
                topic,
                difficulty,
                xp,
                coins,
                level,
                streak,
                weak_topics,
                strong_topics,
                recent_scores,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                student_id,
                data.get("name", "Student"),
                data.get("grade", "JSS3"),
                data.get("curriculum", "Nigerian"),
                data.get("pathway", "General"),
                data.get("subject", ""),
                data.get("topic", ""),
                data.get("difficulty", "normal"),
                data.get("xp", 0),
                data.get("coins", 0),
                data.get("level", 1),
                data.get("streak", 0),
                json.dumps(data.get("weak_topics", [])),
                json.dumps(data.get("strong_topics", [])),
                json.dumps(data.get("recent_scores", [])),
                data.get("created_at", timestamp),
                timestamp,
            ),
        )

        conn.commit()
        conn.close()

        return StudentEngine.get(student_id)

    @staticmethod
    def get(student_id: str):

        conn = connection()

        row = conn.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()

        conn.close()

        if not row:
            return StudentEngine.create(
                {
                    "id": student_id,
                    "name": "Student",
                }
            )

        student = dict(row)

        student["weak_topics"] = json.loads(
            student.get("weak_topics") or "[]"
        )

        student["strong_topics"] = json.loads(
            student.get("strong_topics") or "[]"
        )

        student["recent_scores"] = json.loads(
            student.get("recent_scores") or "[]"
        )

        return student

    @staticmethod
    def update(student_id: str, updates: dict):

        student = StudentEngine.get(student_id)

        for key, value in updates.items():

            if key in student:
                student[key] = value

        student["updated_at"] = utc_now()

        conn = connection()

        conn.execute(
            """
            UPDATE students
            SET
                name=?,
                grade=?,
                curriculum=?,
                pathway=?,
                subject=?,
                topic=?,
                difficulty=?,
                xp=?,
                coins=?,
                level=?,
                streak=?,
                weak_topics=?,
                strong_topics=?,
                recent_scores=?,
                updated_at=?
            WHERE id=?
            """,
            (
                student["name"],
                student["grade"],
                student["curriculum"],
                student["pathway"],
                student["subject"],
                student["topic"],
                student["difficulty"],
                student["xp"],
                student["coins"],
                student["level"],
                student["streak"],
                json.dumps(student["weak_topics"]),
                json.dumps(student["strong_topics"]),
                json.dumps(student["recent_scores"]),
                student["updated_at"],
                student_id,
            ),
        )

        conn.commit()
        conn.close()

        return StudentEngine.get(student_id)


student_engine = StudentEngine()


# ============================================================
# PROGRESS ENGINE
# ============================================================

class ProgressEngine:

    @staticmethod
    def score(correct: int, total: int):

        if total <= 0:
            return 0.0

        return round(
            (correct / total) * 100,
            2,
        )

    @staticmethod
    def level_for_xp(xp: int):

        return max(
            1,
            (xp // 100) + 1,
        )

    @staticmethod
    def add_xp(
        student_id: str,
        amount: int,
    ):

        student = student_engine.get(student_id)

        student["xp"] += max(0, amount)

        student["level"] = ProgressEngine.level_for_xp(
            student["xp"]
        )

        student_engine.update(
            student_id,
            {
                "xp": student["xp"],
                "level": student["level"],
            },
        )

        return student_engine.get(student_id)

    @staticmethod
    def add_coins(
        student_id: str,
        amount: int,
    ):

        student = student_engine.get(student_id)

        student["coins"] += max(0, amount)

        student_engine.update(
            student_id,
            {
                "coins": student["coins"],
            },
        )

        return student_engine.get(student_id)

    @staticmethod
    def record_score(
        student_id: str,
        score: float,
    ):

        student = student_engine.get(student_id)

        scores = student["recent_scores"]

        scores.append(score)

        scores = scores[-30:]

        student_engine.update(
            student_id,
            {
                "recent_scores": scores,
            },
        )

        return scores


progress_engine = ProgressEngine()


# ============================================================
# EVENT ENGINE
# ============================================================

class EventEngine:

    @staticmethod
    def log(
        student_id: str,
        feature_id: int,
        event: str,
        payload: Optional[dict] = None,
    ):

        conn = connection()

        conn.execute(
            """
            INSERT INTO events
            (
                student_id,
                feature_id,
                event,
                payload,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                student_id,
                feature_id,
                event,
                json.dumps(payload or {}),
                utc_now(),
            ),
        )

        conn.commit()
        conn.close()


event_engine = EventEngine()


# ============================================================
# STUDY SESSION ENGINE
# ============================================================

class StudySessionEngine:

    @staticmethod
    def start(
        student_id: str,
        subject: str,
        topic: str = "",
        mode: str = "standard",
        goal: str = "",
    ):

        session_id = str(uuid.uuid4())

        conn = connection()

        conn.execute(
            """
            INSERT INTO study_sessions
            (
                id,
                student_id,
                subject,
                topic,
                mode,
                goal,
                status,
                progress,
                started_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                session_id,
                student_id,
                subject,
                topic,
                mode,
                goal,
                "active",
                0,
                utc_now(),
            ),
        )

        conn.commit()
        conn.close()

        event_engine.log(
            student_id,
            96,
            "study_session_started",
            {
                "session_id": session_id,
                "mode": mode,
            },
        )

        return StudySessionEngine.get(session_id)

    @staticmethod
    def get(session_id: str):

        conn = connection()

        row = conn.execute(
            """
            SELECT *
            FROM study_sessions
            WHERE id=?
            """,
            (session_id,),
        ).fetchone()

        conn.close()

        if not row:
            raise HTTPException(
                status_code=404,
                detail="Study session not found.",
            )

        return dict(row)

    @staticmethod
    def update(
        session_id: str,
        progress: Optional[float] = None,
        status: Optional[str] = None,
        score: Optional[float] = None,
    ):

        session = StudySessionEngine.get(session_id)

        if progress is not None:
            session["progress"] = max(
                0,
                min(100, progress),
            )

        if status is not None:
            session["status"] = status

        if score is not None:
            session["score"] = score

        ended_at = session["ended_at"]

        if session["status"] == "completed":
            ended_at = utc_now()

        conn = connection()

        conn.execute(
            """
            UPDATE study_sessions
            SET progress=?,
                status=?,
                score=?,
                ended_at=?
            WHERE id=?
            """,
            (
                session["progress"],
                session["status"],
                session["score"],
                ended_at,
                session_id,
            ),
        )

        conn.commit()
        conn.close()

        if session["status"] == "completed":
            ProgressEngine.add_xp(
                session["student_id"],
                25,
            )

            ProgressEngine.add_coins(
                session["student_id"],
                5,
            )

            event_engine.log(
                session["student_id"],
                115,
                "study_session_reward",
                {
                    "xp": 25,
                    "coins": 5,
                },
            )

        return StudySessionEngine.get(session_id)


study_engine = StudySessionEngine()


# ============================================================
# AI BRIDGE
# ============================================================

class AIBridge:

    @staticmethod
    def run(
        feature_name: str,
        student: dict,
        request: str,
    ):

        if not AI_ENGINE_AVAILABLE:
            raise HTTPException(
                status_code=503,
                detail=(
                    "AI engine unavailable. "
                    "Your existing ai_engine.py must be placed "
                    "beside learn_it_engine.py."
                ),
            )

        return run_ai(
            feature_name,
            student,
            request,
        )


ai_bridge = AIBridge()


# ============================================================
# AI FEATURE ROUTER
# ============================================================

class FeatureRouter:

    @staticmethod
    def execute(
        feature_id: int,
        student_id: str,
        request: str = "",
    ):

        if feature_id not in FEATURES:
            raise HTTPException(
                status_code=404,
                detail="Unknown Learn It feature.",
            )

        feature = FEATURES[feature_id]

        student = student_engine.get(
            student_id
        )

        event_engine.log(
            student_id,
            feature_id,
            "feature_started",
            {
                "feature": feature["name"],
                "request": request,
            },
        )

        # ----------------------------------------------------
        # AI
        # ----------------------------------------------------

        if feature["mode"] == "ai":

            result = ai_bridge.run(
                feature["name"],
                student,
                request,
            )

            event_engine.log(
                student_id,
                feature_id,
                "ai_feature_completed",
            )

            return {
                "feature": feature,
                "type": "ai",
                "result": result,
            }

        # ----------------------------------------------------
        # HYBRID
        # ----------------------------------------------------

        if feature["mode"] == "hybrid":

            result = FeatureRouter.hybrid(
                feature_id,
                student,
                request,
            )

            return {
                "feature": feature,
                "type": "hybrid",
                "result": result,
            }

        # ----------------------------------------------------
        # CORE
        # ----------------------------------------------------

        result = FeatureRouter.core(
            feature_id,
            student,
            request,
        )

        event_engine.log(
            student_id,
            feature_id,
            "core_feature_completed",
        )

        return {
            "feature": feature,
            "type": "core",
            "result": result,
        }

    @staticmethod
    def hybrid(
        feature_id: int,
        student: dict,
        request: str,
    ):

        feature = FEATURES[feature_id]

        # Study Session Hub
        if feature_id == 96:

            return {
                "status": "ready",
                "system": "Study Session Hub",
                "available_modes": [
                    "quick",
                    "deep",
                    "quiet",
                    "tutor",
                    "classroom",
                    "past_questions",
                    "quiz",
                    "flashcards",
                    "practice",
                    "timed_exam",
                ],
            }

        # AI Tutor Session
        if feature_id == 102:

            return ai_bridge.run(
                "AI Tutor Session",
                student,
                request,
            )

        # AI Classroom Session
        if feature_id == 103:

            return ai_bridge.run(
                "AI Classroom Session",
                student,
                request,
            )

        # AI Session Recommendations
        if feature_id == 114:

            return ai_bridge.run(
                "AI Session Recommendations",
                student,
                request,
            )

        return ai_bridge.run(
            feature["name"],
            student,
            request,
        )

    @staticmethod
    def core(
        feature_id: int,
        student: dict,
        request: str,
    ):

        name = FEATURES[feature_id]["name"]

        # ---------------------------------------------
        # SESSION FEATURES
        # ---------------------------------------------

        if 97 <= feature_id <= 115:

            return {
                "feature": name,
                "status": "available",
                "student_id": student["id"],
            }

        # ---------------------------------------------
        # STUDY SYSTEM
        # ---------------------------------------------

        if 116 <= feature_id <= 130:

            return {
                "feature": name,
                "status": "available",
                "student_id": student["id"],
                "subject": student["subject"],
                "topic": student["topic"],
            }

        # ---------------------------------------------
        # EXAMS
        # ---------------------------------------------

        if 131 <= feature_id <= 145:

            return {
                "feature": name,
                "status": "available",
                "exam_system": True,
                "student_id": student["id"],
            }

        # ---------------------------------------------
        # GAMES
        # ---------------------------------------------

        if 146 <= feature_id <= 155:

            return {
                "feature": name,
                "status": "game_ready",
                "student_id": student["id"],
            }

        # ---------------------------------------------
        # PROGRESS / REWARDS
        # ---------------------------------------------

        if 156 <= feature_id <= 170:

            return {
                "feature": name,
                "status": "available",
                "xp": student["xp"],
                "coins": student["coins"],
                "level": student["level"],
                "streak": student["streak"],
            }

        return {
            "feature": name,
            "status": "available",
        }


feature_router = FeatureRouter()


# ============================================================
# QUIZ ENGINE
# ============================================================

class QuizEngine:

    @staticmethod
    def calculate_score(
        answers: list,
        correct_answers: list,
    ):

        total = len(correct_answers)

        if total == 0:
            return {
                "correct": 0,
                "total": 0,
                "score": 0,
            }

        correct = sum(
            1
            for user_answer, correct_answer
            in zip(
                answers,
                correct_answers,
            )
            if user_answer == correct_answer
        )

        score = progress_engine.score(
            correct,
            total,
        )

        return {
            "correct": correct,
            "total": total,
            "score": score,
        }

    @staticmethod
    def save_result(
        student_id: str,
        subject: str,
        topic: str,
        answers: list,
        correct_answers: list,
        difficulty: str = "normal",
    ):

        result = QuizEngine.calculate_score(
            answers,
            correct_answers,
        )

        quiz_id = str(uuid.uuid4())

        conn = connection()

        conn.execute(
            """
            INSERT INTO quizzes
            (
                id,
                student_id,
                subject,
                topic,
                difficulty,
                answers,
                correct_answers,
                score,
                completed,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                quiz_id,
                student_id,
                subject,
                topic,
                difficulty,
                json.dumps(answers),
                json.dumps(correct_answers),
                result["score"],
                1,
                utc_now(),
            ),
        )

        conn.commit()
        conn.close()

        progress_engine.record_score(
            student_id,
            result["score"],
        )

        xp = round(
            result["score"]
            * (
                2
                if difficulty == "hard"
                else 1.5
            )
        )

        coins = max(
            1,
            round(result["score"] / 20),
        )

        progress_engine.add_xp(
            student_id,
            xp,
        )

        progress_engine.add_coins(
            student_id,
            coins,
        )

        event_engine.log(
            student_id,
            43,
            "quiz_marked",
            {
                "score": result["score"],
                "xp": xp,
                "coins": coins,
            },
        )

        return {
            "quiz_id": quiz_id,
            **result,
            "xp_earned": xp,
            "coins_earned": coins,
        }


quiz_engine = QuizEngine()


# ============================================================
# PAST QUESTION ENGINE
# ============================================================

class PastQuestionEngine:

    ALLOWED_EXAMS = {
        "WAEC",
        "NECO",
        "JAMB",
        "BECE",
    }

    @staticmethod
    def search(
        exam_type: str,
        subject: str,
        topic: str = "",
        year: Optional[int] = None,
    ):

        exam_type = exam_type.upper()

        if exam_type not in PastQuestionEngine.ALLOWED_EXAMS:
            raise ValueError(
                "Unsupported examination."
            )

        conn = connection()

        query = """
            SELECT *
            FROM questions
            WHERE exam_type=?
              AND subject=?
              AND source_type='official'
              AND authorized=1
        """

        params = [
            exam_type,
            subject,
        ]

        if topic:

            query += " AND topic=?"

            params.append(topic)

        if year:

            query += " AND year=?"

            params.append(year)

        query += " ORDER BY year DESC"

        rows = conn.execute(
            query,
            params,
        ).fetchall()

        conn.close()

        return [
            dict(row)
            for row in rows
        ]

    @staticmethod
    def add_authorized_question(
        exam_type: str,
        subject: str,
        topic: str,
        prompt: str,
        year: Optional[int] = None,
        options: Optional[list] = None,
        answer: Optional[str] = None,
        explanation: Optional[str] = None,
    ):

        exam_type = exam_type.upper()

        if exam_type not in PastQuestionEngine.ALLOWED_EXAMS:
            raise ValueError(
                "Unsupported examination."
            )

        conn = connection()

        cursor = conn.execute(
            """
            INSERT INTO questions
            (
                exam_type,
                subject,
                topic,
                year,
                source_type,
                prompt,
                options,
                answer,
                explanation,
                authorized,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                exam_type,
                subject,
                topic,
                year,
                "official",
                prompt,
                json.dumps(options or []),
                answer,
                explanation,
                1,
                utc_now(),
            ),
        )

        conn.commit()

        question_id = cursor.lastrowid

        conn.close()

        return {
            "id": question_id,
            "exam_type": exam_type,
            "source_type": "official",
            "authorized": True,
        }


past_question_engine = PastQuestionEngine()


# ============================================================
# AI-QUESTION SAFETY SEPARATION
# ============================================================

def label_question_source(source_type: str):

    source_type = source_type.lower()

    if source_type in {
        "official",
        "authorized",
    }:

        return {
            "label": "Official / Authorized",
            "is_official": True,
            "is_ai_generated": False,
        }

    if source_type in {
        "ai",
        "generated",
        "ai_generated",
    }:

        return {
            "label": "AI-Generated Practice",
            "is_official": False,
            "is_ai_generated": True,
        }

    return {
        "label": "Unknown Source",
        "is_official": False,
        "is_ai_generated": False,
    }


# ============================================================
# CLASSROOM ENGINE
# ============================================================

class ClassroomEngine:

    @staticmethod
    def create(
        student_id: str,
        subject: str,
        topic: str,
        teacher_personality: str = "standard",
    ):

        classroom_id = str(uuid.uuid4())

        conn = connection()

        conn.execute(
            """
            INSERT INTO classrooms
            (
                id,
                student_id,
                subject,
                topic,
                teacher_personality,
                status,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                classroom_id,
                student_id,
                subject,
                topic,
                teacher_personality,
                "active",
                utc_now(),
            ),
        )

        conn.commit()
        conn.close()

        return ClassroomEngine.get(
            classroom_id
        )

    @staticmethod
    def get(classroom_id: str):

        conn = connection()

        row = conn.execute(
            """
            SELECT *
            FROM classrooms
            WHERE id=?
            """,
            (classroom_id,),
        ).fetchone()

        conn.close()

        if not row:
            raise HTTPException(
                404,
                "Classroom not found.",
            )

        return dict(row)

    @staticmethod
    def ask(
        classroom_id: str,
        request: str,
    ):

        classroom = ClassroomEngine.get(
            classroom_id
        )

        student = student_engine.get(
            classroom["student_id"]
        )

        return ai_bridge.run(
            "AI Classroom",
            student,
            request,
        )


classroom_engine = ClassroomEngine()


# ============================================================
# NOTES ENGINE
# ============================================================

class NotesEngine:

    @staticmethod
    def create(
        student_id: str,
        title: str,
        body: str,
    ):

        note_id = str(uuid.uuid4())

        timestamp = utc_now()

        conn = connection()

        conn.execute(
            """
            INSERT INTO notes
            (
                id,
                student_id,
                title,
                body,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                note_id,
                student_id,
                title,
                body,
                timestamp,
                timestamp,
            ),
        )

        conn.commit()
        conn.close()

        return {
            "id": note_id,
            "student_id": student_id,
            "title": title,
            "body": body,
        }


notes_engine = NotesEngine()


# ============================================================
# GAME ENGINE
# ============================================================

class GameEngine:

    GAMES = {
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
    }

    @staticmethod
    def start(
        student_id: str,
        game: str,
        mode: str = "standard",
    ):

        if game not in GameEngine.GAMES:
            raise ValueError(
                "Unknown Learn It game."
            )

        game_id = str(uuid.uuid4())

        conn = connection()

        conn.execute(
            """
            INSERT INTO games
            (
                id,
                student_id,
                game,
                mode,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                game_id,
                student_id,
                game,
                mode,
                utc_now(),
            ),
        )

        conn.commit()
        conn.close()

        return {
            "id": game_id,
            "game": game,
            "mode": mode,
            "status": "active",
        }

    @staticmethod
    def finish(
        game_id: str,
        score: int,
    ):

        conn = connection()

        row = conn.execute(
            "SELECT * FROM games WHERE id=?",
            (game_id,),
        ).fetchone()

        if not row:
            conn.close()

            raise HTTPException(
                404,
                "Game not found.",
            )

        conn.execute(
            """
            UPDATE games
            SET score=?,
                status='completed',
                ended_at=?
            WHERE id=?
            """,
            (
                score,
                utc_now(),
                game_id,
            ),
        )

        conn.commit()
        conn.close()

        student_id = row["student_id"]

        progress_engine.add_xp(
            student_id,
            max(1, score),
        )

        return {
            "game_id": game_id,
            "score": score,
            "status": "completed",
        }


game_engine = GameEngine()


# ============================================================
# REQUEST MODELS
# ============================================================

class StudentRequest(BaseModel):

    id: str = "demo-student"

    name: str = "Student"

    grade: str = "JSS3"

    curriculum: str = "Nigerian"

    pathway: str = "General"

    subject: str = ""

    topic: str = ""

    difficulty: str = "normal"


class FeatureRequest(BaseModel):

    student_id: str = "demo-student"

    request: str = ""


class StudySessionRequest(BaseModel):

    student_id: str = "demo-student"

    subject: str = "Mathematics"

    topic: str = ""

    mode: str = "standard"

    goal: str = ""


class SessionUpdateRequest(BaseModel):

    progress: Optional[float] = None

    status: Optional[str] = None

    score: Optional[float] = None


class QuizRequest(BaseModel):

    student_id: str = "demo-student"

    subject: str = ""

    topic: str = ""

    answers: list[Any] = Field(
        default_factory=list
    )

    correct_answers: list[Any] = Field(
        default_factory=list
    )

    difficulty: str = "normal"


class ClassroomRequest(BaseModel):

    student_id: str = "demo-student"

    subject: str = "Mathematics"

    topic: str = ""

    teacher_personality: str = "standard"


class ClassroomAskRequest(BaseModel):

    request: str


class NoteRequest(BaseModel):

    student_id: str = "demo-student"

    title: str

    body: str


class GameRequest(BaseModel):

    student_id: str = "demo-student"

    game: str

    mode: str = "standard"


class GameFinishRequest(BaseModel):

    score: int = 0


# ============================================================
# API
# ============================================================

@app.get("/")
def home():

    return {
        "app": "Learn It",
        "engine": "Learn It Core Engine",
        "version": "1.0.0",
        "features": 170,
        "ai_engine_connected": AI_ENGINE_AVAILABLE,
    }


@app.get("/api/health")
def health():

    return {
        "status": "online",
        "learn_it_engine": True,
        "ai_engine_connected": AI_ENGINE_AVAILABLE,
        "total_features": 170,
    }


# ============================================================
# FEATURES
# ============================================================

@app.get("/api/features")
def all_features():

    return {
        "count": 170,
        "features": list(
            FEATURES.values()
        ),
    }


@app.get("/api/features/{feature_id}")
def get_feature(feature_id: int):

    if feature_id not in FEATURES:
        raise HTTPException(
            404,
            "Feature not found.",
        )

    return FEATURES[feature_id]


@app.post("/api/features/{feature_id}/run")
def run_feature(
    feature_id: int,
    request: FeatureRequest,
):

    return feature_router.execute(
        feature_id,
        request.student_id,
        request.request,
    )


# ============================================================
# STUDENTS
# ============================================================

@app.post("/api/students")
def create_student(
    request: StudentRequest,
):

    return student_engine.create(
        request.model_dump()
    )


@app.get("/api/students/{student_id}")
def get_student(student_id: str):

    return student_engine.get(
        student_id
    )


# ============================================================
# AI DIRECT ACCESS
# ============================================================

@app.post("/api/ai")
def direct_ai(
    request: FeatureRequest,
):

    student = student_engine.get(
        request.student_id
    )

    return {
        "result": ai_bridge.run(
            "Learn It AI",
            student,
            request.request,
        )
    }


# ============================================================
# STUDY SESSION HUB
# ============================================================

@app.post("/api/study/sessions")
def start_study_session(
    request: StudySessionRequest,
):

    student_engine.get(
        request.student_id
    )

    return study_engine.start(
        student_id=request.student_id,
        subject=request.subject,
        topic=request.topic,
        mode=request.mode,
        goal=request.goal,
    )


@app.get("/api/study/sessions/{student_id}")
def get_student_sessions(
    student_id: str,
):

    conn = connection()

    rows = conn.execute(
        """
        SELECT *
        FROM study_sessions
        WHERE student_id=?
        ORDER BY started_at DESC
        """,
        (student_id,),
    ).fetchall()

    conn.close()

    return [
        dict(row)
        for row in rows
    ]


@app.get("/api/study/session/{session_id}")
def get_study_session(
    session_id: str,
):

    return study_engine.get(
        session_id
    )


@app.patch("/api/study/session/{session_id}")
def update_study_session(
    session_id: str,
    request: SessionUpdateRequest,
):

    return study_engine.update(
        session_id,
        request.progress,
        request.status,
        request.score,
    )


# ============================================================
# AI CLASSROOM
# ============================================================

@app.post("/api/classroom")
def create_classroom(
    request: ClassroomRequest,
):

    return classroom_engine.create(
        student_id=request.student_id,
        subject=request.subject,
        topic=request.topic,
        teacher_personality=request.teacher_personality,
    )


@app.get("/api/classroom/{classroom_id}")
def get_classroom(
    classroom_id: str,
):

    return classroom_engine.get(
        classroom_id
    )


@app.post("/api/classroom/{classroom_id}/ask")
def ask_classroom(
    classroom_id: str,
    request: ClassroomAskRequest,
):

    return {
        "result": classroom_engine.ask(
            classroom_id,
            request.request,
        )
    }


# ============================================================
# QUIZ
# ============================================================

@app.post("/api/quiz/mark")
def mark_quiz(
    request: QuizRequest,
):

    return quiz_engine.save_result(
        student_id=request.student_id,
        subject=request.subject,
        topic=request.topic,
        answers=request.answers,
        correct_answers=request.correct_answers,
        difficulty=request.difficulty,
    )


# ============================================================
# PAST QUESTIONS
# ============================================================

@app.get("/api/past-questions")
def search_past_questions(
    exam_type: str,
    subject: str,
    topic: str = "",
    year: Optional[int] = None,
):

    try:

        return {
            "source": "authorized_question_database",
            "questions": past_question_engine.search(
                exam_type,
                subject,
                topic,
                year,
            ),
        }

    except ValueError as error:

        raise HTTPException(
            400,
            str(error),
        )


@app.post("/api/past-questions/label")
def question_label(
    source_type: str,
):

    return label_question_source(
        source_type
    )


# ============================================================
# NOTES
# ============================================================

@app.post("/api/notes")
def create_note(
    request: NoteRequest,
):

    return notes_engine.create(
        request.student_id,
        request.title,
        request.body,
    )


# ============================================================
# GAMES
# ============================================================

@app.post("/api/games")
def start_game(
    request: GameRequest,
):

    try:

        return game_engine.start(
            request.student_id,
            request.game,
            request.mode,
        )

    except ValueError as error:

        raise HTTPException(
            400,
            str(error),
        )


@app.post("/api/games/{game_id}/finish")
def finish_game(
    game_id: str,
    request: GameFinishRequest,
):

    return game_engine.finish(
        game_id,
        request.score,
    )


# ============================================================
# PROGRESS
# ============================================================

@app.get("/api/progress/{student_id}")
def student_progress(
    student_id: str,
):

    student = student_engine.get(
        student_id
    )

    conn = connection()

    event_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE student_id=?
        """,
        (student_id,),
    ).fetchone()[0]

    completed_sessions = conn.execute(
        """
        SELECT COUNT(*)
        FROM study_sessions
        WHERE student_id=?
          AND status='completed'
        """,
        (student_id,),
    ).fetchone()[0]

    conn.close()

    return {
        "student": student,
        "xp": student["xp"],
        "coins": student["coins"],
        "level": student["level"],
        "streak": student["streak"],
        "weak_topics": student["weak_topics"],
        "strong_topics": student["strong_topics"],
        "recent_scores": student["recent_scores"],
        "events": event_count,
        "completed_study_sessions": completed_sessions,
    }


# ============================================================
# LEADERBOARD
# ============================================================

@app.get("/api/leaderboard")
def leaderboard():

    conn = connection()

    rows = conn.execute(
        """
        SELECT
            id,
            name,
            xp,
            coins,
            level,
            streak
        FROM students
        ORDER BY xp DESC
        LIMIT 100
        """
    ).fetchall()

    conn.close()

    return {
        "leaderboard": [
            dict(row)
            for row in rows
        ]
    }


# ============================================================
# AI ENGINE STATUS
# ============================================================

@app.get("/api/ai/status")
def ai_status():

    return {
        "connected": AI_ENGINE_AVAILABLE,
        "engine": "ai_engine.py",
        "message": (
            "Existing AI engine detected."
            if AI_ENGINE_AVAILABLE
            else
            "Place ai_engine.py beside this file."
        ),
    }


# ============================================================
# STARTUP MESSAGE
# ============================================================

if __name__ == "__main__":

    import uvicorn

    print("=" * 60)
    print("LEARN IT CORE ENGINE")
    print("=" * 60)
    print("170 features registered")
    print(
        "AI engine:",
        "CONNECTED"
        if AI_ENGINE_AVAILABLE
        else "NOT FOUND",
    )
    print("Database:", DATABASE)
    print("=" * 60)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
)# learn_it_engine.py
#
# LEARN IT CORE ENGINE
# ====================
# Powers the non-AI side of Learn It and connects AI features
# to the existing ai_engine.py.
#
# IMPORTANT:
# Your existing ai_engine.py must contain:
#
#     def run_ai(feature, student, request):
#         ...
#
# This engine imports it below.
#
# Run the API:
#     uvicorn learn_it_engine:app --reload
#
# Install:
#     pip install fastapi uvicorn pydantic
#
# NOTE:
# This is the core engine foundation. It deliberately keeps
# official exam questions separate from AI-generated questions.

from __future__ import annotations

import json
import sqlite3
import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# ============================================================
# EXISTING AI ENGINE
# ============================================================

try:
    from ai_engine import run_ai
    AI_ENGINE_AVAILABLE = True
except ImportError:
    AI_ENGINE_AVAILABLE = False

    def run_ai(feature, student, request):
        raise RuntimeError(
            "ai_engine.py was not found. "
            "Place your existing ai_engine.py beside learn_it_engine.py."
        )


# ============================================================
# APPLICATION
# ============================================================

app = FastAPI(
    title="Learn It Core Engine",
    description="Core engine powering all 170 Learn It features.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# DATABASE
# ============================================================

DATABASE = "learn_it.db"


def connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def initialize_database():

    conn = connection()

    conn.executescript(
        """

        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            grade TEXT DEFAULT 'JSS3',
            curriculum TEXT DEFAULT 'Nigerian',
            pathway TEXT DEFAULT 'General',
            subject TEXT DEFAULT '',
            topic TEXT DEFAULT '',
            difficulty TEXT DEFAULT 'normal',

            xp INTEGER DEFAULT 0,
            coins INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            streak INTEGER DEFAULT 0,

            weak_topics TEXT DEFAULT '[]',
            strong_topics TEXT DEFAULT '[]',
            recent_scores TEXT DEFAULT '[]',

            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS study_sessions (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            subject TEXT,
            topic TEXT,
            mode TEXT,

            goal TEXT,
            status TEXT DEFAULT 'active',

            progress REAL DEFAULT 0,
            score REAL DEFAULT 0,

            started_at TEXT NOT NULL,
            ended_at TEXT
        );

        CREATE TABLE IF NOT EXISTS classrooms (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            subject TEXT,
            topic TEXT,

            teacher_personality TEXT DEFAULT 'standard',

            status TEXT DEFAULT 'active',

            created_at TEXT NOT NULL,
            ended_at TEXT
        );

        CREATE TABLE IF NOT EXISTS quizzes (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            subject TEXT,
            topic TEXT,
            difficulty TEXT,

            questions TEXT DEFAULT '[]',
            answers TEXT DEFAULT '[]',
            correct_answers TEXT DEFAULT '[]',

            score REAL DEFAULT 0,
            completed INTEGER DEFAULT 0,

            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS exams (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            exam_type TEXT,
            subject TEXT,
            year INTEGER,

            questions TEXT DEFAULT '[]',
            answers TEXT DEFAULT '[]',

            score REAL DEFAULT 0,
            status TEXT DEFAULT 'created',

            created_at TEXT NOT NULL,
            completed_at TEXT
        );

        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            exam_type TEXT NOT NULL,
            subject TEXT NOT NULL,
            topic TEXT,

            year INTEGER,

            source_type TEXT NOT NULL,

            prompt TEXT NOT NULL,
            options TEXT DEFAULT '[]',
            answer TEXT,
            explanation TEXT,

            authorized INTEGER DEFAULT 0,

            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS notes (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            title TEXT,
            body TEXT,

            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS flashcards (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            subject TEXT,
            topic TEXT,

            front TEXT,
            back TEXT,

            difficulty TEXT DEFAULT 'normal',
            confidence INTEGER DEFAULT 0,

            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_id TEXT,
            feature_id INTEGER,
            event TEXT,

            payload TEXT DEFAULT '{}',

            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS achievements (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            name TEXT,
            description TEXT,

            unlocked_at TEXT
        );

        CREATE TABLE IF NOT EXISTS games (
            id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,

            game TEXT,
            mode TEXT,

            score INTEGER DEFAULT 0,
            opponent TEXT,

            status TEXT DEFAULT 'active',

            created_at TEXT NOT NULL,
            ended_at TEXT
        );

        """
    )

    conn.commit()
    conn.close()


initialize_database()


# ============================================================
# 170 FEATURE REGISTRY
# ============================================================

FEATURE_NAMES = [
    # 1-15 AI CORE
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

    # 16-30 AI LEARNING
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

    # 31-40 AI NOTES
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

    # 41-50 AI QUIZ
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

    # 51-55 AI FLASHCARDS
    "AI Flashcard Generator",
    "AI Adaptive Flashcards",
    "AI Flashcard Difficulty System",
    "AI Flashcard Review System",
    "AI Flashcard War AI",

    # 56-65 AI GAMES
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

    # 66-70 AI PAST QUESTIONS
    "AI WAEC Question Coach",
    "AI NECO Question Coach",
    "AI JAMB Question Coach",
    "AI BECE Question Coach",
    "AI Past-Question Analyzer",

    # 71-80 ADDITIONAL AI
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

    # 81-95 AI CLASSROOM
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

    # 96-115 STUDY SESSION HUB
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

    # 116-130 STUDY SYSTEM
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

    # 131-145 EXAMS
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

    # 146-155 GAMES
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

    # 156-170 PROGRESS / REWARDS
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


assert len(FEATURE_NAMES) == 170


# ============================================================
# FEATURE CLASSIFICATION
# ============================================================

AI_FEATURE_IDS = set(range(1, 96))

HYBRID_FEATURE_IDS = {
    96,
    102,
    103,
    114,
}

CORE_FEATURE_IDS = (
    set(range(96, 171)) - HYBRID_FEATURE_IDS
)


def feature_info(feature_id: int):

    if feature_id < 1 or feature_id > 170:
        raise ValueError("Feature ID must be between 1 and 170.")

    if feature_id in HYBRID_FEATURE_IDS:
        mode = "hybrid"
    elif feature_id in AI_FEATURE_IDS:
        mode = "ai"
    else:
        mode = "core"

    return {
        "id": feature_id,
        "name": FEATURE_NAMES[feature_id - 1],
        "mode": mode,
        "enabled": True,
    }


FEATURES = {
    feature_id: feature_info(feature_id)
    for feature_id in range(1, 171)
}


# ============================================================
# STUDENT ENGINE
# ============================================================

class StudentEngine:

    @staticmethod
    def create(data: dict):

        student_id = data.get("id") or str(uuid.uuid4())

        timestamp = utc_now()

        conn = connection()

        conn.execute(
            """
            INSERT OR REPLACE INTO students
            (
                id,
                name,
                grade,
                curriculum,
                pathway,
                subject,
                topic,
                difficulty,
                xp,
                coins,
                level,
                streak,
                weak_topics,
                strong_topics,
                recent_scores,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                student_id,
                data.get("name", "Student"),
                data.get("grade", "JSS3"),
                data.get("curriculum", "Nigerian"),
                data.get("pathway", "General"),
                data.get("subject", ""),
                data.get("topic", ""),
                data.get("difficulty", "normal"),
                data.get("xp", 0),
                data.get("coins", 0),
                data.get("level", 1),
                data.get("streak", 0),
                json.dumps(data.get("weak_topics", [])),
                json.dumps(data.get("strong_topics", [])),
                json.dumps(data.get("recent_scores", [])),
                data.get("created_at", timestamp),
                timestamp,
            ),
        )

        conn.commit()
        conn.close()

        return StudentEngine.get(student_id)

    @staticmethod
    def get(student_id: str):

        conn = connection()

        row = conn.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()

        conn.close()

        if not row:
            return StudentEngine.create(
                {
                    "id": student_id,
                    "name": "Student",
                }
            )

        student = dict(row)

        student["weak_topics"] = json.loads(
            student.get("weak_topics") or "[]"
        )

        student["strong_topics"] = json.loads(
            student.get("strong_topics") or "[]"
        )

        student["recent_scores"] = json.loads(
            student.get("recent_scores") or "[]"
        )

        return student

    @staticmethod
    def update(student_id: str, updates: dict):

        student = StudentEngine.get(student_id)

        for key, value in updates.items():

            if key in student:
                student[key] = value

        student["updated_at"] = utc_now()

        conn = connection()

        conn.execute(
            """
            UPDATE students
            SET
                name=?,
                grade=?,
                curriculum=?,
                pathway=?,
                subject=?,
                topic=?,
                difficulty=?,
                xp=?,
                coins=?,
                level=?,
                streak=?,
                weak_topics=?,
                strong_topics=?,
                recent_scores=?,
                updated_at=?
            WHERE id=?
            """,
            (
                student["name"],
                student["grade"],
                student["curriculum"],
                student["pathway"],
                student["subject"],
                student["topic"],
                student["difficulty"],
                student["xp"],
                student["coins"],
                student["level"],
                student["streak"],
                json.dumps(student["weak_topics"]),
                json.dumps(student["strong_topics"]),
                json.dumps(student["recent_scores"]),
                student["updated_at"],
                student_id,
            ),
        )

        conn.commit()
        conn.close()

        return StudentEngine.get(student_id)


student_engine = StudentEngine()


# ============================================================
# PROGRESS ENGINE
# ============================================================

class ProgressEngine:

    @staticmethod
    def score(correct: int, total: int):

        if total <= 0:
            return 0.0

        return round(
            (correct / total) * 100,
            2,
        )

    @staticmethod
    def level_for_xp(xp: int):

        return max(
            1,
            (xp // 100) + 1,
        )

    @staticmethod
    def add_xp(
        student_id: str,
        amount: int,
    ):

        student = student_engine.get(student_id)

        student["xp"] += max(0, amount)

        student["level"] = ProgressEngine.level_for_xp(
            student["xp"]
        )

        student_engine.update(
            student_id,
            {
                "xp": student["xp"],
                "level": student["level"],
            },
        )

        return student_engine.get(student_id)

    @staticmethod
    def add_coins(
        student_id: str,
        amount: int,
    ):

        student = student_engine.get(student_id)

        student["coins"] += max(0, amount)

        student_engine.update(
            student_id,
            {
                "coins": student["coins"],
            },
        )

        return student_engine.get(student_id)

    @staticmethod
    def record_score(
        student_id: str,
        score: float,
    ):

        student = student_engine.get(student_id)

        scores = student["recent_scores"]

        scores.append(score)

        scores = scores[-30:]

        student_engine.update(
            student_id,
            {
                "recent_scores": scores,
            },
        )

        return scores


progress_engine = ProgressEngine()


# ============================================================
# EVENT ENGINE
# ============================================================

class EventEngine:

    @staticmethod
    def log(
        student_id: str,
        feature_id: int,
        event: str,
        payload: Optional[dict] = None,
    ):

        conn = connection()

        conn.execute(
            """
            INSERT INTO events
            (
                student_id,
                feature_id,
                event,
                payload,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                student_id,
                feature_id,
                event,
                json.dumps(payload or {}),
                utc_now(),
            ),
        )

        conn.commit()
        conn.close()


event_engine = EventEngine()


# ============================================================
# STUDY SESSION ENGINE
# ============================================================

class StudySessionEngine:

    @staticmethod
    def start(
        student_id: str,
        subject: str,
        topic: str = "",
        mode: str = "standard",
        goal: str = "",
    ):

        session_id = str(uuid.uuid4())

        conn = connection()

        conn.execute(
            """
            INSERT INTO study_sessions
            (
                id,
                student_id,
                subject,
                topic,
                mode,
                goal,
                status,
                progress,
                started_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                session_id,
                student_id,
                subject,
                topic,
                mode,
                goal,
                "active",
                0,
                utc_now(),
            ),
        )

        conn.commit()
        conn.close()

        event_engine.log(
            student_id,
            96,
            "study_session_started",
            {
                "session_id": session_id,
                "mode": mode,
            },
        )

        return StudySessionEngine.get(session_id)

    @staticmethod
    def get(session_id: str):

        conn = connection()

        row = conn.execute(
            """
            SELECT *
            FROM study_sessions
            WHERE id=?
            """,
            (session_id,),
        ).fetchone()

        conn.close()

        if not row:
            raise HTTPException(
                status_code=404,
                detail="Study session not found.",
            )

        return dict(row)

    @staticmethod
    def update(
        session_id: str,
        progress: Optional[float] = None,
        status: Optional[str] = None,
        score: Optional[float] = None,
    ):

        session = StudySessionEngine.get(session_id)

        if progress is not None:
            session["progress"] = max(
                0,
                min(100, progress),
            )

        if status is not None:
            session["status"] = status

        if score is not None:
            session["score"] = score

        ended_at = session["ended_at"]

        if session["status"] == "completed":
            ended_at = utc_now()

        conn = connection()

        conn.execute(
            """
            UPDATE study_sessions
            SET progress=?,
                status=?,
                score=?,
                ended_at=?
            WHERE id=?
            """,
            (
                session["progress"],
                session["status"],
                session["score"],
                ended_at,
                session_id,
            ),
        )

        conn.commit()
        conn.close()

        if session["status"] == "completed":
            ProgressEngine.add_xp(
                session["student_id"],
                25,
            )

            ProgressEngine.add_coins(
                session["student_id"],
                5,
            )

            event_engine.log(
                session["student_id"],
                115,
                "study_session_reward",
                {
                    "xp": 25,
                    "coins": 5,
                },
            )

        return StudySessionEngine.get(session_id)


study_engine = StudySessionEngine()


# ============================================================
# AI BRIDGE
# ============================================================

class AIBridge:

    @staticmethod
    def run(
        feature_name: str,
        student: dict,
        request: str,
    ):

        if not AI_ENGINE_AVAILABLE:
            raise HTTPException(
                status_code=503,
                detail=(
                    "AI engine unavailable. "
                    "Your existing ai_engine.py must be placed "
                    "beside learn_it_engine.py."
                ),
            )

        return run_ai(
            feature_name,
            student,
            request,
        )


ai_bridge = AIBridge()


# ============================================================
# AI FEATURE ROUTER
# ============================================================

class FeatureRouter:

    @staticmethod
    def execute(
        feature_id: int,
        student_id: str,
        request: str = "",
    ):

        if feature_id not in FEATURES:
            raise HTTPException(
                status_code=404,
                detail="Unknown Learn It feature.",
            )

        feature = FEATURES[feature_id]

        student = student_engine.get(
            student_id
        )

        event_engine.log(
            student_id,
            feature_id,
            "feature_started",
            {
                "feature": feature["name"],
                "request": request,
            },
        )

        # ----------------------------------------------------
        # AI
        # ----------------------------------------------------

        if feature["mode"] == "ai":

            result = ai_bridge.run(
                feature["name"],
                student,
                request,
            )

            event_engine.log(
                student_id,
                feature_id,
                "ai_feature_completed",
            )

            return {
                "feature": feature,
                "type": "ai",
                "result": result,
            }

        # ----------------------------------------------------
        # HYBRID
        # ----------------------------------------------------

        if feature["mode"] == "hybrid":

            result = FeatureRouter.hybrid(
                feature_id,
                student,
                request,
            )

            return {
                "feature": feature,
                "type": "hybrid",
                "result": result,
            }

        # ----------------------------------------------------
        # CORE
        # ----------------------------------------------------

        result = FeatureRouter.core(
            feature_id,
            student,
            request,
        )

        event_engine.log(
            student_id,
            feature_id,
            "core_feature_completed",
        )

        return {
            "feature": feature,
            "type": "core",
            "result": result,
        }

    @staticmethod
    def hybrid(
        feature_id: int,
        student: dict,
        request: str,
    ):

        feature = FEATURES[feature_id]

        # Study Session Hub
        if feature_id == 96:

            return {
                "status": "ready",
                "system": "Study Session Hub",
                "available_modes": [
                    "quick",
                    "deep",
                    "quiet",
                    "tutor",
                    "classroom",
                    "past_questions",
                    "quiz",
                    "flashcards",
                    "practice",
                    "timed_exam",
                ],
            }

        # AI Tutor Session
        if feature_id == 102:

            return ai_bridge.run(
                "AI Tutor Session",
                student,
                request,
            )

        # AI Classroom Session
        if feature_id == 103:

            return ai_bridge.run(
                "AI Classroom Session",
                student,
                request,
            )

        # AI Session Recommendations
        if feature_id == 114:

            return ai_bridge.run(
                "AI Session Recommendations",
                student,
                request,
            )

        return ai_bridge.run(
            feature["name"],
            student,
            request,
        )

    @staticmethod
    def core(
        feature_id: int,
        student: dict,
        request: str,
    ):

        name = FEATURES[feature_id]["name"]

        # ---------------------------------------------
        # SESSION FEATURES
        # ---------------------------------------------

        if 97 <= feature_id <= 115:

            return {
                "feature": name,
                "status": "available",
                "student_id": student["id"],
            }

        # ---------------------------------------------
        # STUDY SYSTEM
        # ---------------------------------------------

        if 116 <= feature_id <= 130:

            return {
                "feature": name,
                "status": "available",
                "student_id": student["id"],
                "subject": student["subject"],
                "topic": student["topic"],
            }

        # ---------------------------------------------
        # EXAMS
        # ---------------------------------------------

        if 131 <= feature_id <= 145:

            return {
                "feature": name,
                "status": "available",
                "exam_system": True,
                "student_id": student["id"],
            }

        # ---------------------------------------------
        # GAMES
        # ---------------------------------------------

        if 146 <= feature_id <= 155:

            return {
                "feature": name,
                "status": "game_ready",
                "student_id": student["id"],
            }

        # ---------------------------------------------
        # PROGRESS / REWARDS
        # ---------------------------------------------

        if 156 <= feature_id <= 170:

            return {
                "feature": name,
                "status": "available",
                "xp": student["xp"],
                "coins": student["coins"],
                "level": student["level"],
                "streak": student["streak"],
            }

        return {
            "feature": name,
            "status": "available",
        }


feature_router = FeatureRouter()


# ============================================================
# QUIZ ENGINE
# ============================================================

class QuizEngine:

    @staticmethod
    def calculate_score(
        answers: list,
        correct_answers: list,
    ):

        total = len(correct_answers)

        if total == 0:
            return {
                "correct": 0,
                "total": 0,
                "score": 0,
            }

        correct = sum(
            1
            for user_answer, correct_answer
            in zip(
                answers,
                correct_answers,
            )
            if user_answer == correct_answer
        )

        score = progress_engine.score(
            correct,
            total,
        )

        return {
            "correct": correct,
            "total": total,
            "score": score,
        }

    @staticmethod
    def save_result(
        student_id: str,
        subject: str,
        topic: str,
        answers: list,
        correct_answers: list,
        difficulty: str = "normal",
    ):

        result = QuizEngine.calculate_score(
            answers,
            correct_answers,
        )

        quiz_id = str(uuid.uuid4())

        conn = connection()

        conn.execute(
            """
            INSERT INTO quizzes
            (
                id,
                student_id,
                subject,
                topic,
                difficulty,
                answers,
                correct_answers,
                score,
                completed,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                quiz_id,
                student_id,
                subject,
                topic,
                difficulty,
                json.dumps(answers),
                json.dumps(correct_answers),
                result["score"],
                1,
                utc_now(),
            ),
        )

        conn.commit()
        conn.close()

        progress_engine.record_score(
            student_id,
            result["score"],
        )

        xp = round(
            result["score"]
            * (
                2
                if difficulty == "hard"
                else 1.5
            )
        )

        coins = max(
            1,
            round(result["score"] / 20),
        )

        progress_engine.add_xp(
            student_id,
            xp,
        )

        progress_engine.add_coins(
            student_id,
            coins,
        )

        event_engine.log(
            student_id,
            43,
            "quiz_marked",
            {
                "score": result["score"],
                "xp": xp,
                "coins": coins,
            },
        )

        return {
            "quiz_id": quiz_id,
            **result,
            "xp_earned": xp,
            "coins_earned": coins,
        }


quiz_engine = QuizEngine()


# ============================================================
# PAST QUESTION ENGINE
# ============================================================

class PastQuestionEngine:

    ALLOWED_EXAMS = {
        "WAEC",
        "NECO",
        "JAMB",
        "BECE",
    }

    @staticmethod
    def search(
        exam_type: str,
        subject: str,
        topic: str = "",
        year: Optional[int] = None,
    ):

        exam_type = exam_type.upper()

        if exam_type not in PastQuestionEngine.ALLOWED_EXAMS:
            raise ValueError(
                "Unsupported examination."
            )

        conn = connection()

        query = """
            SELECT *
            FROM questions
            WHERE exam_type=?
              AND subject=?
              AND source_type='official'
              AND authorized=1
        """

        params = [
            exam_type,
            subject,
        ]

        if topic:

            query += " AND topic=?"

            params.append(topic)

        if year:

            query += " AND year=?"

            params.append(year)

        query += " ORDER BY year DESC"

        rows = conn.execute(
            query,
            params,
        ).fetchall()

        conn.close()

        return [
            dict(row)
            for row in rows
        ]

    @staticmethod
    def add_authorized_question(
        exam_type: str,
        subject: str,
        topic: str,
        prompt: str,
        year: Optional[int] = None,
        options: Optional[list] = None,
        answer: Optional[str] = None,
        explanation: Optional[str] = None,
    ):

        exam_type = exam_type.upper()

        if exam_type not in PastQuestionEngine.ALLOWED_EXAMS:
            raise ValueError(
                "Unsupported examination."
            )

        conn = connection()

        cursor = conn.execute(
            """
            INSERT INTO questions
            (
                exam_type,
                subject,
                topic,
                year,
                source_type,
                prompt,
                options,
                answer,
                explanation,
                authorized,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                exam_type,
                subject,
                topic,
                year,
                "official",
                prompt,
                json.dumps(options or []),
                answer,
                explanation,
                1,
                utc_now(),
            ),
        )

        conn.commit()

        question_id = cursor.lastrowid

        conn.close()

        return {
            "id": question_id,
            "exam_type": exam_type,
            "source_type": "official",
            "authorized": True,
        }


past_question_engine = PastQuestionEngine()


# ============================================================
# AI-QUESTION SAFETY SEPARATION
# ============================================================

def label_question_source(source_type: str):

    source_type = source_type.lower()

    if source_type in {
        "official",
        "authorized",
    }:

        return {
            "label": "Official / Authorized",
            "is_official": True,
            "is_ai_generated": False,
        }

    if source_type in {
        "ai",
        "generated",
        "ai_generated",
    }:

        return {
            "label": "AI-Generated Practice",
            "is_official": False,
            "is_ai_generated": True,
        }

    return {
        "label": "Unknown Source",
        "is_official": False,
        "is_ai_generated": False,
    }


# ============================================================
# CLASSROOM ENGINE
# ============================================================

class ClassroomEngine:

    @staticmethod
    def create(
        student_id: str,
        subject: str,
        topic: str,
        teacher_personality: str = "standard",
    ):

        classroom_id = str(uuid.uuid4())

        conn = connection()

        conn.execute(
            """
            INSERT INTO classrooms
            (
                id,
                student_id,
                subject,
                topic,
                teacher_personality,
                status,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                classroom_id,
                student_id,
                subject,
                topic,
                teacher_personality,
                "active",
                utc_now(),
            ),
        )

        conn.commit()
        conn.close()

        return ClassroomEngine.get(
            classroom_id
        )

    @staticmethod
    def get(classroom_id: str):

        conn = connection()

        row = conn.execute(
            """
            SELECT *
            FROM classrooms
            WHERE id=?
            """,
            (classroom_id,),
        ).fetchone()

        conn.close()

        if not row:
            raise HTTPException(
                404,
                "Classroom not found.",
            )

        return dict(row)

    @staticmethod
    def ask(
        classroom_id: str,
        request: str,
    ):

        classroom = ClassroomEngine.get(
            classroom_id
        )

        student = student_engine.get(
            classroom["student_id"]
        )

        return ai_bridge.run(
            "AI Classroom",
            student,
            request,
        )


classroom_engine = ClassroomEngine()


# ============================================================
# NOTES ENGINE
# ============================================================

class NotesEngine:

    @staticmethod
    def create(
        student_id: str,
        title: str,
        body: str,
    ):

        note_id = str(uuid.uuid4())

        timestamp = utc_now()

        conn = connection()

        conn.execute(
            """
            INSERT INTO notes
            (
                id,
                student_id,
                title,
                body,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                note_id,
                student_id,
                title,
                body,
                timestamp,
                timestamp,
            ),
        )

        conn.commit()
        conn.close()

        return {
            "id": note_id,
            "student_id": student_id,
            "title": title,
            "body": body,
        }


notes_engine = NotesEngine()


# ============================================================
# GAME ENGINE
# ============================================================

class GameEngine:

    GAMES = {
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
    }

    @staticmethod
    def start(
        student_id: str,
        game: str,
        mode: str = "standard",
    ):

        if game not in GameEngine.GAMES:
            raise ValueError(
                "Unknown Learn It game."
            )

        game_id = str(uuid.uuid4())

        conn = connection()

        conn.execute(
            """
            INSERT INTO games
            (
                id,
                student_id,
                game,
                mode,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                game_id,
                student_id,
                game,
                mode,
                utc_now(),
            ),
        )

        conn.commit()
        conn.close()

        return {
            "id": game_id,
            "game": game,
            "mode": mode,
            "status": "active",
        }

    @staticmethod
    def finish(
        game_id: str,
        score: int,
    ):

        conn = connection()

        row = conn.execute(
            "SELECT * FROM games WHERE id=?",
            (game_id,),
        ).fetchone()

        if not row:
            conn.close()

            raise HTTPException(
                404,
                "Game not found.",
            )

        conn.execute(
            """
            UPDATE games
            SET score=?,
                status='completed',
                ended_at=?
            WHERE id=?
            """,
            (
                score,
                utc_now(),
                game_id,
            ),
        )

        conn.commit()
        conn.close()

        student_id = row["student_id"]

        progress_engine.add_xp(
            student_id,
            max(1, score),
        )

        return {
            "game_id": game_id,
            "score": score,
            "status": "completed",
        }


game_engine = GameEngine()


# ============================================================
# REQUEST MODELS
# ============================================================

class StudentRequest(BaseModel):

    id: str = "demo-student"

    name: str = "Student"

    grade: str = "JSS3"

    curriculum: str = "Nigerian"

    pathway: str = "General"

    subject: str = ""

    topic: str = ""

    difficulty: str = "normal"


class FeatureRequest(BaseModel):

    student_id: str = "demo-student"

    request: str = ""


class StudySessionRequest(BaseModel):

    student_id: str = "demo-student"

    subject: str = "Mathematics"

    topic: str = ""

    mode: str = "standard"

    goal: str = ""


class SessionUpdateRequest(BaseModel):

    progress: Optional[float] = None

    status: Optional[str] = None

    score: Optional[float] = None


class QuizRequest(BaseModel):

    student_id: str = "demo-student"

    subject: str = ""

    topic: str = ""

    answers: list[Any] = Field(
        default_factory=list
    )

    correct_answers: list[Any] = Field(
        default_factory=list
    )

    difficulty: str = "normal"


class ClassroomRequest(BaseModel):

    student_id: str = "demo-student"

    subject: str = "Mathematics"

    topic: str = ""

    teacher_personality: str = "standard"


class ClassroomAskRequest(BaseModel):

    request: str


class NoteRequest(BaseModel):

    student_id: str = "demo-student"

    title: str

    body: str


class GameRequest(BaseModel):

    student_id: str = "demo-student"

    game: str

    mode: str = "standard"


class GameFinishRequest(BaseModel):

    score: int = 0


# ============================================================
# API
# ============================================================

@app.get("/")
def home():

    return {
        "app": "Learn It",
        "engine": "Learn It Core Engine",
        "version": "1.0.0",
        "features": 170,
        "ai_engine_connected": AI_ENGINE_AVAILABLE,
    }


@app.get("/api/health")
def health():

    return {
        "status": "online",
        "learn_it_engine": True,
        "ai_engine_connected": AI_ENGINE_AVAILABLE,
        "total_features": 170,
    }


# ============================================================
# FEATURES
# ============================================================

@app.get("/api/features")
def all_features():

    return {
        "count": 170,
        "features": list(
            FEATURES.values()
        ),
    }


@app.get("/api/features/{feature_id}")
def get_feature(feature_id: int):

    if feature_id not in FEATURES:
        raise HTTPException(
            404,
            "Feature not found.",
        )

    return FEATURES[feature_id]


@app.post("/api/features/{feature_id}/run")
def run_feature(
    feature_id: int,
    request: FeatureRequest,
):

    return feature_router.execute(
        feature_id,
        request.student_id,
        request.request,
    )


# ============================================================
# STUDENTS
# ============================================================

@app.post("/api/students")
def create_student(
    request: StudentRequest,
):

    return student_engine.create(
        request.model_dump()
    )


@app.get("/api/students/{student_id}")
def get_student(student_id: str):

    return student_engine.get(
        student_id
    )


# ============================================================
# AI DIRECT ACCESS
# ============================================================

@app.post("/api/ai")
def direct_ai(
    request: FeatureRequest,
):

    student = student_engine.get(
        request.student_id
    )

    return {
        "result": ai_bridge.run(
            "Learn It AI",
            student,
            request.request,
        )
    }


# ============================================================
# STUDY SESSION HUB
# ============================================================

@app.post("/api/study/sessions")
def start_study_session(
    request: StudySessionRequest,
):

    student_engine.get(
        request.student_id
    )

    return study_engine.start(
        student_id=request.student_id,
        subject=request.subject,
        topic=request.topic,
        mode=request.mode,
        goal=request.goal,
    )


@app.get("/api/study/sessions/{student_id}")
def get_student_sessions(
    student_id: str,
):

    conn = connection()

    rows = conn.execute(
        """
        SELECT *
        FROM study_sessions
        WHERE student_id=?
        ORDER BY started_at DESC
        """,
        (student_id,),
    ).fetchall()

    conn.close()

    return [
        dict(row)
        for row in rows
    ]


@app.get("/api/study/session/{session_id}")
def get_study_session(
    session_id: str,
):

    return study_engine.get(
        session_id
    )


@app.patch("/api/study/session/{session_id}")
def update_study_session(
    session_id: str,
    request: SessionUpdateRequest,
):

    return study_engine.update(
        session_id,
        request.progress,
        request.status,
        request.score,
    )


# ============================================================
# AI CLASSROOM
# ============================================================

@app.post("/api/classroom")
def create_classroom(
    request: ClassroomRequest,
):

    return classroom_engine.create(
        student_id=request.student_id,
        subject=request.subject,
        topic=request.topic,
        teacher_personality=request.teacher_personality,
    )


@app.get("/api/classroom/{classroom_id}")
def get_classroom(
    classroom_id: str,
):

    return classroom_engine.get(
        classroom_id
    )


@app.post("/api/classroom/{classroom_id}/ask")
def ask_classroom(
    classroom_id: str,
    request: ClassroomAskRequest,
):

    return {
        "result": classroom_engine.ask(
            classroom_id,
            request.request,
        )
    }


# ============================================================
# QUIZ
# ============================================================

@app.post("/api/quiz/mark")
def mark_quiz(
    request: QuizRequest,
):

    return quiz_engine.save_result(
        student_id=request.student_id,
        subject=request.subject,
        topic=request.topic,
        answers=request.answers,
        correct_answers=request.correct_answers,
        difficulty=request.difficulty,
    )


# ============================================================
# PAST QUESTIONS
# ============================================================

@app.get("/api/past-questions")
def search_past_questions(
    exam_type: str,
    subject: str,
    topic: str = "",
    year: Optional[int] = None,
):

    try:

        return {
            "source": "authorized_question_database",
            "questions": past_question_engine.search(
                exam_type,
                subject,
                topic,
                year,
            ),
        }

    except ValueError as error:

        raise HTTPException(
            400,
            str(error),
        )


@app.post("/api/past-questions/label")
def question_label(
    source_type: str,
):

    return label_question_source(
        source_type
    )


# ============================================================
# NOTES
# ============================================================

@app.post("/api/notes")
def create_note(
    request: NoteRequest,
):

    return notes_engine.create(
        request.student_id,
        request.title,
        request.body,
    )


# ============================================================
# GAMES
# ============================================================

@app.post("/api/games")
def start_game(
    request: GameRequest,
):

    try:

        return game_engine.start(
            request.student_id,
            request.game,
            request.mode,
        )

    except ValueError as error:

        raise HTTPException(
            400,
            str(error),
        )


@app.post("/api/games/{game_id}/finish")
def finish_game(
    game_id: str,
    request: GameFinishRequest,
):

    return game_engine.finish(
        game_id,
        request.score,
    )


# ============================================================
# PROGRESS
# ============================================================

@app.get("/api/progress/{student_id}")
def student_progress(
    student_id: str,
):

    student = student_engine.get(
        student_id
    )

    conn = connection()

    event_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE student_id=?
        """,
        (student_id,),
    ).fetchone()[0]

    completed_sessions = conn.execute(
        """
        SELECT COUNT(*)
        FROM study_sessions
        WHERE student_id=?
          AND status='completed'
        """,
        (student_id,),
    ).fetchone()[0]

    conn.close()

    return {
        "student": student,
        "xp": student["xp"],
        "coins": student["coins"],
        "level": student["level"],
        "streak": student["streak"],
        "weak_topics": student["weak_topics"],
        "strong_topics": student["strong_topics"],
        "recent_scores": student["recent_scores"],
        "events": event_count,
        "completed_study_sessions": completed_sessions,
    }


# ============================================================
# LEADERBOARD
# ============================================================

@app.get("/api/leaderboard")
def leaderboard():

    conn = connection()

    rows = conn.execute(
        """
        SELECT
            id,
            name,
            xp,
            coins,
            level,
            streak
        FROM students
        ORDER BY xp DESC
        LIMIT 100
        """
    ).fetchall()

    conn.close()

    return {
        "leaderboard": [
            dict(row)
            for row in rows
        ]
    }


# ============================================================
# AI ENGINE STATUS
# ============================================================

@app.get("/api/ai/status")
def ai_status():

    return {
        "connected": AI_ENGINE_AVAILABLE,
        "engine": "ai_engine.py",
        "message": (
            "Existing AI engine detected."
            if AI_ENGINE_AVAILABLE
            else
            "Place ai_engine.py beside this file."
        ),
    }


# ============================================================
# STARTUP MESSAGE
# ============================================================

if __name__ == "__main__":

    import uvicorn

    print("=" * 60)
    print("LEARN IT CORE ENGINE")
    print("=" * 60)
    print("170 features registered")
    print(
        "AI engine:",
        "CONNECTED"
        if AI_ENGINE_AVAILABLE
        else "NOT FOUND",
    )
    print("Database:", DATABASE)
    print("=" * 60)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
)
