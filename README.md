## Model Evaluation

The Logistic Regression model was evaluated using:

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

The `class_weight='balanced'` setting increased the model's ability to detect the minority class (`Churn = 1`), resulting in a recall of **79.09%**.

However, this improvement came with a decrease in precision and accuracy, showing the trade-off between different classification metrics.
