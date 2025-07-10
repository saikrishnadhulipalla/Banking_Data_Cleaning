# 🏦 Banking Dataset Project

This project simulates and processes a synthetic banking transaction dataset using Python. It involves data generation, cleaning, and preparation for analytics or machine learning tasks.


## 📁 Project Structure


---

## 🧪 Data Description

The dataset includes ~2000 rows with the following features:

- `Customer_ID`: Unique identifier
- `Name`: Full name of customer
- `Age`: Customer’s age
- `Gender`: Male or Female
- `Account_Type`: [Savings, Current, Salary]
- `Account_Balance`: Current balance
- `Transaction_Date`: Date of transaction
- `Transaction_Type`: [Credit, Debit]
- `Transaction_Amount`: Amount credited or debited
- `Branch_Code`: Branch identifier (e.g., B001)
- `Is_International_Transaction`: Binary indicator (0 = No, 1 = Yes)

---

## 🧹 Cleaning Performed

- Filled missing values using **median** strategy for numeric fields.
- Converted `Transaction_Date` to proper datetime format.
- Removed any **duplicate records**.
- Reset index and saved the cleaned dataset.

---

## 🚀 How to Run

1. Clone the repo (or download the project)
2. Activate your virtual environment
3. Install requirements:

```bash
pip install pandas faker numpy