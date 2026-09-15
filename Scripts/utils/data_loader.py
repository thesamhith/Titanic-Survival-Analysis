from functools import lru_cache
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "titanic.csv"


@lru_cache(maxsize=1)
def load_titanic_data():
    """
    Load and prepare the Titanic dataset.

    The result is cached so the CSV is only read once
    per application process.
    """

    df = pd.read_csv(DATA_PATH)

    # Fill missing Age values using the dataset median.
    df["Age"] = df["Age"].fillna(df["Age"].median())

    # Feature engineering used by the analysis.
    df["Family_Size"] = df["SibSp"] + df["Parch"] + 1

    df["Age_Category"] = pd.cut(
        df["Age"],
        bins=[-float("inf"), 12, 25, 60, float("inf")],
        labels=["Child", "Youth", "Adult", "Senior"],
    )

    return df


def get_data():
    """
    Return a copy of the prepared Titanic dataset.

    Returning a copy prevents individual pages or callbacks
    from accidentally mutating the cached dataframe.
    """

    return load_titanic_data().copy()