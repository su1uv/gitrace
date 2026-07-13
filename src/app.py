from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from prompt_toolkit.widgets import (
    Frame,
    RadioList,
)
from pygments.styles import get_style_by_name

from .get_commits import get_commits
from .tui.commit_content import commit_content
from .tui.commit_list import commit_list

kb = KeyBindings()


@kb.add("c-q")
def exit_(event):
    event.app.exit()


def app(work_dir, file_path):
    style: Style = style_from_pygments_cls(get_style_by_name("one-dark"))
    commits: list[tuple[str, str]] = get_commits(work_dir, file_path)
    commits_options: RadioList = commit_list(commits)
    commit_preview: Window = commit_content(commits_options, work_dir, file_path)

    root_container = HSplit(
        [
            Frame(body=commits_options),
            Frame(body=commit_preview),
        ]
    )

    layout = Layout(root_container)
    app = Application(layout=layout, key_bindings=kb, full_screen=True, style=style)
    app.run()
