# coordination compounds opencode prompt

Paste into an opencode session. It uses parallel agents to build a visual coordination compounds site from your nomad data in a new repo and deploys it with gh.

## before you run it

- Run `gh auth status` and confirm you are logged in. The deploy step needs it.
- Let the agent run shell commands and `gh` without asking each time, or it will stall on approvals.
- Pick a strong model in opencode. This is a long task with several sub-agents.
- This prompt has no `/goal` wrapper. Paste it as the message itself.

## prompt

```
Build and deploy a standalone Coordination Compounds website, taught visually, using the coordination compounds data from my existing repo. Work autonomously until it is live. Do not stop to ask questions; make reasonable decisions and note them in the new repo's README.

AGENTS
Use sub-agents in parallel where the work is independent, then integrate and review their output yourself:
- Agent 1, content: extract and merge the source data into one clean topic list and write the explanations.
- Agent 2, simulations: build the interactive visuals.
- Agent 3, questions: prepare the practice questions and worked solutions.
- Agent 4, research and review: web research to fill gaps, then check every formula, name, and example for chemical correctness.
You are responsible for the final integration, the build, and the deploy.

SOURCE DATA
- Clone https://github.com/Amanfor/nomad (public) into a scratch folder and treat it as read-only. Do not modify it.
- Coordination compounds material to mine: src/data/context/10_Coordination_Compounds.md, relevant entries in src/data/questions.ts and public/pyq-database.json, and any coordination compound images in public/media/ (for example the crystal field splitting and isomerism diagrams).
- Merge everything into one clean, non-duplicated topic list. Fix any errors you find in names, formulas, or electron counts.

NEW REPOSITORY
- Create a new public repo named coordination-compounds (under my GitHub account) with gh repo create. Put the site in it. Do not put it inside nomad.
- Stack: Astro or plain Vite + vanilla JS/TS. Use KaTeX for math and formulas. Keep it a fully static site.

CONCEPTS TO COVER
Werner's theory; ligands, denticity, and chelates; coordination number and geometry; IUPAC nomenclature; isomerism (structural: ionisation, hydrate, linkage, coordination; stereo: geometrical and optical); valence bond theory (hybridisation, inner and outer orbital complexes, magnetic moment); crystal field theory (octahedral and tetrahedral splitting, spectrochemical series, high and low spin, CFSE, colour of complexes); stability of complexes; effective atomic number; metal carbonyls and bonding; applications and biological importance.

WEBSITE REQUIREMENTS
- Every concept is explained primarily through visuals. Text is short and supports the visual.
- Build interactive SVG/canvas visuals, for example:
  - a 3D-style rotatable viewer for geometries and for geometrical and optical isomers, including cis/trans and fac/mer
  - a d-orbital splitting diagram where the user picks the metal ion, its oxidation state, and the ligand, and the electrons fill live to show high or low spin, unpaired electrons, magnetic moment, and CFSE
  - the spectrochemical series as a draggable or sortable strip
  - a colour wheel that links absorbed colour to observed colour
  - a step-by-step IUPAC name builder
  - a Werner experiment visual showing precipitated chloride for different complexes
- Each visual shows the rule or formula it demonstrates and updates numbers live as the user interacts.
- Each concept page ends with 3 to 5 JEE-style practice questions from the repo data, with step-by-step solutions that reveal on click.
- Include a one-page cheat sheet: nomenclature rules, hybridisation and geometry table, spectrochemical series, and isomer types.
- Design: pure black background, white text, thin lines, minimal, lowercase titles, no clutter. Must work well on mobile. Fast load, no heavy dependencies.
- Navigation: a simple concept index plus search (fuzzy search is fine).

RESEARCH
- Use web search whenever the repo data is thin, ambiguous, or you need better visual explanations, intuition, or common student mistakes. Prefer authoritative sources such as NCERT, university inorganic chemistry notes, and IUPAC recommendations. Do not copy text verbatim; write it in your own words.

DEPLOY
- Add a GitHub Actions workflow (or use gh) to deploy to GitHub Pages, enable Pages through gh, and wait for the deployment to succeed.
- Verify the live URL loads and the visuals work. Fix anything broken, then redeploy.

DONE WHEN
- The live site URL responds with HTTP 200, every concept page renders its visual and its interaction without console errors, and math renders correctly.
- Finish by printing: the new repo URL, the live site URL, and a short list of the concepts covered.
```