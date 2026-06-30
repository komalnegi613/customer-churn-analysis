import pandas as pd

df = pd.read_csv("C:/Users/Dell/Desktop/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Loaded Successfully!")
print(df.head())

print("\nRows and Columns:")
print(df.shape)

print("\nChurn Count:")
print(df['Churn'].value_counts())

print("\nChurn Percentage:")
churn_percentage = (df['Churn'].value_counts(normalize=True) * 100)
print(churn_percentage)



import matplotlib.pyplot as plt

df['Churn'].value_counts().plot(kind='bar')

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x='gender', hue='Churn')
plt.title('Gender vs Churn')
plt.show()


print("GENDER GRAPH RUNNING")

import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Test Graph")
plt.show()

print("Program Finished")


sns.boxplot(data=df, x='Churn', y='MonthlyCharges')
plt.title('Monthly Charges vs Churn')
plt.show()