"""Task 3"""

from datetime import date


class Trainee:
    """Creates trainee object."""

    def __init__(
            self, name: str, email: str, date_of_birth: date,
            assessments: list[Assessment]):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = assessments
        if self.assessments is None:
            self.assessments = []
        for assessment in assessments:
            if not isinstance(assessment, Assessment):
                raise TypeError("An assessment must be of type Assessment.")

    def get_age(self) -> int:
        """Returns trainee age in years."""
        age = date.today().year - self.date_of_birth.year

        if date.today().month < self.date_of_birth.month:
            age -= 1

        elif date.today().month < self.date_of_birth.month:
            if date.today().day < self.date_of_birth.day:
                age -= 1

        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """Adds an 'Assessment' to the trainee's list of assessments."""
        self.assessment = assessment
        self.assessments.append(self.assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """Returns 'Assessment' object that has name given."""
        for assessment in self.assessments:
            if name in self.assessments:
                return assessment
        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """Creates a list of assessments of the same type"""
        assessments_of_type = []
        for assessment in self.assessments:
            if assessment.type == type:
                assessments_of_type.append(assessment)


class Assessment:
    """Creates assessment object."""

    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type
        self.score = score

        if self.type.lower() not in ["multiple-choice", "technical", "presentation"]:
            raise ValueError(
                "Must be of type multiple-choice, technical, or presentation.")

        if self.score < 0 or self.score > 100:
            raise ValueError("Score must be between 0 and 100.")


class MultipleChoiceAssessment(Assessment):
    """Creates a multiple choice assessment object."""

    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self):
        """Calculates score."""
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """Creates a technical assessment object."""

    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)

    def calculate_score(self):
        """Calculates score."""
        return self.score


class PresentationAssessment(Assessment):
    """Creates a presentation assessment object."""

    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)

    def calculate_score(self):
        """Calculates score"""
        return self.score * 0.6


class Question:
    """Creates a question object."""

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    """Creates a quiz object."""

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:
    """Creates a marking object."""

    def __init__(self, quiz: Quiz) -> None:
        if not isinstance(quiz, Quiz):
            raise TypeError("quiz object must be of type Quiz.")
        self._quiz = quiz

    def mark(self) -> int:
        """Returns total score for the assessment as a percentage."""
        total_questions = len(self._quiz.questions)

        if len(self._quiz.questions) == 0:
            return 0

        correct_answers = 0
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                correct_answers += 1

        return round(correct_answers / total_questions * 100)

    def generate_assessment(self) -> Assessment:
        """Returns an instance of an 'Assessment'"""
        if self._quiz.type == "multiple-choice":
            return MultipleChoiceAssessment(self._quiz.name, self.mark())

        elif self._quiz.type == "technical":
            return TechnicalAssessment(self._quiz.name, self.mark())

        return PresentationAssessment(self._quiz.name, self.mark())
