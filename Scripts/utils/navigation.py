from dash import dcc, html


PAGE_ORDER = [
    ("/", "Home"),
    ("/explore", "Explore"),
    ("/model", "Model"),
    ("/conclusions", "Conclusions"),
    ("/under-the-hood", "Under the Hood"),
]


def page_navigation(current_path):
    """
    Create Previous / Next navigation based on page order.
    """

    current_index = next(
        index
        for index, (path, _) in enumerate(PAGE_ORDER)
        if path == current_path
    )

    previous_page = (
        PAGE_ORDER[current_index - 1]
        if current_index > 0
        else None
    )

    next_page = (
        PAGE_ORDER[current_index + 1]
        if current_index < len(PAGE_ORDER) - 1
        else None
    )

    previous = (
        dcc.Link(
            f"← {previous_page[1]}",
            href=previous_page[0],
            className="page-nav-button",
        )
        if previous_page
        else html.Div()
    )

    next_ = (
        dcc.Link(
            f"{next_page[1]} →",
            href=next_page[0],
            className="page-nav-button",
        )
        if next_page
        else html.Div()
    )

    return html.Div(
        [
            previous,
            next_,
        ],
        className="page-navigation",
    )