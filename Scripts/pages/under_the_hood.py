from dash import html, register_page

from utils.navigation import page_navigation


register_page(
    __name__,
    path="/under-the-hood",
)


GITHUB_REPO = "https://github.com/thesamhith/Titanic-Survival-Analysis"


layout = html.Div(
    [
        html.H1("Under the Hood"),

        html.P(
            "A closer look at the data, analysis, modelling and "
            "engineering behind this project."
        ),

        html.Div(
            [
                html.H2("Project Structure"),

                html.Div(
                    [
                        html.Div(
                            [
                                html.Span(className="code-window-dot"),
                                html.Span(className="code-window-dot"),
                                html.Span(className="code-window-dot"),
                                html.Span(
                                    "titanic-app/",
                                    className="code-window-label",
                                ),
                            ],
                            className="code-window-header",
                        ),

                        html.Pre(
                            """titanic-app/
├── data/
│   └── titanic.csv
├── models/
│   └── picker_pipeline.pkl
├── notebooks/
│   └── Titanic_Analysis.ipynb
    └── Titanic_ML_Model.ipynb
├── pages/
│   ├── home.py
│   ├── explore.py
│   ├── model.py
│   ├── conclusions.py
│   └── under_the_hood.py
├── utils/
│   ├── data_loader.py
│   ├── analysis.py
│   ├── ml_pipeline.py
│   └── navigation.py
├── assets/
│   └── style.css
└── app.py""",
                            className="code-block",
                        ),
                    ],
                    className="code-window",
                ),
            ],
            className="content-card",
        ),

        html.Div(
            [
                html.H2("Data & Analysis"),

                html.P(
                    "The Titanic training dataset is loaded and prepared "
                    "through a reusable data-loading layer."
                ),

                html.A(
                    "View the dataset on Kaggle →",
                    href="https://www.kaggle.com/competitions/titanic",
                    target="_blank",
                    className="inline-link",
                ),

                html.P(
                    "Missing Age values are filled using the dataset median. "
                    "Family size and age categories are derived during "
                    "data preparation."
                ),

                html.P(
                    "The analysis layer then produces the summaries used by "
                    "the visualisations on the Explore page."
                ),
            ],
            className="content-card",
        ),

        html.Div(
            [
                html.H2("Machine Learning"),

                html.P(
                    "The prediction component uses a Logistic Regression "
                    "pipeline trained on passenger characteristics and "
                    "engineered family features."
                ),

                html.P(
                    "The deployed pipeline handles preprocessing and "
                    "prediction consistently with the model used during training."
                ),

                html.P(
                    "For each passenger profile, the model returns both a "
                    "predicted outcome and an estimated survival probability."
                ),
            ],
            className="content-card",
        ),

        html.Div(
            [
                html.H2("Project Resources"),

                html.P(
                    "The complete source code, notebook and supporting "
                    "project files are available on GitHub."
                ),

                html.A(
                    "View the project on GitHub →",
                    href=GITHUB_REPO,
                    target="_blank",
                    className="button",
                ),
            ],
            className="content-card",
        ),

        page_navigation("/under-the-hood"),
    ]
)