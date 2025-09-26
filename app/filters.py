import flask
from markdown import markdown as md
from markupsafe import Markup

def register_filters(app: flask.Flask):
    def register(name, fun):
        app.jinja_env.filters[name] = fun
    register("markdown", markdown)
    
def markdown(text: str | None) -> Markup:
    if text is None:
        return Markup("")
    return Markup(md(text))