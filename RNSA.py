import csv

# Path to the Nessus CSV report
report_path = "path_to_nessus_report.csv"

# Dictionary to store vulnerability count by severity
vulnerability_counts = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0, "Info": 0}

# Read the CSV report
with open(report_path, 'r') as report_file:
    reader = csv.DictReader(report_file)
    for row in reader:
        severity = row["Severity"]
        vulnerability_counts[severity] += 1

# Print the results
for severity, count in vulnerability_counts.items():
    print(f"{severity}: {count} vulnerabilities")

