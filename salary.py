import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  
db = client["companyDB"]        # database name
collection = db["employees"]    # collection name

data = list(collection.find({}, {"_id": 0})) 
df = pd.DataFrame(data)

if df.empty:
    print("No employee records found in the database.")
else:
    avg_salary = df.groupby("department")["salary"].mean().reset_index()

    avg_salary = avg_salary.sort_values(by="salary", ascending=False)

    print("\nAverage Salary by Department (Descending):\n")
    print(avg_salary)
