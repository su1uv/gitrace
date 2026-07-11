import os

from dotenv import load_dotenv
from prompt_toolkit.styles import Style

from src.app import app
from src.get_commits import get_commits

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

    content = "hola"
    # content: str = get_file_content("git", work_dir, file, result)
    app(content, options)


if __name__ == "__main__":
    main()
