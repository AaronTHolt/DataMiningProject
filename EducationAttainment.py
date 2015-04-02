#Aaron Holt
#Data Mining Project
#2015

import csv
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


#Education Attainment 25+ DATA
filename = 'Census2012/e20121co0065000.txt'

with open(filename) as f:
	table_2012_65 = f.readlines()

Edu25Data=[]
i = 0
for line in table_2012_65:
	# print len(line.split(','))
	#Columns 12-22 are counties from the g20121co file
	if i>=12 and i<=22:
		line = line.split(',')
		#lines 7-32 are education attainment for 25+
		#the census data starts at 1 instead of 0, so use 6-31
		# print line[6:31]
		Edu25Data.append(line[6:31])
	i += 1
	if i>22:
		break
for rr in range(0,len(Edu25Data)):
	for cc in range(0,len(Edu25Data[rr])):
		if cc>0:
			Edu25Data[rr][cc]=float(Edu25Data[rr][cc])/float(Edu25Data[rr][0])*100.0

#Lookup table to get column names
filename = 'Census2012/Lookup2012.txt'

with open(filename) as f:
	columnInfo = f.readlines()


#EducationAttainment 25+ column labelings
columns = []
cIndex = []
i = 0
for line in columnInfo:
	line = line.split(',')
	#table number
	if line[1] == 'B15003':
		if line[3] != ' ':
			#7th column in lookup for this table is education attainment
			columns.append(line[7])
			cIndex.append(i)
			i += 1

# print columns

#Lookup table to get row info
filename = 'Census2012/g20121co.csv'
i=0
rows=[]
rIndex=[]
with open(filename) as f:
	rowInfo = f.readlines()

for line in rowInfo:
	line=line.split(',')
	#50 is county code
	# print line[2]
	if line[2] == '050':
		# print len(line)
		# print line[49]
		rows.append(line[49])
		rIndex.append(i)
		i += 1

# print rows
# print columns
# print cIndex
# print Edu25Data[0]

def listmaker(n, length):
	listofn = [n] * length
	return listofn

#plot county data!
#First plot has 2 counties
plt.gcf().subplots_adjust(bottom=0.25)
mpl.rcParams['axes.color_cycle'] = ['r', 'b', 'm', 'y', 'k', 'c']

line0, =plt.plot(cIndex, Edu25Data[0], 'bo')
line1, =plt.plot(cIndex, Edu25Data[1], 'ro')

plt.ylabel('Percent of population in county')
plt.ylim([0,40])
# plt.yticks(rIndex, rows)
plt.xlabel('Number attaining education level')
plt.xticks(cIndex[1:], columns[1:], rotation='vertical')
plt.title('Education attainment of couties in Colorado')
plt.legend([line0, line1], [rows[0], rows[1]])

plt.show()

plt.gcf().subplots_adjust(bottom=0.25)

lines=[]
# for ii in range(0,len(rows)):   #all counties
for ii in range(0,6):  #6 counties
	var = 'line'+str(ii)
	var, = plt.plot(cIndex, Edu25Data[ii], 'o')
	lines.append(var)
plt.ylabel('Percent of population in county')
plt.ylim([0,40])
# plt.yticks(rIndex, rows)
plt.xlabel('Number attaining education level')
plt.xticks(cIndex[1:], columns[1:], rotation='vertical')
plt.title('Education attainment of couties in Colorado')
plt.legend([line for line in lines], [row for row in rows], loc=2)
plt.show()


print "DONE"



##########################################################
#HW2 EXAMPLE CODE
##################################
	# #Plot1
	# line1, =plt.plot(day1, high1, 'r--')
	# line2, =plt.plot(day1, low1, 'b--')
	# plt.xlabel('Day')
	# plt.ylabel("Price ($)")
	# plt.title('High and Low Price versus Day in HD Stock')
	# plt.legend([line1, line2], ["High", "Low"])
	# plt.show()

	# #Plot2
	# data= [open1,close1]
	# boxplot(data)
	# xticks([1,2],['Open','Close'])
	# plt.ylabel("Price ($)")
	# plt.title('Boxplot of Opening and Closing Prices in HD Stock')
	# plt.show()

	# #Plot3
	# plt.hist(volume1, 10,histtype='bar')
	# plt.ylabel("Frequency")
	# plt.xlabel("Volume")
	# plt.title('Frequency of Volume in HD Stock')
	# plt.show()

	# #Plot4
	# line1, =plt.plot(day1, high1, 'r--')
	# line2, =plt.plot(day1, close1, 'b--')
	# plt.xlabel('Day')
	# plt.ylabel("Price ($)")
	# plt.title('High and Close Price versus Day in HD Stock')
	# plt.legend([line1, line2], ["High", "Close"])
	# plt.show()