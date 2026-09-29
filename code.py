import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix

data_csv= pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
#print(data_csv)
#print(pd.isna(data_csv).sum())
data_csv['Churn']=data_csv['Churn'].map({'Yes':1,"No":0})

data_csv['Partner']=data_csv['Partner'].map({'Yes':1,"No":0})

data_csv['Dependents']=data_csv['Dependents'].map({'Yes':1,"No":0})
data_csv = pd.get_dummies(data_csv, columns=['InternetService'], dtype=int)
data_csv=data_csv.drop(columns=['customerID', 'gender', 'TotalCharges'])
x = data_csv[
    [
        'SeniorCitizen',
        'Partner',
        'Dependents',
        'tenure',
        'MonthlyCharges',
        'InternetService_DSL',
        'InternetService_Fiber optic',
        'InternetService_No'
    ]
]
y=data_csv['Churn']
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=42)

model=LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
print("accuracy",accuracy)
print("precision",precision)
print("recall",recall)
print("f1",f1)
cm = confusion_matrix(y_test, y_pred)

print(cm)
print(y.value_counts())