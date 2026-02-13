from typing import List

from problem import Problem
from skill_index import SkillIndex
from user_profile import UserProfile


class Recommender:
    def __init__(self, skill_index: SkillIndex):
        self.skill_index = skill_index

    def weakest_skills(self, user: UserProfile, top_k: int = 2) -> List[str]:
        if not user.skill_scores:
            return []

        sorted_skills = sorted(
            user.skill_scores.items(), key=lambda x: x[1]
        )

        return [skill for skill, _ in sorted_skills[:top_k]]

    def recommend(self, user: UserProfile, limit: int = 3) -> List[Problem]:
        weak_skills = self.weakest_skills(user)

        recommendations = []
        seen = set()

        for skill in weak_skills:
            problems = self.skill_index.problems_for_skill(skill)
            for p in problems:
                if p.id not in seen:
                    recommendations.append(p)
                    seen.add(p.id)

                if len(recommendations) >= limit:
                    return recommendations

        return recommendations
