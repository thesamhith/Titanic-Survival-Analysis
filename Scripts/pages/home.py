from dash import html, dcc, register_page

from utils.data_loader import get_data
from utils.navigation import page_navigation


register_page(__name__, path="/")


df = get_data()


dataset_preview = df[
    [
        "Survived",
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked",
    ]
].head(5)


preview_table = html.Table(
    [
        html.Thead(
            html.Tr(
                [
                    html.Th(column)
                    for column in dataset_preview.columns
                ]
            )
        ),

        html.Tbody(
            [
                html.Tr(
                    [
                        html.Td(str(row[column]))
                        for column in dataset_preview.columns
                    ]
                )
                for _, row in dataset_preview.iterrows()
            ]
        ),
    ],
    className="dataset-table",
)


layout = html.Div(
    [
        html.Section(
            [
                html.Div(
                    [
                        html.P(
                            "RMS TITANIC",
                            className="hero-eyebrow",
                        ),

                        html.H1(
                            "Exploring survival aboard RMS Titanic"
                        ),

                        html.P(
                            "A data-driven look at the passenger "
                            "characteristics and circumstances associated "
                            "with survival — followed by a simple "
                            "predictive model.",
                            className="hero-subtitle",
                        ),

                        html.Div(
                            [
                                dcc.Link(
                                    "Explore the data",
                                    href="/explore",
                                    className="button",
                                ),

                                dcc.Link(
                                    "Try the model",
                                    href="/model",
                                    className="button hero-secondary-button",
                                ),
                            ],
                            className="hero-actions",
                        ),
                    ],
                    className="hero-content",
                )
            ],
            className="hero-section",
        ),

        html.Section(
            [
                html.Div(
                    [
                        html.H2("The historical context"),

                        html.P(
                            "RMS Titanic departed Southampton on 10 April 1912 "
                            "on her maiden voyage to New York, stopping at Cherbourg "
                            "and Queenstown along the way. On the night of 14 April, Titanic struck an iceberg. "
                            "The ship sank in the early hours of 15 April, resulting "
                            "in the loss of approximately 1,500 lives."
                        ),

                        html.P(
                            "The passenger data from this voyage also provides an "
                            "interesting opportunity to examine how survival varied "
                            "across social, demographic and family-related factors. This project uses that data to explore those patterns "
                            "and then applies logistic regression to estimate the "
                            "survival probability of an individual passenger."
                        ),

                    ],
                    className="content-card",
                )
            ]
        ),

        html.Section(
            [
                html.H2("A quick look at the dataset"),

                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    f"{len(df):,}",
                                    className="stat-number",
                                ),
                                html.P("Kaggle training records"),
                            ],
                            className="kpi-card",
                        ),

                        html.Div(
                            [
                                html.P(
                                    "12",
                                    className="stat-number",
                                ),
                                html.P("Original dataset columns"),
                            ],
                            className="kpi-card",
                        ),

                        html.Div(
                            [
                                html.P(
                                    "79.3%",
                                    className="stat-number",
                                ),
                                html.P("Model test accuracy"),
                            ],
                            className="kpi-card",
                        ),
                    ],
                    className="stats-grid",
                ),

                html.Div(
                    [
                        html.H3("Sample passenger records"),

                        html.P(
                            "The original dataset contains passenger attributes "
                            "such as class, sex, age, family relationships, fare "
                            "and embarkation port."
                        ),

                        preview_table,

                        html.H3("Dataset scope"),

                        html.P(
                            "This project uses the records contained in Kaggle's "
                            "Titanic training dataset. The historical Titanic voyage "
                            "involved roughly 2,200 people aboard, so these records "
                            "should not be interpreted as the complete passenger "
                            "and crew manifest."
                        ),

                        html.P(
                            "The model therefore learns survival patterns from this "
                            "dataset rather than attempting to reconstruct the "
                            "historical outcome of everyone aboard Titanic."
                        ),

                        html.H3("Model features"),

                        html.P(
                            "Pclass · Sex · Age · Embarked · Family Size · Is Alone"
                        ),
                    ],
                    className="content-card",
                ),
            ]
        ),

        html.Section(
            [
                html.H2("From data to prediction"),

                html.Div(
                    [
                        html.Div(
                            [
                                html.H3("1. Raw Titanic data"),
                                html.P(
                                    "Passenger records from the Kaggle "
                                    "training dataset."
                                ),
                            ],
                            className="pipeline-step",
                        ),

                        html.Div(
                            [
                                html.H3("2. Data preparation"),
                                html.P(
                                    "Handle missing values and prepare "
                                    "model inputs."
                                ),
                            ],
                            className="pipeline-step",
                        ),

                        html.Div(
                            [
                                html.H3("3. Feature engineering"),
                                html.P(
                                    "Derive family size and whether a "
                                    "passenger travelled alone."
                                ),
                            ],
                            className="pipeline-step",
                        ),

                        html.Div(
                            [
                                html.H3("4. Exploratory analysis"),
                                html.P(
                                    "Examine survival patterns across "
                                    "key variables."
                                ),
                            ],
                            className="pipeline-step",
                        ),

                        html.Div(
                            [
                                html.H3("5. Logistic regression"),
                                html.P(
                                    "Train and evaluate a binary "
                                    "classification model."
                                ),
                            ],
                            className="pipeline-step",
                        ),

                        html.Div(
                            [
                                html.H3("6. Survival estimate"),
                                html.P(
                                    "Estimate survival probability for "
                                    "an individual profile."
                                ),
                            ],
                            className="pipeline-step",
                        ),
                    ],
                    className="pipeline-grid",
                ),
            ]
        ),

                        html.Div(
                        [
                            html.H3("One last thing..."),
                            html.P(
                                "Sorry, Jack. The model doesn't account for the door!",
                            className="easter-egg-title"
                        ),
                            html.P(
                            "It does, however, look at the passenger characteristics "
                            "that were associated with survival."
                        ),
                    ],
                    className="easter-egg"
        ),

        html.Section(
            [
                html.Div(
                    [
                        html.H2("Explore the analysis"),

                        html.P(
                            "Start with the observed survival patterns, then see "
                            "how the model responds to different passenger profiles."
                        ),

                        dcc.Link(
                            "Explore the data",
                            href="/explore",
                            className="button",
                        ),

                        dcc.Link(
                            "Try the model",
                            href="/model",
                            className="button secondary-cta-button",
                        ),
                    ],
                    className="content-card",
                )
            ]
        ),

        page_navigation("/"),
    ]
)