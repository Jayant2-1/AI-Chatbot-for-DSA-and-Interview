from data_loader import DataLoader
from skill_index import SkillIndex
from user_profile import UserProfile
from recommender import Recommender

# load problems
loader = DataLoader("data/problems")
files = loader.list_files()
problems = [loader.load_problem(f) for f in files]

# build skill index
index = SkillIndex()
for p in problems:
    index.add_problem(p)

# create user
user = UserProfile("user_001")

# simulate attempts
user.update_after_attempt(problems[0], solved=False)

# build recommender
rec = Recommender(index)

print("User profile:")
print(user.summary())

print("\nRecommended problems:")
recs = rec.recommend(user)

for p in recs:
    print("-", p.summary())
