# gitrace

A terminal UI for tracing a file's history through git commits.

gitrace shows you every commit that touched a given file and lets you browse the
file's contents at each of those commits, with syntax highlighting — all from
inside the terminal.

> **Status:** early stage / work-in-progress. The target file is currently
> hard-coded and the repo is read from an environment variable. Expect breaking
> changes.

## Features

- Lists all commits that modified a file (via `git log --follow`, so renames
  are followed).
- Select a commit to instantly preview the file's content at that commit
  (`git show <commit>:<file>`).
- Syntax-highlighted preview (Pygments, `one-dark` style).
- Full-screen TUI built with `prompt_toolkit`.

## Requirements

- Python >= 3.13
- git (available on `PATH`)
- [uv](https://docs.astral.sh/uv/) (recommended for dependency management)

## Setup

```sh
uv sync
```

Create a `.env` file in the project root pointing at the repo you want to
inspect:

```sh
echo "REPO_TEST=/path/to/your/repo" > .env
```

## Usage

```sh
uv run main.py
```

Keybindings:

| Key     | Action                  |
| ------- | ----------------------- |
| `Up`/`Down` | Move between commits |
| `Enter` | (radio list default)    |
| `Ctrl+Q`| Quit                    |

## Project structure

```
.
├── main.py                     # Entry point; loads env, launches the app
├── pyproject.toml              # Project metadata + dependencies
├── src
│   ├── app.py                  # TUI layout, keybindings, application
│   ├── consts.py
│   ├── get_commits.py          # git log --follow -> list of commits
│   ├── get_file_per_commit.py  # git show <commit>:<file> -> file content
│   └── tui
│       ├── commit_content.py   # Highlighted preview pane
│       └── commit_list.py      # Commit selector (radio list)
└── uv.lock
```

## Roadmap

- [ ] Configurable / interactive file selection (instead of hard-coded path)
- [ ] Multi-language syntax highlighting (currently Python-only)
- [ ] Diff view between commits
- [ ] Search / filter commits
- [ ] Configurable theme

## License

[MIT](LICENSE)
