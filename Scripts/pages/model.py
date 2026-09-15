from dash import (
    html,
    dcc,
    Input,
    Output,
    State,
    callback,
    register_page,
)

from utils.ml_pipeline import predict_survival
from utils.navigation import page_navigation


register_page(__name__, path="/model")


layout = html.Div(
    [
        html.H1("Predict Survival"),

        html.P(
            "Enter a passenger profile and use the trained logistic "
            "regression model to estimate their survival probability."
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Label("Passenger Class"),
                                dcc.Dropdown(
                                    id="pclass-input",
                                    className="model-dropdown",
                                    options=[
                                        {"label": "First Class", "value": 1},
                                        {"label": "Second Class", "value": 2},
                                        {"label": "Third Class", "value": 3},
                                    ],
                                    value=3,
                                ),
                            ],
                            className="form-field",
                        ),

                        html.Div(
                            [
                                html.Label("Sex"),
                                dcc.Dropdown(
                                    id="sex-input",
                                    className="model-dropdown",
                                    options=[
                                        {"label": "Female", "value": "female"},
                                        {"label": "Male", "value": "male"},
                                    ],
                                    value="male",
                                ),
                            ],
                            className="form-field",
                        ),

                        html.Div(
                            [
                                html.Label("Age"),
                                dcc.Input(
                                    id="age-input",
                                    type="number",
                                    value=0,
                                    min=0,
                                    max=100,
                                    step=1,
                                ),
                            ],
                            className="form-field",
                        ),

                        html.Div(
                            [
                                html.Label("Port of Embarkation"),
                                dcc.Dropdown(
                                    id="embarked-input",
                                    className="model-dropdown",
                                    options=[
                                        {"label": "Cherbourg", "value": "C"},
                                        {"label": "Queenstown", "value": "Q"},
                                        {"label": "Southampton", "value": "S"},
                                    ],
                                    value="S",
                                ),
                            ],
                            className="form-field",
                        ),

                        html.Div(
                            [
                                html.Label("Siblings / Spouses Aboard"),
                                dcc.Input(
                                    id="sibsp-input",
                                    type="number",
                                    value=0,
                                    min=0,
                                    max=8,
                                    step=1,
                                ),
                            ],
                            className="form-field",
                        ),

                        html.Div(
                            [
                                html.Label("Parents / Children Aboard"),
                                dcc.Input(
                                    id="parch-input",
                                    type="number",
                                    value=0,
                                    min=0,
                                    max=6,
                                    step=1,
                                ),
                            ],
                            className="form-field",
                        ),
                    ],
                    className="model-form-grid",
                ),

                html.Button(
                    "Predict Survival",
                    id="predict-button",
                    n_clicks=0,
                ),
            ],
            className="model-form",
        ),

        html.Div(
            id="prediction-result-wrapper",
            children=dcc.Loading(
                id="loading-prediction",
                type="circle",
                color="#B8863B",
                children=html.Div(id="prediction-result"),
            ),
        ),

        page_navigation("/model"),
    ]
)


@callback(
    Output("prediction-result", "children"),

    Input("predict-button", "n_clicks"),

    State("pclass-input", "value"),
    State("sex-input", "value"),
    State("age-input", "value"),
    State("embarked-input", "value"),
    State("sibsp-input", "value"),
    State("parch-input", "value"),

    prevent_initial_call=True,
)
def predict_survival_callback(
    n_clicks,
    pclass,
    sex,
    age,
    embarked,
    sibsp,
    parch,
):

    if age is None:
        return html.Div(
            [
                html.P(
                    "Please enter an age before making a prediction."
                )
            ],
            className="prediction-card validation-message",
        )

    if sibsp is None or parch is None:
        return html.Div(
            [
                html.P(
                    "Please enter values for siblings/spouses "
                    "and parents/children."
                )
            ],
            className="prediction-card validation-message",
        )

    if not (0 <= age <= 100):
        return html.Div(
            [
                html.P("Age must be between 0 and 100.")
            ],
            className="prediction-card validation-message",
        )

    if not (0 <= sibsp <= 8):
        return html.Div(
            [
                html.P(
                    "Siblings/spouses aboard must be between 0 and 8."
                )
            ],
            className="prediction-card validation-message",
        )

    if not (0 <= parch <= 6):
        return html.Div(
            [
                html.P(
                    "Parents/children aboard must be between 0 and 6."
                )
            ],
            className="prediction-card validation-message",
        )

    result = predict_survival(
        pclass=pclass,
        sex=sex,
        age=age,
        embarked=embarked,
        sibsp=sibsp,
        parch=parch,
    )

    prediction = result["prediction"]
    probability = result["survival_probability"]
    family_size = result["family_size"]
    is_alone = result["is_alone"]

    survived = prediction == 1

    result_text = "Survived" if survived else "Didn't survive"

    survival_percentage = round(probability * 100, 1)

    outcome_class = "outcome-survived" if survived else "outcome-not-survived"
    result_class = "prediction-success" if survived else "prediction-danger"
    icon = "✓" if survived else "✕"

    return html.Div(
        [
            html.Div(
                [
                    html.Span(icon, className="prediction-icon"),

                    html.Div(
                        [
                            html.P("Predicted outcome", className="result-label"),
                            html.H2(result_text, className=result_class),
                        ]
                    ),
                ],
                className="prediction-header",
            ),

            html.Div(
                html.Div(
                    className="probability-bar-fill",
                    style={"width": f"{survival_percentage}%"},
                ),
                className="probability-bar",
            ),

            html.P(
                f"Estimated survival probability: {survival_percentage}%",
                className="probability-caption",
            ),

            html.Div(
                [
                    html.Div(
                        [
                            html.P("Family size", className="detail-label"),
                            html.P(str(family_size), className="detail-value"),
                        ]
                    ),

                    html.Div(
                        [
                            html.P("Travelling alone", className="detail-label"),
                            html.P(
                                "Yes" if is_alone else "No",
                                className="detail-value",
                            ),
                        ]
                    ),
                ],
                className="prediction-details",
            ),

            html.P(
                "This is a model-based estimate derived from patterns "
                "in the Titanic training dataset, not a historical certainty.",
                className="model-note",
            ),
        ],
        className=f"prediction-card {outcome_class}",
    )
