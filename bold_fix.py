import json
import re

def bold_repl(match):
    return f"<strong>{match.group(1)}</strong>"

# Fix concepts.json
with open("site/src/data/concepts.json", "r") as f:
    concepts = json.load(f)

for c in concepts:
    if "body" in c and c["body"]:
        c["body"] = re.sub(r'\*\*(.*?)\*\*', bold_repl, c["body"])
    if "summary" in c and c["summary"]:
        c["summary"] = re.sub(r'\*\*(.*?)\*\*', bold_repl, c["summary"])

with open("site/src/data/concepts.json", "w") as f:
    json.dump(concepts, f, indent=2)

# Fix questions.json
with open("site/src/data/questions.json", "r") as f:
    questions = json.load(f)

for q in questions:
    if "solution" in q and q["solution"]:
        q["solution"] = re.sub(r'\*\*(.*?)\*\*', bold_repl, q["solution"])
    if "question" in q and q["question"]:
        q["question"] = re.sub(r'\*\*(.*?)\*\*', bold_repl, q["question"])

with open("site/src/data/questions.json", "w") as f:
    json.dump(questions, f, indent=2)
