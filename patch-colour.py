with open("site/src/components/visuals/ColourWheel.astro", "r") as f:
    content = f.read()

styles = """
  .slice { cursor: pointer; transition: transform 0.2s, opacity 0.2s; }
  .slice:hover { opacity: 0.8; transform: scale(1.05); }
  
  #colour-wheel > g {
    animation: slowSpin 20s linear infinite;
    transform-origin: center;
  }
  #colour-wheel:hover > g {
    animation-play-state: paused;
  }
  @keyframes slowSpin {
    from { transform: translate(150px, 150px) rotate(0deg); }
    to { transform: translate(150px, 150px) rotate(360deg); }
  }
"""

content = content.replace(".slice { cursor: pointer; transition: opacity 0.2s; }", styles)
content = content.replace(".slice:hover { opacity: 0.8; }", "")

with open("site/src/components/visuals/ColourWheel.astro", "w") as f:
    f.write(content)
