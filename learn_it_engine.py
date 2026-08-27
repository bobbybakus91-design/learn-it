"""
Learn It — Core Engine Module (Capabilities 96-170)
Handles session management, non-AI platform mechanisms, gamification, and exam records.
"""

import time
import uuid
from typing import Dict, List, Any, Optional

class LearnItEngine:
    def __init__(self):
        # In-Memory Datastores (Production systems replace this with DB connections)
        self.students: Dict[str, Dict[str, Any]] = {}
        self.study_sessions: Dict[str, Dict[str, Any]] = {}
        self.official_past_questions_db: List[Dict[str, Any]] = self._seed_official_questions()
        
    def _seed_official_questions(self) -> List[Dict[str, Any]]:
        """Populates authentic past question database (Capabilities 131-136, 138)."""
        return [
            {
                "id": "WAEC-2022-MATH-Q01",
                "exam_category": "WAEC",
                "year": 2022,
                "subject": "Mathematics",
                "topic": "Algebra",
                "question_text": "If 3p + 2q = 12 and p - q = 1, find the value of p.",
                "options": ["A) 2", "B) 2.8", "C) 3", "D) 4"],
                "correct_option": "B) 2.8",
                "is_official": True,
                "label": "OFFICIAL WAEC PAST QUESTION",
                "disclaimer": "OFFICIAL QUESTION: Sourced from West African Examinations Council past paper archive."
            },
            {
                "id": "JAMB-2023-ENG-Q14",
                "exam_category": "JAMB",
                "year": 2023,
                "subject": "English Language",
                "topic": "Antonyms",
                "question_text": "Select the option opposite in meaning to 'ephemeral'.",
                "options": ["A) Transient", "B) Perpetual", "C) Fragile", "D) Elusive"],
                "correct_option": "B) Perpetual",
                "is_official": True,
                "label": "OFFICIAL JAMB PAST QUESTION",
                "disclaimer": "OFFICIAL QUESTION: Sourced from Joint Admissions and Matriculation Board archives."
            }
        ]

    # --- Student Profile Management ---
    def get_or_create_student(self, student_id: str, name: str = "Learner") -> Dict[str, Any]:
        if student_id not in self.students:
            self.students[student_id] = {
                "id": student_id,
                "name": name,
                "grade": "SS2",
                "curriculum": "Nigerian National Curriculum",
                "xp": 0,
                "coins": 50,
                "level": 1,
                "streak_days": 1,
                "avatar": "default_scholar",
                "saved_questions": [],
                "mistake_notebook": [],
                "personal_notes": [],
                "mastery_matrix": {},
                "achievements": []
            }
        return self.students[student_id]

    # --- 96-115: Study Session Hub ---
    def start_study_session(self, student_id: str, session_type: str, subject: str, topic: str, goal_minutes: int = 25) -> Dict[str, Any]:
        session_id = f"sess_{uuid.uuid4().hex[:8]}"
        session_data = {
            "session_id": session_id,
            "student_id": student_id,
            "session_type": session_type, # Quick, Deep, Quiet, AI Tutor, AI Classroom, Timed Exam
            "subject": subject,
            "topic": topic,
            "start_time": time.time(),
            "goal_minutes": goal_minutes,
            "status": "ACTIVE",
            "logs": [],
            "performance_score": 0.0
        }
        self.study_sessions[session_id] = session_data
        return session_data

    def end_study_session(self, session_id: str, performance_score: float = 0.8) -> Dict[str, Any]:
        session = self.study_sessions.get(session_id)
        if not session:
            raise ValueError("Session ID not found.")
        
        session["status"] = "COMPLETED"
        session["end_time"] = time.time()
        session["duration_seconds"] = int(session["end_time"] - session["start_time"])
        session["performance_score"] = performance_score
        
        # --- 156-170: Progress & Gamification Rewards Processing ---
        student = self.students[session["student_id"]]
        earned_xp = int((session["duration_seconds"] / 60) * 10 * performance_score) + 50
        earned_coins = int(earned_xp / 5)
        
        student["xp"] += earned_xp
        student["coins"] += earned_coins
        student["level"] = 1 + (student["xp"] // 500)
        
        return {
            "session_summary": session,
            "rewards": {
                "earned_xp": earned_xp,
                "earned_coins": earned_coins,
                "total_xp": student["xp"],
                "total_coins": student["coins"],
                "current_level": student["level"]
            }
        }

    # --- 131-145: Official Exam System ---
    def get_official_past_questions(self, exam_category: str, subject: str) -> List[Dict[str, Any]]:
        """Retrieves verified official questions, strictly marked as non-AI."""
        return [
            q for q in self.official_past_questions_db 
            if q["exam_category"].upper() == exam_category.upper() and q["subject"].lower() == subject.lower()
        ]

    # --- 146-155: Games & Battles Arena ---
    def record_game_battle(self, student_id: str, game_mode: str, score: int, opponent: str = "AI_Opponent") -> Dict[str, Any]:
        student = self.get_or_create_student(student_id)
        xp_gained = score * 2
        student["xp"] += xp_gained
        return {
            "game_mode": game_mode,
            "score": score,
            "opponent": opponent,
            "xp_reward": xp_gained,
            "status": "VICTORY" if score > 50 else "DEFEAT"
                            }    run_ai,
    ai_engine_status,
    health_check as ai_health_check,
)


# ============================================================
# ENGINE CONFIGURATION
# ============================================================

ENGINE_NAME = "Learn It Core Engine"
ENGINE_VERSION = "1.0.0"

TOTAL_FEATURES = 170


# ============================================================
# PLATFORM FEATURE GROUPS
# ============================================================

PLATFORM_FEATURES = {
    # 96-115 — Study Session Hub
    96: "Study Session Hub",
    97: "Start Study Session",
    98: "Continue Session",
    99: "Quick Study",
    100: "Deep Study",
    101: "Quiet Study",
    102: "AI Tutor Session",
    103: "AI Classroom Session",
    104: "Past-Question Session",
    105: "Quiz Session",
    106: "Flashcard Session",
    107: "Practice Session",
    108: "Timed Exam Session",
    109: "Session Timer",
    110: "Session Goals",
    111: "Session Progress",
    112: "Session Summary",
    113: "Session Performance",
    114: "AI Session Recommendations",
    115: "XP/Rewards After Session",

    # 116-130 — Learn It Study System
    116: "Subject Dashboard",
    117: "Topic Explorer",
    118: "Lesson Viewer",
    119: "Learning Materials",
    120: "Saved Questions",
    121: "Mistake Notebook",
    122: "Personal Notes",
    123: "Gaming Notes",
    124: "Study Timetable",
    125: "Study Reminders",
    126: "Daily Study Goals",
    127: "Study Streaks",
    128: "Exam Countdown",
    129: "Revision Mode",
    130: "Exam Mode",

    # 131-145 — Exam System
    131: "WAEC",
    132: "NECO",
    133: "JAMB",
    134: "BECE",
    135: "Past-Question Database",
    136: "Authorized Question Database",
    137: "AI-Generated Practice Questions",
    138: "Official-vs-AI Question Label",
    139: "Timed Exams",
    140: "Mock Exams",
    141: "Automatic Marking",
    142: "Detailed Explanations",
    143: "Exam Results",
    144: "Exam Performance Analytics",
    145: "Weak-Topic Recommendations",

    # 146-155 — Games & Battles
    146: "Math Death Match",
    147: "English Speed",
    148: "Science Catastrophe",
    149: "Flashcard War",
    150: "STEM Competitions",
    151: "Art Merge",
    152: "Business Badge",
    153: "Battle Arena",
    154: "Challenge Mode",
    155: "Competition Rooms",

    # 156-170 — Progress & Rewards
    156: "XP",
    157: "Coins",
    158: "Levels",
    159: "Avatars",
    160: "Avatar Upgrades",
    161: "Achievements",
    162: "Badges",
    163: "Rewards",
    164: "Leaderboard",
    165: "Performance Ranking",
    166: "Daily Challenges",
    167: "Streak Rewards",
    168: "Subject Statistics",
    169: "Topic Mastery",
    170: "Overall Progress Dashboard",
}


# ============================================================
# SUBJECTS
# ============================================================

DEFAULT_SUBJECTS = [
    "Mathematics",
    "English",
    "Biology",
    "Chemistry",
    "Physics",
    "Geography",
    "Computer Science",
    "Further Mathematics",
    "Technical Drawing",
    "Literature",
    "Government",
    "Civic Education",
    "Art",
    "Accounting",
    "Marketing",
    "Economics",
    "Commerce",
]


# ============================================================
# EXAM BOARDS
# ============================================================

EXAM_BOARDS = {
    "WAEC": "West African Examinations Council",
    "NECO": "National Examinations Council",
    "JAMB": "Joint Admissions and Matriculation Board",
    "BECE": "Basic Education Certificate Examination",
}


# ============================================================
# IN-MEMORY STORAGE
# ============================================================
# This is intentionally simple for the first backend version.
# A database can replace these stores later without changing
# the public engine interface.
# ============================================================

students: dict[str, dict[str, Any]] = {}
study_sessions: dict[str, dict[str, Any]] = {}
exams: dict[str, dict[str, Any]] = {}
saved_questions: dict[str, list[dict[str, Any]]] = {}
personal_notes: dict[str, list[dict[str, Any]]] = {}
mistake_notebooks: dict[str, list[dict[str, Any]]] = {}
games: dict[str, dict[str, Any]] = {}
challenges: dict[str, dict[str, Any]] = {}


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def now_iso() -> str:
    """Return the current UTC timestamp."""

    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    """Create a simple unique Learn It ID."""

    return f"{prefix}_{uuid4().hex[:12]}"


# ============================================================
# STUDENT MANAGEMENT
# ============================================================

def create_student(
    name: str = "Student",
    grade: str = "JSS3",
    curriculum: str = "Nigerian",
    pathway: str = "General",
) -> dict[str, Any]:
    """Create a Learn It student profile."""

    student_id = new_id("student")

    student = {
        "id": student_id,
        "name": name,
        "grade": grade,
        "curriculum": curriculum,
        "pathway": pathway,
        "subjects": list(DEFAULT_SUBJECTS),
        "weak_topics": [],
        "strong_topics": [],
        "recent_scores": [],
        "learning_goals": [],
        "xp": 0,
        "coins": 0,
        "level": 1,
        "streak": 0,
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }

    students[student_id] = student

    return student


def get_student(
    student_id: str,
) -> Optional[dict[str, Any]]:
    """Return a student profile."""

    return students.get(student_id)


def update_student(
    student_id: str,
    updates: dict[str, Any],
) -> dict[str, Any]:
    """Update student profile information."""

    student = students.get(student_id)

    if student is None:
        raise ValueError("Student not found.")

    protected = {
        "id",
        "created_at",
    }

    for key, value in updates.items():
        if key not in protected:
            student[key] = value

    student["updated_at"] = now_iso()

    return student


# ============================================================
# AI CONNECTION
# ============================================================

def use_ai(
    feature: str,
    student_id: Optional[str],
    request: str,
) -> dict[str, Any]:
    """Send a request from the core engine to the AI engine."""

    student = None

    if student_id:
        student = get_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

    return run_ai(
        feature=feature,
        student=student,
        request=request,
    )


# ============================================================
# STUDY SESSION HUB — 96-115
# ============================================================

def start_study_session(
    student_id: str,
    session_type: str = "Quick Study",
    subject: Optional[str] = None,
    topic: Optional[str] = None,
    goal: Optional[str] = None,
) -> dict[str, Any]:
    """Start a Learn It study session."""

    if student_id not in students:
        raise ValueError("Student not found.")

    session_id = new_id("session")

    session = {
        "id": session_id,
        "student_id": student_id,
        "type": session_type,
        "subject": subject,
        "topic": topic,
        "goal": goal,
        "status": "active",
        "started_at": now_iso(),
        "ended_at": None,
        "duration_seconds": 0,
        "progress": 0,
        "performance": None,
        "summary": None,
        "xp_earned": 0,
        "coins_earned": 0,
    }

    study_sessions[session_id] = session

    return session


def get_study_session(
    session_id: str,
) -> Optional[dict[str, Any]]:
    """Return a study session."""

    return study_sessions.get(session_id)


def update_session_progress(
    session_id: str,
    progress: int,
) -> dict[str, Any]:
    """Update study-session progress."""

    session = study_sessions.get(session_id)

    if session is None:
        raise ValueError("Study session not found.")

    session["progress"] = max(
        0,
        min(100, int(progress)),
    )

    return session


def complete_study_session(
    session_id: str,
    performance: Optional[float] = None,
    summary: Optional[str] = None,
) -> dict[str, Any]:
    """Complete a study session and award XP/coins."""

    session = study_sessions.get(session_id)

    if session is None:
        raise ValueError("Study session not found.")

    if session["status"] == "completed":
        return session

    session["status"] = "completed"
    session["ended_at"] = now_iso()
    session["progress"] = 100
    session["performance"] = performance
    session["summary"] = summary

    xp = 50
    coins = 10

    if performance is not None:
        if performance >= 80:
            xp += 30
            coins += 10
        elif performance >= 50:
            xp += 15
            coins += 5

    session["xp_earned"] = xp
    session["coins_earned"] = coins

    award_xp(
        session["student_id"],
        xp,
    )

    award_coins(
        session["student_id"],
        coins,
    )

    return session


def get_session_recommendations(
    student_id: str,
) -> dict[str, Any]:
    """Generate AI recommendations for the next study session."""

    return use_ai(
        feature="AI Session Recommendations",
        student_id=student_id,
        request=(
            "Recommend the student's next study session "
            "using their current learning context."
        ),
    )


# ============================================================
# STUDY SYSTEM — 116-130
# ============================================================

def get_subject_dashboard(
    student_id: str,
    subject: str,
) -> dict[str, Any]:
    """Return subject dashboard information."""

    student = get_student(student_id)

    if student is None:
        raise ValueError("Student not found.")

    return {
        "student_id": student_id,
        "subject": subject,
        "weak_topics": student.get("weak_topics", []),
        "strong_topics": student.get("strong_topics", []),
        "recent_scores": student.get("recent_scores", []),
        "topic_mastery": {},
        "recommended": [],
    }


def get_topic_explorer(
    student_id: str,
    subject: str,
) -> dict[str, Any]:
    """Return topic-explorer information."""

    return {
        "student_id": student_id,
        "subject": subject,
        "topics": [],
        "message": (
            "Topics can be populated from the selected curriculum."
        ),
    }


def save_question(
    student_id: str,
    question: dict[str, Any],
) -> dict[str, Any]:
    """Save a question for a student."""

    saved_questions.setdefault(
        student_id,
        [],
    ).append(question)

    return question


def get_saved_questions(
    student_id: str,
) -> list[dict[str, Any]]:
    """Return saved questions."""

    return saved_questions.get(
        student_id,
        [],
    )


def add_personal_note(
    student_id: str,
    note: str,
    subject: Optional[str] = None,
    topic: Optional[str] = None,
) -> dict[str, Any]:
    """Add a personal study note."""

    item = {
        "id": new_id("note"),
        "student_id": student_id,
        "subject": subject,
        "topic": topic,
        "note": note,
        "created_at": now_iso(),
    }

    personal_notes.setdefault(
        student_id,
        [],
    ).append(item)

    return item


def get_personal_notes(
    student_id: str,
) -> list[dict[str, Any]]:
    """Return personal notes."""

    return personal_notes.get(
        student_id,
        [],
    )


def add_mistake(
    student_id: str,
    question: str,
    answer: Optional[str] = None,
    correct_answer: Optional[str] = None,
    subject: Optional[str] = None,
    topic: Optional[str] = None,
) -> dict[str, Any]:
    """Add an item to the student's mistake notebook."""

    item = {
        "id": new_id("mistake"),
        "student_id": student_id,
        "question": question,
        "answer": answer,
        "correct_answer": correct_answer,
        "subject": subject,
        "topic": topic,
        "created_at": now_iso(),
    }

    mistake_notebooks.setdefault(
        student_id,
        [],
    ).append(item)

    return item


def get_mistakes(
    student_id: str,
) -> list[dict[str, Any]]:
    """Return the student's mistake notebook."""

    return mistake_notebooks.get(
        student_id,
        [],
    )


# ============================================================
# EXAM SYSTEM — 131-145
# ============================================================

def get_exam_boards() -> dict[str, str]:
    """Return supported examination boards."""

    return dict(EXAM_BOARDS)


def create_exam(
    student_id: str,
    exam_board: str,
    subject: str,
    mode: str = "practice",
    question_source: str = "ai_generated",
) -> dict[str, Any]:
    """Create an exam session."""

    board = exam_board.upper()

    if board not in EXAM_BOARDS:
        raise ValueError(
            f"Unsupported exam board: {exam_board}"
        )

    exam_id = new_id("exam")

    is_ai = question_source.lower() == "ai_generated"

    exam = {
        "id": exam_id,
        "student_id": student_id,
        "exam_board": board,
        "subject": subject,
        "mode": mode,
        "question_source": (
            "AI-Generated Practice"
            if is_ai
            else "Official/Authorized"
        ),
        "is_ai_generated": is_ai,
        "questions": [],
        "answers": [],
        "score": None,
        "status": "created",
        "created_at": now_iso(),
    }

    exams[exam_id] = exam

    return exam


def get_exam(
    exam_id: str,
) -> Optional[dict[str, Any]]:
    """Return an exam."""

    return exams.get(exam_id)


def add_exam_question(
    exam_id: str,
    question: dict[str, Any],
) -> dict[str, Any]:
    """Add a question to an exam."""

    exam = exams.get(exam_id)

    if exam is None:
        raise ValueError("Exam not found.")

    exam["questions"].append(question)

    return exam


def submit_exam(
    exam_id: str,
    answers: list[Any],
) -> dict[str, Any]:
    """
    Submit an exam.

    Actual marking can be expanded when the question database
    is connected.
    """

    exam = exams.get(exam_id)

    if exam is None:
        raise ValueError("Exam not found.")

    exam["answers"] = answers
    exam["status"] = "submitted"

    return exam


# ============================================================
# AI QUESTION GENERATION
# ============================================================

def generate_practice_questions(
    student_id: str,
    subject: str,
    topic: str,
    count: int = 5,
) -> dict[str, Any]:
    """
    Generate AI practice questions.

    These are explicitly labelled as AI-generated.
    """

    request = f"""
Create {count} practice questions.

Subject: {subject}
Topic: {topic}

These must be clearly AI-generated practice questions.
Do not claim they are official WAEC, NECO, JAMB, or BECE
questions.
"""

    result = use_ai(
        feature="AI Practice Generator",
        student_id=student_id,
        request=request,
    )

    result["question_source"] = "AI-Generated Practice"
    result["is_official"] = False

    return result


# ============================================================
# GAMES & BATTLES — 146-155
# ============================================================

GAME_TYPES = [
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
]


def create_game(
    student_id: str,
    game_type: str,
) -> dict[str, Any]:
    """Create a Learn It game session."""

    if game_type not in GAME_TYPES:
        raise ValueError(
            f"Unknown game type: {game_type}"
        )

    game_id = new_id("game")

    game = {
        "id": game_id,
        "student_id": student_id,
        "type": game_type,
        "status": "waiting",
        "score": 0,
        "created_at": now_iso(),
    }

    games[game_id] = game

    return game


def create_ai_challenge(
    student_id: str,
    game_type: str,
) -> dict[str, Any]:
    """Create an AI-powered challenge."""

    return use_ai(
        feature="AI Challenge Generator",
        student_id=student_id,
        request=(
            f"Create an educational challenge for "
            f"{game_type}."
        ),
    )


# ============================================================
# PROGRESS & REWARDS — 156-170
# ============================================================

def award_xp(
    student_id: str,
    amount: int,
) -> dict[str, Any]:
    """Award XP and update the student's level."""

    student = get_student(student_id)

    if student is None:
        raise ValueError("Student not found.")

    amount = max(0, int(amount))

    student["xp"] += amount

    student["level"] = (
        student["xp"] // 100
    ) + 1

    student["updated_at"] = now_iso()

    return student


def award_coins(
    student_id: str,
    amount: int,
) -> dict[str, Any]:
    """Award Learn It coins."""

    student = get_student(student_id)

    if student is None:
        raise ValueError("Student not found.")

    student["coins"] += max(
        0,
        int(amount),
    )

    student["updated_at"] = now_iso()

    return student


def get_progress_dashboard(
    student_id: str,
) -> dict[str, Any]:
    """Return the overall progress dashboard."""

    student = get_student(student_id)

    if student is None:
        raise ValueError("Student not found.")

    sessions = [
        session
        for session in study_sessions.values()
        if session["student_id"] == student_id
    ]

    completed_sessions = [
        session
        for session in sessions
        if session["status"] == "completed"
    ]

    return {
        "student": student,
        "xp": student["xp"],
        "coins": student["coins"],
        "level": student["level"],
        "streak": student["streak"],
        "study_sessions": len(sessions),
        "completed_sessions": len(
            completed_sessions
        ),
        "subject_statistics": {},
        "topic_mastery": {},
        "achievements": [],
        "badges": [],
        "rewards": [],
    }


# ============================================================
# FEATURE REGISTRY
# ============================================================

def get_all_features() -> list[dict[str, Any]]:
    """
    Return all 170 capabilities.

    AI capabilities come from ai_engine.py.
    Platform capabilities are explicitly registered here.
    """

    features = []

    for feature_id in range(1, TOTAL_FEATURES + 1):

        if feature_id in FEATURES:
            name = FEATURES[feature_id]
        elif feature_id in PLATFORM_FEATURES:
            name = PLATFORM_FEATURES[feature_id]
        else:
            name = f"Learn It Feature {feature_id}"

        features.append(
            {
                "id": feature_id,
                "name": name,
                "type": (
                    "ai"
                    if feature_id <= 95
                    else "platform"
                ),
            }
        )

    return features


def get_feature(
    feature_id: int,
) -> dict[str, Any]:
    """Return one Learn It feature."""

    if not 1 <= feature_id <= TOTAL_FEATURES:
        raise ValueError(
            f"Feature ID must be between 1 and {TOTAL_FEATURES}."
        )

    if feature_id in FEATURES:
        name = FEATURES[feature_id]
        feature_type = "ai"
    else:
        name = PLATFORM_FEATURES.get(
            feature_id,
            f"Learn It Feature {feature_id}",
        )
        feature_type = "platform"

    return {
        "id": feature_id,
        "name": name,
        "type": feature_type,
    }


# ============================================================
# ENGINE STATUS
# ============================================================

def engine_status() -> dict[str, Any]:
    """Return the complete Learn It engine status."""

    return {
        "engine": ENGINE_NAME,
        "version": ENGINE_VERSION,
        "status": "ready",
        "total_features": TOTAL_FEATURES,
        "ai_features": 95,
        "platform_features": 75,
        "ai_engine": ai_engine_status(),
    }


def health_check() -> dict[str, Any]:
    """Return a complete health check."""

    ai_status = ai_health_check()

    return {
        "healthy": bool(
            ai_status.get("healthy")
        ),
        "engine": ENGINE_NAME,
        "total_features": TOTAL_FEATURES,
        "ai_engine": ai_status,
    }


# ============================================================
# DEVELOPMENT VALIDATION
# ============================================================

def validate_engine() -> dict[str, Any]:
    """Validate the complete 170-feature architecture."""

    all_features = get_all_features()

    ids = [
        feature["id"]
        for feature in all_features
    ]

    names = [
        feature["name"]
        for feature in all_features
    ]

    return {
        "valid": (
            len(all_features) == 170
            and len(set(ids)) == 170
            and len(set(names)) == 170
        ),
        "total_features": len(all_features),
        "unique_ids": len(set(ids)),
        "unique_names": len(set(names)),
        "ai_features": len(AI_FEATURES),
        "platform_features": len(PLATFORM_FEATURES),
}    "GEMINI_MODEL",
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
