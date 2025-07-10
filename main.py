# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

# Constants
num_rows = 2000
account_types = ['Savings', 'Current', 'Salary']
transaction_types = ['Credit', 'Debit']
branch_codes = ['B001', 'B002', 'B003', 'B004', 'B005']

# Generate data
data = {
    'Customer_ID': [fake.uuid4()[:8] for _ in range(num_rows)],
    'Name': [fake.name() for _ in range(num_rows)],
    'Age': np.random.randint(18, 75, num_rows),
    'Gender': [random.choice(['Male', 'Female']) for _ in range(num_rows)],
    'Account_Type': [random.choice(account_types) for _ in range(num_rows)],
    'Account_Balance': np.round(np.random.uniform(1000, 100000, num_rows), 2),
    'Transaction_Date': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_rows)],
    'Transaction_Type': [random.choice(transaction_types) for _ in range(num_rows)],
    'Transaction_Amount': np.round(np.random.uniform(10, 10000, num_rows), 2),
    'Branch_Code': [random.choice(branch_codes) for _ in range(num_rows)],
    'Is_International_Transaction': [random.choice([0, 1]) for _ in range(num_rows)]
}

df = pd.DataFrame(data)

# Introduce some missing values for cleaning tasks
for col in ['Age', 'Account_Balance', 'Transaction_Amount']:
    df.loc[df.sample(frac=0.03).index, col] = np.nan

# Save the dataset
df.to_csv("banking_dataset.csv", index=False)
print("✅ Dataset with 2000 rows saved as 'banking_dataset.csv'")

