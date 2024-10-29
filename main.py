"""
Very much inspired by the README of the author of rich:
    https://github.com/willmcgugan/willmcgugan
"""

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("😄 [link=https://www.maartengrootendorst.com]Maarten Grootendorst", guide_style="bold cyan")
book_tree = tree.add("📖 Book Author")
book_tree.add("[link=https://www.amazon.com/Hands-Large-Language-Models-Alammar-ebook/dp/B0DGZ46G88]Hands-On Large Language Models")
packages_tree = tree.add("🧙‍♂️ Open Sourcerer")
packages_tree.add("[link=https://github.com/MaartenGr/BERTopic]BERTopic")
packages_tree.add("[link=https://github.com/MaartenGr/KeyBERT]KeyBERT")
packages_tree.add("[link=https://github.com/MaartenGr/PolyFuzz]PolyFuzz")
articles_tree = tree.add("📘 Demystifying AI")
articles_tree.add("[link=https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts]A Visual Guide to Mixture of Experts")
articles_tree.add("[link=https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization]A Visual Guide to Quantization")
articles_tree.add("[link=https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state]A Visual Guide to Mamba")
articles_tree.add("[link=https://towardsdatascience.com/9-distance-measures-in-data-science-918109d069fa?sk=5a95055c23e46aed2db69271b559b464]9 Distance Measures")
articles_tree.add("[link=https://towardsdatascience.com/keyword-extraction-with-bert-724efca412ea?sk=97a99c2669bb16f22f2f362820ba6bef]Keyword Extraction with BERT")
articles_tree.add("[link=https://towardsdatascience.com/topic-modeling-with-bert-779f7db187e6?sk=0b5a470c006d1842ad4c8a3057063a99]Topic Modeling with BERT")


about = """\
A psychologist turned data scientist who is passionate about using AI to make the world a slightly better place. I enjoy working on open source projects and writing (visual) AI-related articles on [link=https://newsletter.maartengrootendorst.com/]my newsletter[/].

Follow me on [bold link=https://twitter.com/MaartenGr]Twitter[/] and [bold link=https://www.linkedin.com/in/mgrootendorst/]LinkedIn[/]. 

Feel free to ask me anything!"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi 👋 I'm Maarten", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)