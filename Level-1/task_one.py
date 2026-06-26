"""Task 1"""

from datetime import date


class Trainee:
    """Creates trainee object."""

    def __init__(self, name: str, email: str, date_of_birth: date, assessments: list[Assessment]):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = assessments
        if self.assessments is None:
            self.assessments = []

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
