from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from prompt_toolkit.widgets import (
    Frame,
    HorizontalLine,
    RadioList,
    TextArea,
)
from pygments.lexers.python import PythonLexer
from pygments.styles import get_style_by_name

kb = KeyBindings()


@kb.add("c-q")
def exit_(event):
    event.app.exit()


def app(file_text, commits):
    style: Style = style_from_pygments_cls(get_style_by_name("one-dark"))
    textarea = TextArea(
        text=file_text,
        lexer=PygmentsLexer(PythonLexer),
    )
    print(textarea)
    root_container = HSplit(
        [
            Frame(body=RadioList(values=commits)),
            HorizontalLine(),
            Frame(body=textarea),
        ]
    )
    layout = Layout(root_container)
    app = Application(layout=layout, key_bindings=kb, full_screen=True, style=style)
    app.run()
