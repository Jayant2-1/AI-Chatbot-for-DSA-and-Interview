from typing import Dict
from problem import Problem

class UserProfile:
    def __init__(self, user_id: str):
        self.user_id = user_id

        self.skill_scores: Dict[str, float] = {}
    
    def get_skill_score(self, skill: str) -> float:
        return self.skill_scores.get(skill, 0.0)
    
    def update_after_attempt(self, problem: Problem, solved: bool):
        for skill in problem.skills:
            current = self.get_skill_score(skill)

            if solved:
                new_score = min(1.0, current + 0.1)
            else:
                new_score = max(0.0, current - 0.05)

            self.skill_scores[skill] = new_score

    def summary(self) -> str:
        lines = [f"User: {self.user_id}"]
        for skill, score in self.skill_scores.items():
            lines.append(f"{skill}: {round(score, 2)}")
        return "\n".join(lines)