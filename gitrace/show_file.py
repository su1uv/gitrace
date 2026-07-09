import _io
import subprocess


def show_file(git_path_abs: str, work_dir: str, file_path: str, commit_id: str):
    ps: subprocess.Popen[bytes] = subprocess.Popen(
        (
            git_path_abs,
            "-C",
            work_dir,
            "show",
            f"{commit_id}:{file_path}",
        ),
        stdout=subprocess.PIPE,
    )

    if isinstance(ps.stdout, _io.BufferedReader):
        output = subprocess.run(["bat", "-l", "python"], stdin=ps.stdout)

    ps.wait()
