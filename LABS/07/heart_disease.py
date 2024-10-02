import pandas as pd

data = pd.read_csv("/heart.csv")
data=data.rename(columns={'sex':"gender"})

data['gender'] = data['gender'].replace({1: "male", 0: "female"})

print(data.head())
print(data[['chol','trestbps', 'oldpeak']].mean())
print(data[['chol','trestbps', 'oldpeak']].median())
print(data[['chol','trestbps', 'oldpeak']].mode())
