def get_overall_survival(df):
    return df["Survived"].mean()


def get_class_summary(df):
    summary = (
        df.groupby("Pclass")
        .agg(
            survivors=("Survived", "sum"),
            total_passengers=("Survived", "count"),
        )
        .reset_index()
    )

    summary["non_survivors"] = (
        summary["total_passengers"] - summary["survivors"]
    )

    summary["Ship_Class"] = summary["Pclass"].map(
        {
            1: "First Class",
            2: "Second Class",
            3: "Third Class",
        }
    )

    return summary


def get_sex_summary(df):
    summary = (
        df.groupby("Sex")
        .agg(
            survivors=("Survived", "sum"),
            total_passengers=("Survived", "count"),
        )
        .reset_index()
    )

    summary["non_survivors"] = (
        summary["total_passengers"] - summary["survivors"]
    )

    return summary


def get_sex_class_summary(df):
    summary = (
        df.groupby(["Pclass", "Sex"])["Survived"]
        .mean()
        .reset_index()
    )

    summary["Survival_Rate"] = summary["Survived"] * 100

    return summary[
        [
            "Pclass",
            "Sex",
            "Survival_Rate",
        ]
    ]


def get_age_summary(df):
    summary = (
        df.groupby("Age_Category", observed=True)["Survived"]
        .mean()
        .reset_index()
    )

    summary["Survival_Rate"] = summary["Survived"] * 100

    return summary[
        [
            "Age_Category",
            "Survival_Rate",
        ]
    ]


def get_family_summary(df):
    summary = (
        df[df["Family_Size"] <= 7]
        .groupby("Family_Size")["Survived"]
        .mean()
        .reset_index()
    )

    summary["Survival_Rate"] = summary["Survived"] * 100

    return summary[
        [
            "Family_Size",
            "Survival_Rate",
        ]
    ]