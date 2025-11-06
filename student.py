import pymongo
import pandas as pd
import matplotlib.pyplot as plt

def plot_average_grades_per_subject(mongo_uri, db_name, collection_name):
    client = pymongo.MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    data = list(collection.find())
    if not data:
        print("No data found in the collection.")
        return

    df = pd.DataFrame(data)

    if 'subject' not in df.columns or 'grade' not in df.columns:
        print("Missing required fields: 'subject' and 'grade'")
        return

    avg_grades = df.groupby('subject')['grade'].mean().sort_values()

    avg_grades.plot(kind='bar')
    plt.title('Average Grades per Subject')
    plt.xlabel('Subject')
    plt.ylabel('Average Grade')
    

