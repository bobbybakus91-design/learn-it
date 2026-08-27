# ============================================================
# LEARN IT — MAIN API
# ============================================================

from __future__ import annotations

from typing import Any, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

import learn_it_engine


# ============================================================
# APP
# ============================================================

app = FastAPI(
    title="Learn It API",
    description="Learn It educational platform API",
    version="1.0.0",
)


# ============================================================
# REQUEST MODELS
# ============================================================

class StudentCreate(BaseModel):
    name: str = "Student"
    grade: str = "JSS3"
    curriculum: str = "Nigerian"
    pathway: str = "General"


class StudentUpdate(BaseModel):
    updates: dict[str, Any]


class AIRequest(BaseModel):
    feature: str
    student_id: Optional[str] = None
    request: str


class StudySessionCreate(BaseModel):
    student_id: str
    session_type: str = "Quick Study"
    subject: Optional[str] = None
    topic: Optional[str] = None
    goal: Optional[str] = None


class SessionProgress(BaseModel):
    progress: int = Field(ge=0, le=100)


class SessionComplete(BaseModel):
    performance: Optional[float] = Field(
        default=None,
        ge=0,
        le=100,
    )
    summary: Optional[str] = None


class NoteCreate(BaseModel):
    student_id: str
    note: str
    subject: Optional[str] = None
    topic: Optional[str] = None


class SaveQuestionRequest(BaseModel):
    student_id: str
    question: dict[str, Any]


class MistakeCreate(BaseModel):
    student_id: str
    question: str
    answer: Optional[str] = None
    correct_answer: Optional[str] = None
    subject: Optional[str] = None
    topic: Optional[str] = None


class ExamCreate(BaseModel):
    student_id: str
    exam_board: str
    subject: str
    mode: str = "practice"
    question_source: str = "ai_generated"


class ExamQuestionRequest(BaseModel):
    question: dict[str, Any]


class ExamSubmit(BaseModel):
    answers: list[Any]


class PracticeQuestionRequest(BaseModel):
    student_id: str
    subject: str
    topic: str
    count: int = Field(
        default=5,
        ge=1,
        le=50,
    )


class GameCreate(BaseModel):
    student_id: str
    game_type: str


class ChallengeCreate(BaseModel):
    student_id: str
    game_type: str


class RewardRequest(BaseModel):
    student_id: str
    amount: int = Field(ge=0)


# ============================================================
# BASIC ROUTES
# ============================================================

@app.get("/")
def root():
    return {
        "name": "Learn It",
        "message": "Learn It API is running.",
        "version": "1.0.0",
        "total_features": 170,
    }


@app.get("/health")
def health():
    return learn_it_engine.health_check()


@app.get("/status")
def status():
    return learn_it_engine.engine_status()


# ============================================================
# FEATURE SYSTEM
# ============================================================

@app.get("/features")
def get_features():
    return {
        "total": 170,
        "features": learn_it_engine.get_all_features(),
    }


@app.get("/features/{feature_id}")
def get_feature(feature_id: int):
    try:
        return learn_it_engine.get_feature(
            feature_id
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@app.get("/features/validate")
def validate_features():
    return learn_it_engine.validate_engine()


# ============================================================
# AI SYSTEM
# ============================================================

@app.post("/ai/run")
def run_ai(data: AIRequest):
    try:
        return learn_it_engine.use_ai(
            feature=data.feature,
            student_id=data.student_id,
            request=data.request,
        )
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


# ============================================================
# STUDENTS
# ============================================================

@app.post("/students")
def create_student(data: StudentCreate):
    return learn_it_engine.create_student(
        name=data.name,
        grade=data.grade,
        curriculum=data.curriculum,
        pathway=data.pathway,
    )


@app.get("/students/{student_id}")
def get_student(student_id: str):
    student = learn_it_engine.get_student(
        student_id
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found.",
        )

    return student


@app.patch("/students/{student_id}")
def update_student(
    student_id: str,
    data: StudentUpdate,
):
    try:
        return learn_it_engine.update_student(
            student_id,
            data.updates,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


# ============================================================
# STUDY SESSION HUB — 96-115
# ============================================================

@app.post("/study/sessions")
def start_session(
    data: StudySessionCreate,
):
    try:
        return learn_it_engine.start_study_session(
            student_id=data.student_id,
            session_type=data.session_type,
            subject=data.subject,
            topic=data.topic,
            goal=data.goal,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@app.get("/study/sessions/{session_id}")
def get_session(session_id: str):
    session = learn_it_engine.get_study_session(
        session_id
    )

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Study session not found.",
        )

    return session


@app.patch("/study/sessions/{session_id}/progress")
def update_session(
    session_id: str,
    data: SessionProgress,
):
    try:
        return learn_it_engine.update_session_progress(
            session_id,
            data.progress,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@app.post("/study/sessions/{session_id}/complete")
def complete_session(
    session_id: str,
    data: SessionComplete,
):
    try:
        return learn_it_engine.complete_study_session(
            session_id,
            performance=data.performance,
            summary=data.summary,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@app.get(
    "/study/sessions/{student_id}/recommendations"
)
def session_recommendations(
    student_id: str,
):
    try:
        return learn_it_engine.get_session_recommendations(
            student_id
        )
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


# ============================================================
# STUDY SYSTEM — 116-130
# ============================================================

@app.get(
    "/study/subjects/{student_id}/{subject}"
)
def subject_dashboard(
    student_id: str,
    subject: str,
):
    try:
        return learn_it_engine.get_subject_dashboard(
            student_id,
            subject,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@app.get(
    "/study/topics/{student_id}/{subject}"
)
def topic_explorer(
    student_id: str,
    subject: str,
):
    try:
        return learn_it_engine.get_topic_explorer(
            student_id,
            subject,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@app.post("/study/saved-questions")
def save_question(
    data: SaveQuestionRequest,
):
    try:
        return learn_it_engine.save_question(
            data.student_id,
            data.question,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@app.get(
    "/study/saved-questions/{student_id}"
)
def saved_questions(student_id: str):
    return learn_it_engine.get_saved_questions(
        student_id
    )


@app.post("/study/notes")
def create_note(data: NoteCreate):
    try:
        return learn_it_engine.add_personal_note(
            student_id=data.student_id,
            note=data.note,
            subject=data.subject,
            topic=data.topic,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@app.get("/study/notes/{student_id}")
def get_notes(student_id: str):
    return learn_it_engine.get_personal_notes(
        student_id
    )


@app.post("/study/mistakes")
def create_mistake(data: MistakeCreate):
    try:
        return learn_it_engine.add_mistake(
            student_id=data.student_id,
            question=data.question,
            answer=data.answer,
            correct_answer=data.correct_answer,
            subject=data.subject,
            topic=data.topic,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@app.get("/study/mistakes/{student_id}")
def get_mistakes(student_id: str):
    return learn_it_engine.get_mistakes(
        student_id
    )


# ============================================================
# EXAM SYSTEM — 131-145
# ============================================================

@app.get("/exams/boards")
def exam_boards():
    return learn_it_engine.get_exam_boards()


@app.post("/exams")
def create_exam(data: ExamCreate):
    try:
        return learn_it_engine.create_exam(
            student_id=data.student_id,
            exam_board=data.exam_board,
            subject=data.subject,
            mode=data.mode,
            question_source=data.question_source,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@app.get("/exams/{exam_id}")
def get_exam(exam_id: str):
    exam = learn_it_engine.get_exam(
        exam_id
    )

    if exam is None:
        raise HTTPException(
            status_code=404,
            detail="Exam not found.",
        )

    return exam


@app.post(
    "/exams/{exam_id}/questions"
)
def add_exam_question(
    exam_id: str,
    data: ExamQuestionRequest,
):
    try:
        return learn_it_engine.add_exam_question(
            exam_id,
            data.question,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@app.post("/exams/{exam_id}/submit")
def submit_exam(
    exam_id: str,
    data: ExamSubmit,
):
    try:
        return learn_it_engine.submit_exam(
            exam_id,
            data.answers,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@app.post("/exams/practice/generate")
def generate_practice(
    data: PracticeQuestionRequest,
):
    try:
        return learn_it_engine.generate_practice_questions(
            student_id=data.student_id,
            subject=data.subject,
            topic=data.topic,
            count=data.count,
        )
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


# ============================================================
# GAMES & BATTLES — 146-155
# ============================================================

@app.get("/games/types")
def game_types():
    return {
        "games": learn_it_engine.GAME_TYPES
    }


@app.post("/games")
def create_game(data: GameCreate):
    try:
        return learn_it_engine.create_game(
            student_id=data.student_id,
            game_type=data.game_type,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@app.post("/games/challenge")
def create_challenge(
    data: ChallengeCreate,
):
    try:
        return learn_it_engine.create_ai_challenge(
            student_id=data.student_id,
            game_type=data.game_type,
        )
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


# ============================================================
# PROGRESS & REWARDS — 156-170
# ============================================================

@app.get(
    "/progress/{student_id}"
)
def progress(student_id: str):
    try:
        return learn_it_engine.get_progress_dashboard(
            student_id
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@app.post("/progress/xp")
def add_xp(data: RewardRequest):
    try:
        return learn_it_engine.award_xp(
            data.student_id,
            data.amount,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@app.post("/progress/coins")
def add_coins(data: RewardRequest):
    try:
        return learn_it_engine.award_coins(
            data.student_id,
            data.amount,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


# ============================================================
# END
# ============================================================        "status": "online",
        "message": "Learn It backend is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ============================================================
# AI ENGINE STATUS
# ============================================================

@app.get("/ai/status")
def ai_status():
    return ai_engine_status()


# ============================================================
# AI FEATURES
# ============================================================

@app.get("/ai/features")
def ai_features():
    return {
        "count": len(AI_FEATURES),
        "features": AI_FEATURES
    }


# ============================================================
# AI REQUEST
# ============================================================

@app.post("/ai")
def ai(request: AIRequest):
    return run_ai(
        feature=request.feature,
        student=request.student,
        request=request.request,
    )
