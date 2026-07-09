import os

from consts import TEST_REPO
from get_commits import get_commits


def main():
    git_path_abs: str = "/usr/bin/git"
    file_path_abs: str = os.path.join(TEST_REPO, "src/main.py")

    commits: dict[str, tuple[str, str, str]] = get_commits(TEST_REPO, "src/main.py")
    for commit in commits.values():
        print(commit)


if __name__ == "__main__":
    main()
