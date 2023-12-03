from importlib.resources import open_text
from jinja2 import Template


def _load_template(name: str) -> Template:
    print('Loading template: ' + name)
    with open_text('templates', name+'.j2') as tmpl:
        return Template(tmpl.read())


hero = _load_template('hero')
