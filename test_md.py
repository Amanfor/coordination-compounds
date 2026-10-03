import markdown
text = "Here is some **bold** and *italic*. \n\n- Item 1 with $x^2$\n- Item 2\n\nEquation: $$\\Delta_o$$"
html = markdown.markdown(text)
print(html)
