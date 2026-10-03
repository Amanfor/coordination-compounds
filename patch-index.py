with open("site/src/pages/index.astro", "r") as f:
    content = f.read()

# We will replace the <div class="hero"> section and add styles
hero_html = """
	<div class="hero">
		<div class="hero-visual">
			<div class="orbit orbit-1"></div>
			<div class="orbit orbit-2"></div>
			<div class="orbit orbit-3"></div>
			<div class="core">M</div>
		</div>
		<div class="hero-content">
			<h2 class="animate-title">coordination<br>chemistry</h2>
			<p class="subtitle animate-subtitle">A visual, minimal guide for JEE Advanced.</p>
		</div>
	</div>
"""

# Replace old hero
import re
content = re.sub(r'<div class="hero">.*?</div>', hero_html, content, flags=re.DOTALL)

# Add CSS
styles = """
	/* Hero Animations */
	.hero {
		display: flex;
		align-items: center;
		gap: 3rem;
		margin-bottom: 5rem;
		padding: 3rem 0;
		border-bottom: 1px solid var(--border);
	}
	.hero-content {
		flex: 1;
	}
	.hero-visual {
		position: relative;
		width: 150px;
		height: 150px;
		display: flex;
		justify-content: center;
		align-items: center;
		flex-shrink: 0;
	}
	
	@media (max-width: 600px) {
		.hero {
			flex-direction: column-reverse;
			text-align: center;
			gap: 2rem;
			padding: 2rem 0;
		}
	}

	/* CSS Atom/Orbital Animation */
	.core {
		position: absolute;
		width: 30px;
		height: 30px;
		background: #fff;
		color: #000;
		border-radius: 50%;
		display: flex;
		justify-content: center;
		align-items: center;
		font-weight: bold;
		font-size: 14px;
		z-index: 10;
		box-shadow: 0 0 15px rgba(255,255,255,0.5);
	}
	.orbit {
		position: absolute;
		width: 100%;
		height: 100%;
		border: 1px dashed rgba(255, 255, 255, 0.3);
		border-radius: 50%;
	}
	.orbit-1 { animation: spin 8s linear infinite; }
	.orbit-2 { animation: spin 12s linear infinite reverse; transform: rotateX(60deg) rotateY(45deg); }
	.orbit-3 { animation: spin 10s linear infinite; transform: rotateX(45deg) rotateY(60deg); }
	
	.orbit::before {
		content: '';
		position: absolute;
		top: -4px;
		left: 50%;
		width: 8px;
		height: 8px;
		background: #fff;
		border-radius: 50%;
		box-shadow: 0 0 10px #fff;
	}

	@keyframes spin {
		0% { transform: rotate(0deg) scaleY(0.4); }
		100% { transform: rotate(360deg) scaleY(0.4); }
	}
	
	/* Text Entry Animations */
	.animate-title {
		opacity: 0;
		transform: translateY(20px);
		animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
		font-size: 2.8rem;
		line-height: 1.1;
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
		transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
	}
	.concept-card:hover {
		transform: translateY(-4px);
		border-color: #555;
		box-shadow: 0 10px 30px rgba(255,255,255,0.02);
	}
"""

content = content.replace("<style>", "<style>\n" + styles)

with open("site/src/pages/index.astro", "w") as f:
    f.write(content)
