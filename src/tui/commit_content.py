import pygments
from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import RadioList
from pygments.lexers.python import PythonLexer

from ..get_file_per_commit import get_file_per_commit


def commit_content(commits_options: RadioList, work_dir: str, file_path: str) -> Window:
    def get_commit_content() -> PygmentsTokens:
        commit_id = commits_options.current_value
        commit_content = get_file_per_commit(work_dir, file_path, commit_id)
        tokens = list(pygments.lex(commit_content, lexer=PythonLexer()))
        commit_tokens = PygmentsTokens(tokens)

        return commit_tokens

    return Window(content=FormattedTextControl(text=get_commit_content))
