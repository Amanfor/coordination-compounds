import json
import markdown

with open("site/src/data/concepts.json", "r") as f:
    concepts = json.load(f)

for c in concepts:
    if "body" in c and c["body"]:
        c["body"] = markdown.markdown(c["body"])
    if "summary" in c and c["summary"]:
        c["summary"] = markdown.markdown(c["summary"]).replace("<p>", "").replace("</p>", "") # summary is usually inline

with open("site/src/data/concepts.json", "w") as f:
    json.dump(concepts, f, indent=2)

with open("site/src/data/questions.json", "r") as f:
    questions = json.load(f)

for q in questions:
    if "solution" in q and q["solution"]:
        q["solution"] = markdown.markdown(q["solution"])
    if "question" in q and q["question"]:
        q["question"] = markdown.markdown(q["question"])
    if "options" in q and q["options"]:
        q["options"] = [markdown.markdown(opt).replace("<p>", "").replace("</p>", "") for opt in q["options"]]

with open("site/src/data/questions.json", "w") as f:
    json.dump(questions, f, indent=2)
