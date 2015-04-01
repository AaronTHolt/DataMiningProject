#Aaron Holt
#Data Mining Project
#2015


filename = 'Census2012/e20121co0065000.txt'

with open(filename) as f:
	table_2012_65 = f.readlines()

print len(table_2012_65)
i = 0

for line in table_2012_65:
	print len(line.split(','))
	print line
	i += 1
	if i>2:
		break