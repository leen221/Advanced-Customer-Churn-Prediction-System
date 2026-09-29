# Telco Customer Churn Prediction

## Project Overview

This project uses machine learning to predict whether a telecom customer is likely to churn.

The project focuses on building a binary classification model using **Logistic Regression**, while exploring data preprocessing, feature selection, model evaluation, and class imbalance.

## Objective

The objective is to understand the machine learning workflow from preparing the data to training and evaluating a classification model.

## Dataset

The project uses the **Telco Customer Churn** dataset, which contains information about telecom customers and whether they churned.

### Selected Features

The model uses the following features:

* `SeniorCitizen`
* `Partner`
* `Dependents`
* `tenure`
* `MonthlyCharges`
* `InternetService`

`InternetService` was converted into multiple binary features using one-hot encoding.

The `customerID` column was removed because it is an identifier and does not provide useful predictive information for the model.

## Data Preprocessing

The dataset was prepared by:

* Converting `Churn` from `Yes/No` to `1/0`
* Converting `Partner` and `Dependents` from `Yes/No` to `1/0`
* Applying one-hot encoding to `InternetService`
* Removing `customerID`, `gender`, and `TotalCharges`
* Selecting a limited number of features for the model

## Model

The model used in this project is **Logistic Regression**.

Since the target variable has two possible outcomes (`0` or `1`), this is a **binary classification** problem.

The dataset was split into:

* 70% training data
* 30% testing data

## Model Evaluation

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### Final Results

To handle the imbalance between the two classes, I used:

`class_weight='balanced'`

The final model achieved:

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 74.82% |
| Precision | 52.42% |
| Recall    | 79.09% |
| F1 Score  | 63.06% |

### Confusion Matrix

```text
[[1127  412]
 [ 120  454]]
```

The model correctly identified **454 customers who churned**, while **120 churned customers were incorrectly predicted as non-churned**.

Using `class_weight='balanced'` increased the model's ability to detect the minority class (`Churn = 1`), resulting in a recall of **79.09%**.

However, this improvement came with a decrease in precision and accuracy, showing the trade-off between different classification metrics.

## What I Learned

Through this project, I practiced:

* Loading and exploring a real-world dataset
* Feature selection
* Data preprocessing
* One-hot encoding
* Train/test splitting
* Binary classification
* Logistic Regression
* Accuracy, Precision, Recall, and F1 Score
* Confusion matrices
* False Positives and False Negatives
* Class imbalance
* Using `class_weight='balanced'`
* Comparing model experiments

## Technologies & Libraries

* Python
* Pandas
* Scikit-learn
* Logistic Regression
* Git & GitHub

## Project Structure

```text
Telco-Customer-Churn-Prediction/
│
├── code.py
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
└── README.md
```

## Limitations

This is an introductory machine learning project, so only a limited number of features were used.

The model is not intended to be a production-ready customer churn prediction system.

Future improvements could include:

* Testing additional relevant features
* Feature scaling
* Comparing different classification models
* Further analysis of model errors
* Hyperparameter tuning
