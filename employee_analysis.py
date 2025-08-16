import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("employees_dataset.csv")

# Calculate frequency count for HR department
hr_count = (df["Department"] == "HR").sum()
print("Number of employees in HR:", hr_count)

# Create interactive histogram
fig = px.histogram(df, x="Department", title="Distribution of Employees by Department")

# Save as HTML
fig.write_html("employee_distribution.html")
