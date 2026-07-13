import subprocess


def get_commits(work_dir: str, file_path: str) -> list[tuple[str, str]]:
    commits: list[tuple[str, str]] = []

    get_commits: subprocess.CompletedProcess = subprocess.run(
        ("git", "-C", work_dir, "log", "--follow", file_path),
        capture_output=True,
        text=True,
    )
    if isinstance(get_commits.stdout, str):
        commits_list: list[str] = get_commits.stdout.replace("\n\n", "\n").split(
            "commit "
        )
    else:
        return commits

    for commit in commits_list:
        if commit == "":
            continue
        commit_content: list[str] = commit.splitlines()
        commit_value: str = commit_content[0].strip()
        commit_label: str = commit_content[3].strip()

        commit_option: tuple[str, str] = (commit_value, commit_label)
        commits.append(commit_option)

    return commits
