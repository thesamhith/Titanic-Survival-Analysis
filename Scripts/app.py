from dash import (
    Dash,
    html,
    page_container,
    dcc,
    clientside_callback,
    Input,
    Output,
    State,
)


GITHUB_REPO = "https://github.com/thesamhith/Titanic-Survival-Analysis"


app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
)

server = app.server


SIDEBAR_LINKS = [
    ("/", "⌂", "Home"),
    ("/explore", "◈", "Explore"),
    ("/model", "◎", "Model"),
    ("/conclusions", "✓", "Conclusions"),
    ("/under-the-hood", "⚙", "Under the Hood"),
]


app.layout = html.Div(
    [
        dcc.Store(
            id="theme-store",
            storage_type="local",
        ),

        dcc.Store(
            id="sidebar-store",
            storage_type="local",
            data=False,
        ),

        html.Div(
            [
                # =====================================================
                # SIDEBAR
                # =====================================================

                html.Aside(
                    [
                        html.Div(
                            [
                                html.Div(
                                    "T",
                                    className="sidebar-logo",
                                ),

                                html.Div(
                                    "Titanic Survival Analysis",
                                    className="sidebar-title",
                                ),
                            ],
                            className="sidebar-brand",
                        ),

                        html.Button(
                            "☰",
                            id="sidebar-toggle",
                            className="sidebar-toggle",
                            n_clicks=0,
                        ),

                        html.Nav(
                            [
                                dcc.Link(
                                    [
                                        html.Span(
                                        icon,
                                        className="nav-icon",
                                    ),
                                html.Span(
                                label,
                                className="nav-label",
                                ),
                            ],
                            href=href,
                            className="sidebar-link",
                            )
                            for href, icon, label in SIDEBAR_LINKS
                        ],
                        className="sidebar-nav",
                        ),

                        html.Div(
                            [
                                html.A(
                                    [
                                        html.Span(
                                            html.Img(
                                                src="https://cdn.simpleicons.org/github/ffffff",
                                                alt="GitHub",
                                                width="16",
                                                height="16",
                                            ),
                                            className="nav-icon",
                                        ),
                                        html.Span(
                                            "GitHub",
                                            className="nav-label",
                                        ),
                                    ],
                                    href=GITHUB_REPO,
                                    target="_blank",
                                    className="sidebar-github",
                                ),

                                html.Button(
                                    "🌙",
                                    id="theme-toggle",
                                    className="theme-button",
                                ),
                            ],
                            className="sidebar-bottom",
                        ),
                    ],
                    id="sidebar",
                    className="sidebar",
                ),

                # =====================================================
                # MAIN CONTENT
                # =====================================================

                html.Main(
                    page_container,
                    id="main-content",
                    className="main-container",
                ),
            ],
            id="app-shell",
            className="app-shell",
        ),
    ]
)


# =========================================================
# SIDEBAR TOGGLE
# =========================================================

clientside_callback(
    """
    function(n_clicks, collapsed) {

        if (!collapsed) {
            collapsed = false;
        }

        if (n_clicks) {
            collapsed = !collapsed;
        }

        return [
            collapsed ? "sidebar collapsed" : "sidebar",
            collapsed
        ];
    }
    """,
    Output("sidebar", "className"),
    Output("sidebar-store", "data"),
    Input("sidebar-toggle", "n_clicks"),
    State("sidebar-store", "data"),
)


# =========================================================
# THEME TOGGLE
# =========================================================

clientside_callback(
    """
    function(n_clicks, current_theme) {

        if (!current_theme) {
            current_theme =
                localStorage.getItem("titanic-theme") || "light";
        }

        const triggered =
            dash_clientside.callback_context.triggered;

        if (
            triggered.length > 0 &&
            triggered[0].prop_id === "theme-toggle.n_clicks"
        ) {
            current_theme =
                current_theme === "dark"
                    ? "light"
                    : "dark";
        }

        document.documentElement.setAttribute(
            "data-theme",
            current_theme
        );

        localStorage.setItem(
            "titanic-theme",
            current_theme
        );

        const toggle_icon =
            current_theme === "dark"
                ? "☀️"
                : "🌙";

        return [
            current_theme,
            toggle_icon
        ];
    }
    """,
    Output("theme-store", "data"),
    Output("theme-toggle", "children"),
    Input("theme-toggle", "n_clicks"),
    State("theme-store", "data"),
)


if __name__ == "__main__":
    app.run(debug=True)