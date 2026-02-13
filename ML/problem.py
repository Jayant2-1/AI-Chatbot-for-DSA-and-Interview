from typing import List

class Problem:
    def __init__(
        self,
        id:str,
        title:str,
        difficulty:str,
        source:str,
        skills: List[str],
        problem: str,
        expected_approach: str,
        common_mistakes: List[str],
    ):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.source = source
        self.skills = skills
        self.problem = problem
        self.expected_approach = expected_approach
        self.common_mistakes = common_mistakes

    def summary(self) -> str:
        return f"{self.title} ({self.difficulty}) - Skills: {', '.join(self.skills)}"