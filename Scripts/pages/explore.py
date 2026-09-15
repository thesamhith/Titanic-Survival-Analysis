import plotly.graph_objects as go

from dash import (
    html,
    dcc,
    register_page,
    callback,
    Input,
    Output,
)

from utils.data_loader import get_data

from utils.analysis import (
    get_overall_survival,
    get_class_summary,
    get_sex_summary,
    get_sex_class_summary,
    get_age_summary,
    get_family_summary,
)

from utils.navigation import page_navigation


register_page(__name__, path="/explore")


df = get_data()


CHART_FONT = "Inter, -apple-system, sans-serif"
SURVIVED_COLOR = "#2F6F5E"
NON_SURVIVED_COLOR = "#B5432D"


layout = html.Div(
    [
        html.H1("Explore the Data"),

        html.P(
            "Explore the key factors associated with passenger survival "
            "aboard the Titanic."
        ),

        html.Div(
            [
                html.H3("Overall Survival Rate"),
                html.H2(f"{get_overall_survival(df):.1%}"),
            ],
            className="kpi-card",
        ),

        html.Div(
            [
                html.H2("Passenger Class"),
                html.P(
                    "Survival varied substantially across passenger classes."
                ),
                dcc.Graph(id="graph-survival-by-class"),
            ],
            className="chart-card",
        ),

        html.Div(
            [
                html.H2("Sex"),
                html.P(
                    "Sex shows one of the strongest associations with survival."
                ),
                dcc.Graph(id="graph-survival-by-sex"),
            ],
            className="chart-card",
        ),

        html.Div(
            [
                html.P(
                    "Statistically speaking, Jack's odds were grim before "
                    "he ever met the door!",
                    className="chart-quip",
                ),
                html.Iframe(
                    src="https://giphy.com/embed/hEALuPEmdy22lSCyDr",
                    className="chart-gif",
                    title="Titanic door scene GIF",
                ),
                html.P(
                    html.A(
                        "via GIPHY",
                        href="https://giphy.com/gifs/titanicmovie-titanic-movie-25-hEALuPEmdy22lSCyDr",
                        target="_blank",
                        className="inline-link",
                    ),
                    className="gif-credit",
                ),
            ],
            className="chart-card easter-egg",
        ),

        html.Div(
            [
                html.H2("Sex × Passenger Class"),
                html.P(
                    "Looking at sex and passenger class together reveals "
                    "an important interaction."
                ),
                dcc.Graph(id="graph-sex-class"),
            ],
            className="chart-card",
        ),

        html.Div(
            [
                html.H2("Age"),
                html.P(
                    "Children had higher observed survival than most older "
                    "age groups."
                ),
                dcc.Graph(id="graph-survival-by-age"),
            ],
            className="chart-card",
        ),

        html.Div(
            [
                html.H2("Family Size"),
                html.P(
                    "The relationship with survival is not necessarily linear."
                ),
                dcc.Graph(id="graph-survival-by-family"),
            ],
            className="chart-card",
        ),

        page_navigation("/explore"),
    ]
)


@callback(
    Output("graph-survival-by-class", "figure"),
    Output("graph-survival-by-sex", "figure"),
    Output("graph-sex-class", "figure"),
    Output("graph-survival-by-age", "figure"),
    Output("graph-survival-by-family", "figure"),
    Input("theme-store", "data"),
)
def update_charts_theme(theme_mode):

    plotly_template = (
        "plotly_dark"
        if theme_mode == "dark"
        else "plotly"
    )

    bg_color = "rgba(0,0,0,0)"

    survived_color = SURVIVED_COLOR
    non_survived_color = NON_SURVIVED_COLOR
    rate_color = "#B8863B"

    grid_color = (
        "rgba(255,255,255,0.08)"
        if theme_mode == "dark"
        else "rgba(11,22,38,0.08)"
    )

    # =====================================================
    # 1. Passenger Class
    # =====================================================

    class_summary = get_class_summary(df)

    fig_class = go.Figure()

    fig_class.add_trace(
        go.Bar(
            x=class_summary["Ship_Class"],
            y=class_summary["survivors"],
            name="Survived",
            marker_color=survived_color,
        )
    )

    fig_class.add_trace(
        go.Bar(
            x=class_summary["Ship_Class"],
            y=class_summary["non_survivors"],
            name="Did not survive",
            marker_color=non_survived_color,
        )
    )

    fig_class.add_trace(
        go.Scatter(
            x=class_summary["Ship_Class"],
            y=class_summary["total_passengers"] + 15,
            text=[
                f"Total: {total}"
                for total in class_summary["total_passengers"]
            ],
            mode="text",
            showlegend=False,
        )
    )

    fig_class.update_layout(
        barmode="stack",
        title="Passenger Survival Outcomes by Class",
        xaxis_title="Passenger Class",
        yaxis_title="Number of Passengers",
        yaxis=dict(
            range=[
                0,
                class_summary["total_passengers"].max() + 60,
            ],
            gridcolor=grid_color,
        ),
        xaxis=dict(gridcolor=grid_color),
        template=plotly_template,
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        font=dict(family=CHART_FONT),
        legend=dict(orientation="h", y=1.12, x=0),
        margin=dict(t=80),
    )

    # =====================================================
    # 2. Sex
    # =====================================================

    sex_summary = get_sex_summary(df)

    fig_sex = go.Figure()

    fig_sex.add_trace(
        go.Bar(
            x=sex_summary["Sex"],
            y=sex_summary["survivors"],
            name="Survived",
            marker_color=survived_color,
        )
    )

    fig_sex.add_trace(
        go.Bar(
            x=sex_summary["Sex"],
            y=sex_summary["non_survivors"],
            name="Did not survive",
            marker_color=non_survived_color,
        )
    )

    fig_sex.add_trace(
        go.Scatter(
            x=sex_summary["Sex"],
            y=sex_summary["total_passengers"] + 20,
            text=[
                f"Total: {total}"
                for total in sex_summary["total_passengers"]
            ],
            mode="text",
            showlegend=False,
        )
    )

    fig_sex.update_layout(
        barmode="stack",
        title="Passenger Survival Outcomes by Sex",
        xaxis_title="Sex",
        yaxis_title="Number of Passengers",
        yaxis=dict(
            range=[
                0,
                sex_summary["total_passengers"].max() + 70,
            ],
            gridcolor=grid_color,
        ),
        xaxis=dict(gridcolor=grid_color),
        template=plotly_template,
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        font=dict(family=CHART_FONT),
        legend=dict(orientation="h", y=1.12, x=0),
        margin=dict(t=80),
    )

    # =====================================================
    # 3. Sex × Class
    # =====================================================

    sex_class_summary = get_sex_class_summary(df)

    fig_sex_class = go.Figure(
        data=go.Heatmap(
            x=sex_class_summary["Pclass"],
            y=sex_class_summary["Sex"],
            z=sex_class_summary["Survival_Rate"],
            text=sex_class_summary["Survival_Rate"].round(1),
            texttemplate="%{text}%",
            colorscale=[
                [0.0, NON_SURVIVED_COLOR],
                [0.5, "#B8863B"],
                [1.0, SURVIVED_COLOR],
            ],
            zmin=0,
            zmax=100,
            colorbar_title="Survival Rate",
        )
    )

    fig_sex_class.update_layout(
        title="Survival Rate by Sex and Passenger Class",
        xaxis=dict(
            title="Passenger Class",
            tickmode="array",
            tickvals=[1, 2, 3],
            ticktext=[
                "First Class",
                "Second Class",
                "Third Class",
            ],
        ),
        yaxis_title="Sex",
        template=plotly_template,
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        font=dict(family=CHART_FONT),
    )

    # =====================================================
    # 4. Age
    # =====================================================

    age_summary = get_age_summary(df)

    fig_age = go.Figure(
        go.Bar(
            x=age_summary["Age_Category"],
            y=age_summary["Survival_Rate"],
            text=[
                f"{rate:.1f}%"
                for rate in age_summary["Survival_Rate"]
            ],
            textposition="outside",
            name="Survival Rate",
            marker_color=rate_color,
        )
    )

    fig_age.update_layout(
        title="Survival Rate by Age Category",
        xaxis_title="Age Category",
        yaxis_title="Survival Rate",
        yaxis=dict(
            range=[0, 110],
            ticksuffix="%",
            gridcolor=grid_color,
        ),
        xaxis=dict(gridcolor=grid_color),
        template=plotly_template,
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        font=dict(family=CHART_FONT),
    )

    # =====================================================
    # 5. Family Size
    # =====================================================

    family_summary = get_family_summary(df)

    fig_family = go.Figure(
        go.Bar(
            x=family_summary["Family_Size"],
            y=family_summary["Survival_Rate"],
            text=[
                f"{rate:.1f}%"
                for rate in family_summary["Survival_Rate"]
            ],
            textposition="outside",
            name="Survival Rate",
            marker_color=rate_color,
        )
    )

    fig_family.update_layout(
        title="Survival Rate by Family Size",
        xaxis=dict(
            title="Family Size",
            tickmode="linear",
            dtick=1,
            gridcolor=grid_color,
        ),
        yaxis=dict(
            title="Survival Rate",
            range=[0, 110],
            ticksuffix="%",
            gridcolor=grid_color,
        ),
        template=plotly_template,
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        font=dict(family=CHART_FONT),
    )

    return (
        fig_class,
        fig_sex,
        fig_sex_class,
        fig_age,
        fig_family,
    )