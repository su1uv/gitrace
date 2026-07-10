import subprocess


def get_commits(work_dir: str, file_path: str) -> dict[str, tuple[str, str, str]]:
    commits_dict: dict[str, tuple[str, str, str]] = {}

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
        return commits_dict

    for commit in commits_list:
        if commit == "":
            continue
        commit_content: list[str] = commit.splitlines()
        commit_id: str = commit_content[0].strip()
        commit_author: str = commit_content[1].strip()
        commit_date: str = commit_content[2].strip()
        commit_msg: str = commit_content[3].strip()

        commit_data: tuple[str, str, str] = (commit_author, commit_date, commit_msg)
        commits_dict[commit_id] = commit_data

    return commits_dict
