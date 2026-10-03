with open("site/src/layouts/Layout.astro", "r") as f:
    content = f.read()

# Add scrollbar css
scroll_css = """
	/* Custom Dark Scrollbar */
	::-webkit-scrollbar {
		width: 8px;
		height: 8px;
	}
	::-webkit-scrollbar-track {
		background: #000;
	}
	::-webkit-scrollbar-thumb {
		background: #222;
		border-radius: 4px;
	}
	::-webkit-scrollbar-thumb:hover {
		background: #444;
	}
	* {
		scrollbar-width: thin;
		scrollbar-color: #222 #000;
	}
"""
content = content.replace("<style is:global>", "<style is:global>\n" + scroll_css)

with open("site/src/layouts/Layout.astro", "w") as f:
    f.write(content)

with open("site/src/pages/index.astro", "r") as f:
    content2 = f.read()

# Remove JEE Advanced
content2 = content2.replace("JEE Advanced.", "JEE.")

# Add staggering animations to concept cards and floating to visuals
animation_css = """
	/* Staggered Card Entry */
	.concept-card {
		opacity: 0;
		animation: fadeUpCard 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
	}
	.concept-card:nth-child(1) { animation-delay: 0.2s; }
	.concept-card:nth-child(2) { animation-delay: 0.3s; }
	.concept-card:nth-child(3) { animation-delay: 0.4s; }
	.concept-card:nth-child(4) { animation-delay: 0.5s; }
	.concept-card:nth-child(n+5) { animation-delay: 0.6s; }

	@keyframes fadeUpCard {
		0% { opacity: 0; transform: translateY(30px); }
		100% { opacity: 1; transform: translateY(0); }
	}

	/* Floating Visuals */
	.visual-container {
		animation: float 6s ease-in-out infinite;
	}
	@keyframes float {
		0% { transform: translateY(0px); }
		50% { transform: translateY(-8px); }
		100% { transform: translateY(0px); }
	}
	
	/* Button hover pulse */
	button:hover {
		animation: pulse 1s infinite;
	}
	@keyframes pulse {
		0% { box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.4); }
		70% { box-shadow: 0 0 0 6px rgba(255, 255, 255, 0); }
		100% { box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
	}
"""
content2 = content2.replace("/* Card Enhancements */", animation_css + "\n\t/* Card Enhancements */")

with open("site/src/pages/index.astro", "w") as f:
    f.write(content2)
