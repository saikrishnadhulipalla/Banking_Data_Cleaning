import pandas as pd

# Load the dataset
df = pd.read_csv("banking_dataset.csv")

# 1. Check null values
print("Null values:\n", df.isnull().sum())

# 2. Fill missing values using best practice (no inplace=True)clean_banking _data.pyclean
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Account_Balance'] = df['Account_Balance'].fillna(df['Account_Balance'].median())
df['Transaction_Amount'] = df['Transaction_Amount'].fillna(df['Transaction_Amount'].median())
# 3. Convert transaction date to datetime
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])

# 4. Remove duplicates (if any)
df = df.drop_duplicates()

# 5. Reset index
df = df.reset_index(drop=True)

# 6. Save cleaned dataset
df.to_csv("banking_dataset_cleaned.csv", index=False)

print("✅ Data cleaned and saved as 'banking_dataset_cleaned.csv'")