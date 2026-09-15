from functools import lru_cache
from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "picker_pipeline.pkl"


@lru_cache(maxsize=1)
def load_model():
    """
    Load the trained model pipeline once per application process.
    """

    return joblib.load(MODEL_PATH)


def predict_survival(
    pclass,
    sex,
    age,
    embarked,
    sibsp,
    parch,
):
    """
    Build a passenger profile and generate a survival prediction.
    """

    family_size = sibsp + parch + 1
    is_alone = family_size == 1

    passenger = pd.DataFrame(
        [
            {
                "pclass": pclass,
                "sex": sex,
                "age": age,
                "embarked": embarked,
                "family_size": family_size,
                "is_alone": is_alone,
            }
        ]
    )

    pipeline = load_model()

    prediction = pipeline.predict(passenger)[0]

    probabilities = pipeline.predict_proba(passenger)[0]

    survival_probability = probabilities[1]

    return {
        "prediction": int(prediction),
        "survival_probability": float(survival_probability),
        "family_size": int(family_size),
        "is_alone": bool(is_alone),
    }