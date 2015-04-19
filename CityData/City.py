import csv
import re
import matplotlib
from csv import DictReader, DictWriter

# locations = DictReader(open('2012_school_address.csv', 'rU'))

# location_data = {}

# for ii in locations:
# 	# print ii
# 	location_data[ii['School Name']] = [ii['Physical City'], ii['Physical Zipcode'],
# 									ii['Physical Address']]

# with open('2012pp.csv', 'rb') as data, open('2012pp2.csv', 'wb') as newdata:
# 	csvreader = csv.DictReader(data)
# 	print csvreader.fieldnames
# 	fieldnames = csvreader.fieldnames + ['City'] + ['Zipcode'] + \
# 										 ['Address']

# 	csvwriter = csv.DictWriter(newdata, fieldnames)
# 	csvwriter.writeheader()
# 	for row in csvreader:
# 		# print row
# 		name = re.sub("'","",row['School_Name'])
# 		print name
# 		row['City'] = location_data[name][0]
# 		row['Zipcode'] = location_data[name][1]
# 		row['Address'] = location_data[name][2]

# 		# print row
# 		csvwriter.writerow(row)



# with open('2012pp2.csv', 'rb') as data, open('Denver.csv', 'wb') as newdata:
# 	csvreader = csv.DictReader(data)
# 	fieldnames = csvreader.fieldnames
# 	csvwriter = csv.DictWriter(newdata, fieldnames)
# 	csvwriter.writeheader()
# 	for row in csvreader:
# 		if row['City'] == 'DENVER':
# 			csvwriter.writerow(row)

# with open('2012pp2.csv', 'rb') as data, open('CoSprings.csv', 'wb') as newdata:
# 	csvreader = csv.DictReader(data)
# 	fieldnames = csvreader.fieldnames
# 	csvwriter = csv.DictWriter(newdata, fieldnames)
# 	csvwriter.writeheader()
# 	for row in csvreader:
# 		if row['City'] == 'COLORADO SPRINGS':
# 			csvwriter.writerow(row)

# with open('2012pp2.csv', 'rb') as data, open('Boulder.csv', 'wb') as newdata:
# 	csvreader = csv.DictReader(data)
# 	fieldnames = csvreader.fieldnames
# 	csvwriter = csv.DictWriter(newdata, fieldnames)
# 	csvwriter.writeheader()
# 	for row in csvreader:
# 		if row['City'] == 'BOULDER':
# 			csvwriter.writerow(row)

with open('2012pp2.csv', 'rb') as data, open('Pueblo.csv', 'wb') as newdata:
	csvreader = csv.DictReader(data)
	fieldnames = csvreader.fieldnames
	csvwriter = csv.DictWriter(newdata, fieldnames)
	csvwriter.writeheader()
	for row in csvreader:
		if row['City'] == 'PUEBLO':
			csvwriter.writerow(row)

with open('2012pp2.csv', 'rb') as data, open('GrandJunc.csv', 'wb') as newdata:
	csvreader = csv.DictReader(data)
	fieldnames = csvreader.fieldnames
	csvwriter = csv.DictWriter(newdata, fieldnames)
	csvwriter.writeheader()
	for row in csvreader:
		if row['City'] == 'GRAND JUNCTION':
			csvwriter.writerow(row)