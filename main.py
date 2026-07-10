import os

import pygments
from dotenv import load_dotenv
from prompt_toolkit import HTML, choice, print_formatted_text
from prompt_toolkit.filters import is_done
from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit.styles import Style
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from pygments.lexers.python import PythonLexer
from pygments.styles import get_style_by_name

from src.get_commits import get_commits
from src.show_file import get_file_content

load_dotenv()


styles = Style.from_dict(
    {
        "frame.border": "#ff4444",
        "selected-option": "bold",
        "bottom-toolbar": "#ffffff bg:#333333 noreverse",
    }
)


def main():
    work_dir: str | None = os.environ.get("REPO_TEST")
    if work_dir is None:
        work_dir = ""

    file: str = "src/main.py"

    commits: dict[str, tuple[str, str, str]] = get_commits(work_dir, file)
    options: list[tuple[str, str]] = []
    for commit in commits:
        options.append((commit, commits[commit][2]))

    result: str = choice(
        message=f"select a commit from {file}",
        options=options,
        style=styles,
        bottom_toolbar=HTML(
            " Press <b>[Up]</b>/<b>[Down]</b> to select, <b>[Enter]</b> to accept."
        ),
        show_frame=~is_done,
    )

    content: str = get_file_content("git", work_dir, file, result)

    style = style_from_pygments_cls(get_style_by_name("one-dark"))
    lexer = pygments.lex(content, lexer=PythonLexer())
    tokens = list(lexer)
    print_formatted_text(PygmentsTokens(tokens), style=style)


if __name__ == "__main__":
    main()
