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
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """Creates a technical assessment object."""

    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)

    def calculate_score(self):
        return self.score


class PresentationAssessment(Assessment):
    """Creates a presentation assessment object."""

    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)

    def calculate_score(self):
        return self.score * 0.6


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
