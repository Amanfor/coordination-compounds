with open("site/src/layouts/Layout.astro", "r") as f:
    content = f.read()

script = """
		<script is:inline>
			document.addEventListener("DOMContentLoaded", function() {
				const render = () => {
					if (typeof renderMathInElement !== 'undefined') {
						renderMathInElement(document.body, {
							delimiters: [
								{left: '$$', right: '$$', display: true},
								{left: '$', right: '$', display: false},
								{left: '\\\\(', right: '\\\\)', display: false},
								{left: '\\\\[', right: '\\\\]', display: true}
							],
							throwOnError: false
						});
					} else {
						setTimeout(render, 100);
					}
				};
				render();
			});
		</script>
	</head>
"""

content = content.replace("</head>", script)

with open("site/src/layouts/Layout.astro", "w") as f:
    f.write(content)
