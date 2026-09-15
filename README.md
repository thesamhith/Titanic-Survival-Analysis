# Titanic Survival Analysis

An exploratory data analysis and machine learning project examining the factors associated with passenger survival aboard the RMS Titanic.

The project combines **exploratory analysis, feature engineering, logistic regression, and an interactive Dash application** that allows users to explore the dataset and estimate survival probability for a passenger profile.

## Project Question

**Which passenger characteristics were most strongly associated with survival?**

Rather than treating the Titanic dataset as a historical record of every passenger aboard, this project uses the available Kaggle training dataset to explore patterns in survival and demonstrate a complete beginner-level machine learning workflow.

## Key Findings

The analysis highlights several strong patterns:

- **Sex was strongly associated with survival**, with female passengers having substantially higher observed survival rates than male passengers.
- **Passenger class mattered significantly**, with first-class passengers showing higher survival rates than passengers in lower classes.
- **Sex and passenger class together revealed an important interaction** — survival patterns differed considerably between men and women within each class.
- **Age showed some variation in survival**, particularly between children and older age groups.
- **Family size showed a non-linear relationship with survival**, suggesting that travelling with some family members may have been advantageous, while very large family groups did not necessarily have the same benefit.

These are associations observed in the dataset, not claims of causation.

## Machine Learning Model

The project uses **logistic regression** to estimate the probability of survival.

### Features

The model uses:

- Passenger class (`Pclass`)
- Sex
- Age
- Port of embarkation (`Embarked`)
- Family size
- Whether the passenger was travelling alone

`Family_Size` is derived from:

```text
SibSp + Parch + 1
```

`Is_Alone` is derived from whether family size equals 1.

The trained preprocessing and logistic regression workflow is saved as:

```text
models/picker_pipeline.pkl
```

The model achieved approximately **79% accuracy on the held-out test data**.

Accuracy is reported as a simple evaluation metric for this introductory project; it is not intended to imply that the model can reliably predict the outcome of an individual historical passenger.

## Interactive Dash App

The project includes a multi-page **Dash application** with four sections:

### Home

Introduces the project, dataset, analytical approach, and model.

### Explore the Data

Interactive visualisations examine survival patterns across:

- Passenger class
- Sex
- Sex × passenger class
- Age category
- Family size

The charts respond to the application's light/dark theme.

### Predict Survival

Users can enter a passenger profile and receive:

- Predicted outcome
- Estimated survival probability
- Calculated family size
- Whether the passenger is travelling alone

The application also validates required inputs before making a prediction.

### Conclusions

Summarises the main analytical findings and limitations of the project.

## Project Structure

```text
Titanic_Analysis/
│
├── Scripts/
│   ├── app.py
│   ├── pages/
│   │   ├── home.py
│   │   ├── explore.py
│   │   ├── model.py
│   │   └── conclusions.py
│   │
│   ├── data/
│   │   └── titanic.csv
│   │
│   └── models/
│       └── picker_pipeline.pkl
│
├── Notebook/
│   └── Titanic_Analysis.ipynb
│
├── pyproject.toml
├── uv.lock
├── README.md
└── .python-version
```

## Run Locally

This project uses **uv** for Python environment and dependency management.

From the project root:

```bash
uv sync
```

Then launch the Dash application:

```bash
uv run python Scripts/app.py
```

The application will be available at the local address shown in the terminal.

## Data

The project uses the Kaggle Titanic training dataset containing **891 passenger records**.

The dataset is a sample used for machine learning and analysis rather than a complete historical manifest of everyone aboard the Titanic.

Missing values are handled as follows:

- Missing `Age` values are filled using the median age.
- Missing `Embarked` values are filled using the mode.
- A `Cabin_Known` indicator is retained because the original cabin field contains substantial missing data.

These preprocessing decisions are documented in the analysis notebook.

## Limitations

This project is intended as a portfolio demonstration of exploratory analysis and introductory machine learning.

The model:

- learns from a relatively small historical dataset;
- captures associations present in the available data rather than causal relationships;
- should not be interpreted as a historically accurate reconstruction of individual survival decisions;
- uses accuracy as its primary evaluation metric rather than presenting the model as a production-grade prediction system.

## Try the App

**Live application:**  
_Add Plotly Cloud URL here after deployment._

## Technologies

- Python
- pandas
- NumPy
- Plotly
- Dash
- scikit-learn
- Jupyter
- uv
- Git / GitHub
