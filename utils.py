def render_html(path: str) -> str:
    """Returns html file like string"""
    with open(path, 'r', encoding='utf-8') as html:
        return html.read()
