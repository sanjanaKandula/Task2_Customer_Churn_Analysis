import pandas as pd

# Load dataset
df = pd.read_csv("customer_data.csv")

print("===== CUSTOMER CHURN ANALYSIS =====")
print(df.head())

# Basic Information
print("\nDataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Values
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# Churn Statistics
if "Churn" in df.columns:

    churn_count = df["Churn"].value_counts()

    print("\nChurn Distribution:")
    print(churn_count)

    churn_percentage = (churn_count / len(df)) * 100

    print("\nChurn Percentage:")
    print(churn_percentage)

# Average Tenure by Churn
if "Tenure" in df.columns and "Churn" in df.columns:

    tenure_analysis = df.groupby("Churn")["Tenure"].mean()

    print("\nAverage Tenure:")
    print(tenure_analysis)

# Monthly Charges Analysis
if "MonthlyCharges" in df.columns and "Churn" in df.columns:

    charge_analysis = df.groupby("Churn")["MonthlyCharges"].mean()

    print("\nAverage Monthly Charges:")
    print(charge_analysis)

# Save Summary Report
summary = pd.DataFrame({
    "Total_Customers": [len(df)],
    "Churned_Customers": [len(df[df["Churn"] == "Yes"])] if "Churn" in df.columns else [0]
})

summary.to_csv("churn_analysis_report.csv", index=False)

print("\nAnalysis Completed Successfully!")
print("Report saved as churn_analysis_report.csv")