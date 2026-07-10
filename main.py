import os

from dotenv import load_dotenv
from prompt_toolkit import choice, prompt

from src.get_commits import get_commits

load_dotenv()


def main():
    work_dir: str | None = os.environ.get("REPO_TEST")
    if work_dir is None:
        work_dir = ""

    file: str = prompt("Insert the file path: ")

    commits: dict[str, tuple[str, str, str]] = get_commits(work_dir, file)
    options: list[tuple[str, str]] = []
    for commit in commits:
        options.append((commit, commits[commit][2]))

    result = choice(message=f"select a commit of {file}", options=options)
    print(result)


if __name__ == "__main__":
    main()
