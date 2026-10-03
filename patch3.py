with open("site/src/layouts/Layout.astro", "r") as f:
    content = f.read()

markdown_styles = """
	/* Markdown Content Styles */
	.concept-body p, .q-text p, .sol-text p {
		margin-bottom: 1rem;
		line-height: 1.6;
		color: #ccc;
	}
	.concept-body ul, .sol-text ul {
		margin-bottom: 1.5rem;
		padding-left: 1.5rem;
		color: #ccc;
	}
	.concept-body li, .sol-text li {
		margin-bottom: 0.5rem;
		line-height: 1.6;
	}
	.concept-body strong, .sol-text strong, .q-text strong {
		color: #fff;
		font-weight: 600;
	}
	.concept-body em, .sol-text em, .q-text em {
		color: var(--accent);
		font-style: italic;
	}
"""

content = content.replace("</style>", markdown_styles + "\n</style>")

with open("site/src/layouts/Layout.astro", "w") as f:
    f.write(content)
