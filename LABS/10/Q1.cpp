import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a = pd.read_csv('diabetes.csv')
print(a.info())
print(a.describe())

outcome_counts = a['Outcome'].value_counts()
label = ["Non-Diabetic", "Diabetic"]
colors = ["pink", "lightblue"]

plt.figure(figsize=(8, 6))
plt.pie(outcome_counts, labels=label, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Diabetes Outcomes Distribution')
plt.axis('equal')
plt.show()

plt.figure(figsize=(15, 12))
for i, column in enumerate(a.columns[:-1], 1):
    plt.subplot(3, 3, i)
    sns.histplot(a[column], kde=True, bins=20, color="skyblue")
    plt.title(f'Distribution of {column}')
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 12))
for i, column in enumerate(a.columns, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(y=a[column], color="lightcoral")
    plt.title(f'Boxplot of {column}')
plt.tight_layout()
plt.show()

sns.pairplot(a, hue='Outcome', palette="Set2")
plt.suptitle("Pairwise Scatterplots (colored by Outcome)", y=1.02)
plt.show()

plt.figure(figsize=(10, 8))
corr_matrix = a.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Heatmap')
plt.show()

features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
            'Insulin', 'BMI', 'DiabetesPedigreeFunction']

plt.figure(figsize=(15, 20))
for i, feature in enumerate(features, 1):
    plt.subplot(4, 2, i)
    sns.scatterplot(x=a[feature], y=a['Age'], hue=a['Outcome'], palette="Set1")
    plt.title(f'{feature} vs Age')
    plt.xlabel(feature)
    plt.ylabel('Age')
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.boxplot(x='Outcome', y='BMI', data=a, palette="pastel")
plt.title('BMI Across Diabetes Outcomes')

plt.subplot(1, 2, 2)
sns.boxplot(x='Outcome', y='Glucose', data=a, palette="pastel")
plt.title('Glucose Across Diabetes Outcomes')

plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(x='Glucose', y='BMI', hue='Outcome', data=a, palette="husl")
plt.title('Scatter Plot: Glucose vs BMI')
plt.xlabel('Glucose')
plt.ylabel('BMI')
plt.show()
