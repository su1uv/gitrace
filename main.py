import os

from dotenv import load_dotenv

from src.app import app

load_dotenv()


def main():
    work_dir: str | None = os.environ.get("REPO_TEST")
    if work_dir is None:
        work_dir = ""

    file: str = "src/main.py"

    app(work_dir, file)


if __name__ == "__main__":
    main()
