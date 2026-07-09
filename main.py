import os
import subprocess

from consts import TEST_REPO


def main():
    git_path_abs: str = "/usr/bin/git"
    print(git_path_abs)
    file_path_abs: str = os.path.join(TEST_REPO, "src/main.py")

    ps = subprocess.Popen(
        (
            git_path_abs,
            "-C",
            TEST_REPO,
            "show",
            "4a1c61ab4f84278dc7ac9376d389a830a67039b0:src/main.py",
        ),
        stdout=subprocess.PIPE,
    )
    output = subprocess.run(("bat"), stdin=ps.stdout)
    ps.wait()
    # commit_list: list[str] = output.stdout.split("commit ")
    # print("first item: ", commit_list[0])
    # print("second item: ", commit_list[1])


if __name__ == "__main__":
    main()
