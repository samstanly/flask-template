import json

with open("report.json","r") as f:
    data=json.loads(f.read())

for report in data:
    if "avalanche_score" not in report:
        print(report)
