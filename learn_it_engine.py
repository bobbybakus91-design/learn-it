# learn_it_engine.py

from ai_engine import run_ai


class LearnItEngine:

    def __init__(self):
        self.name = "Learn It Core Engine"
        self.version = "1.0.0"

    # -------------------------
    # AI CONNECTION
    # -------------------------

    def ai(self, feature, student, request):
        return run_ai(
            feature=feature,
            student=student,
            request=request
        )

    # -------------------------
    # STUDY SESSIONS
    # -------------------------

    def create_study_session(
        self,
        student_id,
        subject,
        topic=None,
        mode="standard"
    ):
        return {
            "student_id": student_id,
            "subject": subject,
            "topic": topic,
            "mode": mode,
            "status": "active",
            "progress": 0
        }

    def finish_study_session(self, session):
        session["status"] = "completed"
        session["progress"] = 100
        return session

    # -------------------------
    # PROGRESS
    # -------------------------

    def calculate_score(self, correct, total):
        if total <= 0:
            return 0

        return round((correct / total) * 100, 2)

    def calculate_xp(self, score, difficulty="normal"):
        multiplier = {
            "easy": 1,
            "normal": 1.5,
            "hard": 2
        }.get(difficulty, 1.5)

        return round(score * multiplier)

    # -------------------------
    # REWARDS
    # -------------------------

    def calculate_level(self, xp):
        return max(1, (xp // 100) + 1)

    # -------------------------
    # QUIZZES
    # -------------------------

    def mark_quiz(self, answers, correct_answers):
        correct = sum(
            1 for user, correct
            in zip(answers, correct_answers)
            if user == correct
        )

        total = len(correct_answers)

        return {
            "correct": correct,
            "total": total,
            "score": self.calculate_score(correct, total)
        }

    # -------------------------
    # AI FEATURE BRIDGE
    # -------------------------

    def run_ai_feature(
        self,
        feature,
        student,
        request
    ):
        return self.ai(
            feature,
            student,
            request
        )


learn_it_engine = LearnItEngine() 
