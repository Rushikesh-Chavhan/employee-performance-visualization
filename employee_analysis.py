import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io, base64

# --------------------------
# Employee performance dataset
# --------------------------
df = pd.read_csv("employees_dataset.csv")

# --------------------------
# Frequency count for HR dept
# --------------------------
hr_count = df[df["Department"] == "HR"].shape[0]
print("Frequency count for HR department:", hr_count)

# --------------------------
# Create histogram
# --------------------------
plt.figure(figsize=(6, 6))
sns.countplot(data=df, x="Department", hue="Department", palette="muted", legend=False)
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Count")


# Save plot to base64
buf = io.BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
img_base64 = base64.b64encode(buf.read()).decode("utf-8")
buf.close()

# --------------------------
# Embed everything into HTML
# --------------------------
python_code = """\
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io, base64

data = {
    "EmployeeID": range(1, 101),
    "Department": ["HR", "Finance", "IT", "Sales", "Marketing"] * 20,
    "Region": ["North", "South", "East", "West", "Central"] * 20,
    "PerformanceScore": [75, 82, 90, 88, 79, 85, 92, 77, 81, 89] * 10
}

df = pd.DataFrame(data)
hr_count = df[df["Department"] == "HR"].shape[0]
print("Frequency count for HR department:", hr_count)

plt.figure(figsize=(6, 6))
sns.countplot(data=df, x="Department", palette="muted")
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()
"""

html_content = f"""
<html>
<head><title>Employee Distribution</title></head>
<body>
<h2>Employee Department Distribution</h2>
<p>Email for verification: 24f3002795@ds.study.iitm.ac.in</p>
<p>Frequency count for HR department: {hr_count}</p>

<h3>Visualization</h3>
<img src="data:image/png;base64,{img_base64}" />

<h3>Python Code Used</h3>
<pre>
{python_code}
</pre>
</body>
</html>
"""

with open("employee_distribution.html", "w") as f:
    f.write(html_content)
