import pandas as pd

data = {
    'employee_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'department': ['HR', 'Engineering', 'Engineering', 'Marketing', 'HR', 'Marketing'],
    'salary': [60000, 80000, 85000, 90000, 75000, 88000]
}

df = pd.DataFrame(data)

# Step 2: Compute average salary grouped by department
avg_salary_df = df.groupby('department', as_index=False)['salary'].mean()

# Step 3: Sort by average salary in descending order
avg_salary_df = avg_salary_df.sort_values(by='salary', ascending=False)

# Step 4: Display the result
print("Average Salary by Department (Descending Order):")
print(avg_salary_df)
