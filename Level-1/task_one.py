from datetime import date


class Trainee:
    """Creates trainee object."""
    def __init__(self, name: str, email: str, date_of_birth: date, assessments: list[Assessment]):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = assessments
    
    def get_age(self) -> int:
        """Returns trainee age in years."""
        birth_date = date.strptime(self.date_of_birth, "%d/%m/%Y")
        age = date.today().year - birth_date.year

        if date.today().month < birth_date.month:
            age -= 1

        elif date.today().month < birth_date.month:
            if date.today().day < birth_date.day:
                age -= 1

        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """Adds an 'Assessment' to the trainee's list of assessments."""
        self.assessments.append(self.assessment)



    def get_assessment(self, name: str) -> Assessment | None:
        """Returns 'Assessment' object that has name given."""
        for assessment in self.assessments:
            if self.name == assessment.name:
                return assessment
        return None



class Assessment:
    """Creates assessment object."""
    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type

        if self.type.lower() not in ["multiple-choice", "technical", "presentation"]:
            raise ValueError("Must be of type multiple-choice, technical, or presentation.")
        
        if self.score not in range(0, 100):
            raise ValueError("Score must be between 0 and 100.")





if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
