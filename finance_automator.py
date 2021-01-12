

import csv
import json

with open('export.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print("skipped")
		else:
			if len(row) > 0:
				date = datetime.datetime.strptime(row[0], "%Y-%M-%d").date()
				