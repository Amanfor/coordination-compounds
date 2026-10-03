import json
import re
import os

concepts = [
    "werners-theory", "ligands-and-chelates", "coordination-number-geometry", 
    "iupac-nomenclature", "isomerism", "valence-bond-theory", 
    "crystal-field-theory", "stability-of-complexes", "ean-rule", 
    "metal-carbonyls", "applications"
]

def map_concept(q_text, solution):
    text = (str(q_text) + " " + str(solution)).lower()
    if "werner" in text: return "werners-theory"
    elif "iupac" in text or "name" in text: return "iupac-nomenclature"
    elif "isomer" in text or "optical" in text or "geometrical" in text or "chirality" in text: return "isomerism"
    elif "crystal field" in text or "cfse" in text or "splitting" in text or "spectrochemical" in text: return "crystal-field-theory"
    elif "carbonyl" in text or "synergic" in text or "co" in text.split(): return "metal-carbonyls"
    elif "ean" in text or "effective atomic number" in text: return "ean-rule"
    elif "stability" in text or "formation constant" in text: return "stability-of-complexes"
    elif "hybrid" in text or "vbt" in text or "magnetic moment" in text or "paramagnetic" in text or "diamagnetic" in text: return "valence-bond-theory"
    elif "application" in text or "wilkinson" in text or "cis-platin" in text or "edta" in text or "chlorophyll" in text or "vitamin" in text: return "applications"
    elif "chelate" in text or "denticity" in text or "ligand" in text: return "ligands-and-chelates"
    elif "coordination number" in text or "geometry" in text or "tetrahedral" in text or "octahedral" in text or "square planar" in text: return "coordination-number-geometry"
    else: return "ligands-and-chelates"

questions = []

try:
    with open('/home/aman/nomad-scratch/public/pyq-database.json', 'r') as f:
        data = json.load(f)
        for q in data:
            q_str = str(q).lower()
            if any(k in q_str for k in ['coordination','ligand','complex','chelate','cfse','werner','spectrochemi']):
                q_id = q.get('id', 'q' + str(len(questions)))
                concept = map_concept(q.get('question', ''), q.get('solution', ''))
                
                options = q.get('options', [])
                correct_idx = q.get('correct', None)
                if correct_idx is not None and isinstance(correct_idx, int) and 0 <= correct_idx < len(options):
                    answer = ['A', 'B', 'C', 'D'][correct_idx] if len(options) >= 4 else str(correct_idx)
                else:
                    answer = str(q.get('answer', ''))
                
                difficulty = "JEE-Main" if "Main" in q.get('source', '') or "AIEEE" in q.get('source', '') else "JEE-Advanced"
                
                formatted_q = {
                    "id": q_id,
                    "concept": concept,
                    "type": "MCQ" if options else "numerical",
                    "difficulty": difficulty,
                    "question": q.get('question', ''),
                    "options": options if options else None,
                    "answer": answer,
                    "solution": q.get('solution', ''),
                    "source": q.get('source', 'PYQ')
                }
                questions.append(formatted_q)
except Exception as e:
    print(e)

# Target ~4-5 questions per concept
concept_counts = {c: 0 for c in concepts}
selected_questions = []

for q in questions:
    c = q['concept']
    if concept_counts[c] < 5:
        selected_questions.append(q)
        concept_counts[c] += 1

# Generate synthetic questions for empty concepts
synthetic_questions = [
    {
        "id": "syn001",
        "concept": "ean-rule",
        "type": "MCQ",
        "difficulty": "JEE-Main",
        "question": "What is the Effective Atomic Number (EAN) of Co in $[Co(NH_3)_6]^{3+}$? (Atomic number of Co = 27)",
        "options": ["36", "33", "35", "34"],
        "answer": "A",
        "solution": "1. Oxidation state of Co is +3.\n2. Number of electrons in $Co^{3+}$ = 27 - 3 = 24.\n3. Each $NH_3$ ligand donates 2 electrons. 6 $NH_3$ donate 12 electrons.\n4. EAN = $24 + 12 = 36$.\n5. Option A is correct.",
        "source": "Practice"
    },
    {
        "id": "syn002",
        "concept": "stability-of-complexes",
        "type": "MCQ",
        "difficulty": "JEE-Main",
        "question": "Which of the following complexes is most stable?",
        "options": ["$[Fe(H_2O)_6]^{3+}$", "$[Fe(NH_3)_6]^{3+}$", "$[Fe(C_2O_4)_3]^{3-}$", "$[FeCl_6]^{3-}$"],
        "answer": "C",
        "solution": "1. Stability of a complex increases with chelation.\n2. $C_2O_4^{2-}$ (oxalate) is a bidentate chelating ligand.\n3. It forms stable 5-membered rings with the central metal ion.\n4. The other ligands ($H_2O$, $NH_3$, $Cl^-$) are monodentate and do not form chelate rings.\n5. Therefore, $[Fe(C_2O_4)_3]^{3-}$ is the most stable complex.",
        "source": "Practice"
    },
    {
        "id": "syn003",
        "concept": "werners-theory",
        "type": "MCQ",
        "difficulty": "JEE-Main",
        "question": "According to Werner's theory, the primary valency and secondary valency of central metal ion in $[Co(NH_3)_5Cl]Cl_2$ respectively are:",
        "options": ["3 and 6", "2 and 6", "3 and 5", "2 and 5"],
        "answer": "A",
        "solution": "1. Primary valency corresponds to the oxidation state of the metal ion, which is ionizable.\n2. Secondary valency corresponds to the coordination number, which is non-ionizable.\n3. In $[Co(NH_3)_5Cl]Cl_2$, the oxidation state of Co is +3 (primary valency = 3).\n4. The number of ligands coordinating to Co inside the sphere is $5 (NH_3) + 1 (Cl^-) = 6$ (secondary valency = 6).\n5. Option A is correct.",
        "source": "Practice"
    }
]

for q in synthetic_questions:
    c = q['concept']
    if concept_counts[c] < 5:
        selected_questions.append(q)
        concept_counts[c] += 1

out_dir = '/home/aman/coordination-compounds/site/src/data'
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, 'questions.json'), 'w') as f:
    json.dump(selected_questions, f, indent=2)

print(f"Agent 3 done: {len(selected_questions)} questions written.")
for c in concepts:
    print(f"{c}: {concept_counts[c]}")
