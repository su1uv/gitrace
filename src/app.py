import pygments
from prompt_toolkit import Application
from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.lexers.pygments import PygmentsLexer
from prompt_toolkit.styles import Style
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from prompt_toolkit.widgets import (
    Frame,
    RadioList,
)
from pygments.lexers.python import PythonLexer
from pygments.styles import get_style_by_name

from .show_file import get_file_content

kb = KeyBindings()


@kb.add("c-q")
def exit_(event):
    event.app.exit()


def app(work_dir, file_path, commits):
    style: Style = style_from_pygments_cls(get_style_by_name("one-dark"))
    commit_list = RadioList(values=commits)

    def get_commit_content() -> PygmentsTokens:
        commit_id = commit_list.current_value
        commit_content = get_file_content("git", work_dir, file_path, commit_id)
        tokens = list(pygments.lex(commit_content, lexer=PythonLexer()))
        commit_tokens = PygmentsTokens(tokens)

        return commit_tokens

    root_container = HSplit(
        [
            Frame(body=commit_list),
            Frame(body=Window(content=FormattedTextControl(text=get_commit_content))),
        ]
    )

    layout = Layout(root_container)
    app = Application(layout=layout, key_bindings=kb, full_screen=True, style=style)
    app.run()
