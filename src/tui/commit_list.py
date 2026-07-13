from prompt_toolkit.widgets import RadioList


def commit_list(commits: list[tuple[str, str]]) -> RadioList:
    commits_list: RadioList = RadioList(values=commits, select_on_focus=True)

    return commits_list
