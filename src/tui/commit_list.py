from prompt_toolkit.widgets import RadioList


def commit_list(commits: list[tuple[str, str]]) -> RadioList:
    commits_list: RadioList = RadioList(
        values=commits,
        select_on_focus=True,
        open_character="",
        close_character="",
        select_character="",
        show_cursor=False,
        checked_style="bg:#A53860",
    )

    return commits_list
