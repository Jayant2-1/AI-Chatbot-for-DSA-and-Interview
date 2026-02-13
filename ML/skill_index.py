from collections import defaultdict
from typing import List, Dict

from problem import Problem


class SkillIndex:
    def __init__(self):
        self.index: Dict[str, List[Problem]] = defaultdict(list)

    def add_problem(self, problem: Problem):
        for skill in problem.skills:
            self.index[skill].append(problem)

    def skills(self) -> List[str]:
        return list(self.index.keys())

    def problems_for_skill(self, skill: str) -> List[Problem]:
        return self.index.get(skill, [])

    def summary(self) -> str:
        lines = []
        for skill, problems in self.index.items():
            lines.append(f"{skill}: {len(problems)} problems")
        return "\n".join(lines)
