import json
import csv

f = open("UKdata.json")
data = json.load(f)
f.close()
f = open("UKJobsdata.csv","w", encoding='utf-8')
csv_file = csv.writer(f)
for item in data:
	csv_file.writerow([item["title"], item["company"], item["city"], item["bin"],str(item["JD"]), item["url"]])
f.close()