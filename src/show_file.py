import subprocess


def get_file_content(
    git_path_abs: str, work_dir: str, file_path: str, commit_id: str
) -> str:
    ps: subprocess.CompletedProcess = subprocess.run(
        (
            git_path_abs,
            "-C",
            work_dir,
            "show",
            f"{commit_id}:{file_path}",
        ),
        capture_output=True,
        text=True,
    )

    return ps.stdout
