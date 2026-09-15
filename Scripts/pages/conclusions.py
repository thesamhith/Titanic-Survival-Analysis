from dash import html, register_page

from utils.navigation import page_navigation


register_page(__name__, path="/conclusions")


layout = html.Div(
    [
        html.H1("Conclusions"),

        html.P(
            "The Titanic dataset shows that survival was strongly associated "
            "with passenger characteristics such as sex, passenger class, "
            "age and family circumstances."
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.Span("1", className="finding-number"),
                        html.H2("Sex was strongly associated with survival"),
                    ],
                    className="finding-header",
                ),

                html.P(
                    "Female passengers had substantially higher observed survival "
                    "rates than male passengers. Sex was one of the strongest "
                    "patterns visible in the dataset."
                ),
            ],
            className="chart-card finding-card",
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.Span("2", className="finding-number"),
                        html.H2("Passenger class mattered"),
                    ],
                    className="finding-header",
                ),

                html.P(
                    "First-class passengers had higher observed survival rates "
                    "than second- and third-class passengers. Passenger class "
                    "can therefore be viewed as an important proxy for differences "
                    "in access and circumstances aboard the ship."
                ),
            ],
            className="chart-card finding-card",
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.Span("3", className="finding-number"),
                        html.H2("Factors interact"),
                    ],
                    className="finding-header",
                ),

                html.P(
                    "Looking at sex and passenger class together revealed patterns "
                    "that are less obvious when examining each variable separately. "
                    "This is why the model considers multiple features together."
                ),
            ],
            className="chart-card finding-card",
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.Span("4", className="finding-number"),
                        html.H2("Family circumstances showed a non-linear pattern"),
                    ],
                    className="finding-header",
                ),

                html.P(
                    "Family size was not simply associated with progressively "
                    "higher or lower survival. Some family-size groups had very "
                    "different observed survival rates, particularly where group "
                    "sizes were small."
                ),
            ],
            className="chart-card finding-card",
        ),

        html.Div(
            [
                html.H2("Logistic Regression Model"),

                html.P(
                    "A logistic regression model was selected because the target "
                    "variable is binary: survived or did not survive. It also "
                    "provides an interpretable baseline for estimating survival "
                    "probabilities from multiple passenger characteristics."
                ),

                html.P(
                    "The model uses passenger class, sex, age, embarkation point, "
                    "family size and whether the passenger was travelling alone."
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                html.P("Accuracy", className="metric-label"),
                                html.P("79.3%", className="metric-value"),
                            ],
                            className="metric-chip",
                        ),
                        html.Div(
                            [
                                html.P("Precision", className="metric-label"),
                                html.P("75.0%", className="metric-value"),
                            ],
                            className="metric-chip",
                        ),
                        html.Div(
                            [
                                html.P("Recall", className="metric-label"),
                                html.P("69.6%", className="metric-value"),
                            ],
                            className="metric-chip",
                        ),
                        html.Div(
                            [
                                html.P("F1 score", className="metric-label"),
                                html.P("72.2%", className="metric-value"),
                            ],
                            className="metric-chip",
                        ),
                    ],
                    className="metrics-grid",
                ),
            ],
            className="chart-card",
        ),

        html.Div(
            [
                html.H2("Limitations"),

                html.P(
                    "These results describe associations within the Titanic "
                    "dataset and should not be interpreted as proof of causation."
                ),

                html.P(
                    "Age contains imputed values, some groups contain relatively "
                    "few passengers, and the model is intentionally simple. "
                    "Its predictions should therefore be treated as estimates "
                    "rather than historical certainty."
                ),
            ],
            className="chart-card limitations-card",
        ),

        page_navigation("/conclusions"),
    ]
)