import subprocess


def get_commits(work_dir: str, file_path: str):
    get_commits: subprocess.CompletedProcess = subprocess.run(
        ("git", "-C", work_dir, "log", "--follow", file_path),
        capture_output=True,
        text=True,
    )
    commits_list: list[str] = []
    if isinstance(get_commits.stdout, str):
        commits_list = get_commits.stdout.split("commit ")

    for commit in commits_list:
        print(commit)
