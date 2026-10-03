with open("site/src/pages/cheatsheet.astro", "r") as f:
    content = f.read()

hero_html = """
	<div class="hero">
		<h2 class="animate-title">cheat sheet</h2>
		<p class="subtitle animate-subtitle">Quick reference guide.</p>
	</div>
"""

import re
content = re.sub(r'<div class="hero">.*?</div>', hero_html, content, flags=re.DOTALL)

styles = """
	/* Text Entry Animations */
	.animate-title {
		opacity: 0;
		transform: translateY(20px);
		animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
		font-size: 2.8rem;
		color: #fff;
	}
	.animate-subtitle {
		opacity: 0;
		transform: translateY(20px);
		animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards;
		font-size: 1.1rem;
		margin-top: 1rem;
	}
	
	@keyframes fadeUp {
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}
	
	/* Card Enhancements */
	.concept-card {
		border: 1px solid var(--border);
		padding: 2rem;
		margin-bottom: 3rem;
		border-radius: 8px;
		background: #050505;
		transition: transform 0.3s ease, border-color 0.3s ease;
	}
	.concept-card:hover {
		transform: translateY(-4px);
		border-color: #555;
	}
"""

content = content.replace("<style>", "<style>\n" + styles)

with open("site/src/pages/cheatsheet.astro", "w") as f:
    f.write(content)
