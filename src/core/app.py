import pytermgui as ptg
from src.core.search import search
from src.core.parsers.parser import parser
OUTPUT = {}


def chose_result(result):
    parse = parser(result)

    with ptg.WindowManager() as manager:
        window = (
            ptg.Window(
                ptg.Container(
                    ptg.Label(f"{parse}"),
                )
            )
            .set_title("Parsed Info")
        )

        manager.add(window)

def submit(manager: ptg.WindowManager, window: ptg.Window) -> None:
    for widget in window:
        if isinstance(widget, ptg.InputField):
            OUTPUT[widget.prompt] = widget.value
            continue

    search_results = search(OUTPUT["Title: "])
    results(search_results)
    manager.stop()


def function_search(self):
    with ptg.WindowManager() as manager:
        search_window = (
            ptg.Window(
                "",
                ptg.InputField(prompt="Title: "),
                ["Submit", lambda *_: submit(manager, search_window)]
            )
            .set_title("Search...")
            .center()
        )

        manager.add(search_window)


def app():
    with ptg.WindowManager() as main_manager:
        main_window = (
            ptg.Window(
                ptg.Container(
                    ptg.Button("Search", onclick=function_search),
                )
            )
            .set_title("GameManager")
        )

        main_manager.add(main_window)


def results(results):
    with ptg.WindowManager() as manager:
        window = (
            ptg.Window(
                ptg.Container(
                    ptg.Button(results[0], onclick=chose_result),
                    ptg.Button(results[1], onclick=chose_result),
                    ptg.Button(results[2], onclick=chose_result),
                    ptg.Button(results[3], onclick=chose_result)
                )
            )
            .set_title("Results")
        )

        manager.add(window)
