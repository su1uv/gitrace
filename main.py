import _io
import os
import subprocess

from consts import TEST_REPO


def main():
    git_path_abs: str = "/usr/bin/git"
    file_path_abs: str = os.path.join(TEST_REPO, "src/main.py")

    get_commits: subprocess.CompletedProcess = subprocess.run(
        ("git", "-C", TEST_REPO, "log", "--follow", "src/main.py"),
        capture_output=True,
        text=True,
    )
    commits_list: list[str] = []
    if isinstance(get_commits.stdout, str):
        commits_list = get_commits.stdout.split("commit ")

    for commit in commits_list:
        print(commit)

    ps: subprocess.Popen[bytes] = subprocess.Popen(
        (
            git_path_abs,
            "-C",
            TEST_REPO,
            "show",
            "4a1c61ab4f84278dc7ac9376d389a830a67039b0:src/main.py",
        ),
        stdout=subprocess.PIPE,
    )
    if isinstance(ps.stdout, _io.BufferedReader):
        output = subprocess.run(["bat", "-l", "python"], stdin=ps.stdout)

    ps.wait()


if __name__ == "__main__":
    main()
