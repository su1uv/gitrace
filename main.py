import os

from dotenv import load_dotenv

from src.get_commits import get_commits

load_dotenv()


def main():
    work_dir: str | None = os.environ.get("REPO_TEST")
    if work_dir is None:
        work_dir = ""

    commits: dict[str, tuple[str, str, str]] = get_commits(work_dir, "src/main.py")
    for commit in commits.values():
        print(commit)


if __name__ == "__main__":
    main()
