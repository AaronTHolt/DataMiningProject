# Written by Hui Soon Kim

"""
Description     : Data Preprocessing for School Data Analysis
"""
import argparse
import sys
import csv

attributes = ['School Name','EMH',
              'EMH_combined','School_Grade','rank_tot',
	          'Overall_ACH_Grade', 'Read_Ach_Grade','Math_Ach_Grade','Write_Ach_Grade',
	          'Sci_Ach_Grade','Overall_Weighted_Growth_Grade','Read_Growth_Grade', 'Math_Growth_Grade',
	          'Write_Growth_Grade', 'SPF_PS_IND_GRAD_RATE']

def integrate_gps(output_array, reader_object):
    for line in output_array:
        for line2 in reader_object:
			if line["School Name"].upper() == line2["School Name"].upper():
				line["Lattitude"] = line2["Lattitude"]
				line["Longitude"] = line2["Longitude"]
				break
			else:
				line["Lattitude"] = ''
				line["Longitude"] = ''
    attributes.append('Lattitude')
    attributes.append("Longitude")

def integrate_zip(output_array, reader_object):
    for line in output_array:
        for line2 in reader_object:
			if line["School Name"].upper() == line2["School Name"].upper():
				line["Physical Zipcode"] = line2["Physical Zipcode"]
				break
			else:
				line["Physical Zipcode"] = ''
    attributes.append('Physical Zipcode')

def integrate_enroll(output_array, reader_object):
    for line in output_array:
        for line2 in reader_object:
			if line["School Name"].upper() == line2["School Name"].upper():
				line["Enrol_TOT"] = line2["TOTAL"]
				line["PCT_AmInd"] = line2["PCT_AmInd"]
				line["PCT_Asian"] = line2["PCT_Asian"]
				line["PCT_Black"] = line2["PCT_Black"]
				line["PCT_hisp"] = line2["PCT_hisp"]
				line["PCT_White"] = line2["PCT_White"]
				line["PCT_PI"] = line2["PCT_PI"]
				line["PCT_2ormore"] = line2["PCT_2ormore"]
				break
			else:
				line["Enrol_TOT"] = ''
				line["PCT_AmInd"] = ''
				line["PCT_Asian"] = ''
				line["PCT_Black"] = ''
				line["PCT_hisp"] = ''
				line["PCT_White"] = ''
				line["PCT_PI"] = ''
				line["PCT_2ormore"] = ''
    attributes.append('Enrol_TOT')
    attributes.append('PCT_AmInd')
    attributes.append('PCT_Asian')
    attributes.append('PCT_Black')
    attributes.append('PCT_hisp')
    attributes.append('PCT_White')
    attributes.append('PCT_PI')
    attributes.append('PCT_2ormore')

def integrate_freemeal(output_array, reader_object):
    for line in output_array:
        for line2 in reader_object:
			if line["School Name"].upper() == line2["SCHOOL NAME"].upper():
				line["PCT_FREE_MEAL"] = line2["FREE AND REDUCED"]
				break
			else:
				line["PCT_FREE_MEAL"] = ''
    attributes.append('PCT_FREE_MEAL')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Preprocessing')
    parser.add_argument("--f_grade",   help="Final_grade_filename",
                           type=str, required=True)
    parser.add_argument("--f_gps",     help="school_gps",
                           type=str, required=False)
    parser.add_argument("--f_add",     help="school_address",
                           type=str, required=False)
    parser.add_argument("--f_enroll",  help="enrl_working",
                           type=str, required=False)
    parser.add_argument("--f_frl",     help="FRL",
                           type=str, required=False)
                           
    args = parser.parse_args()

    # Open and Cast to list to keep it all in memory    
    csv_grade = list(csv.DictReader(open(args.f_grade, 'rU')))
    # Output array : Base =  csv_grade(Copy of grade)
    output_array = csv_grade[:] 


    if(args.f_gps != None):
		csv_gps = list(csv.DictReader(open(args.f_gps, 'rU')))
		integrate_gps(output_array, csv_gps)
    if(args.f_add != None):
		csv_add = list(csv.DictReader(open(args.f_add, 'rU')))
		integrate_zip(output_array, csv_add)
    if(args.f_enroll != None):
		csv_enroll = list(csv.DictReader(open(args.f_enroll, 'rU')))
		integrate_enroll(output_array, csv_enroll)
    if(args.f_frl != None):
		csv_frl = list(csv.DictReader(open(args.f_frl, 'rU')))
		integrate_freemeal(output_array, csv_frl)


    # Write PreProcessed Data..sss
    output_file = open('processed.csv','wb')
    csvwriter = csv.DictWriter(output_file, delimiter=',', fieldnames=attributes)
    csvwriter.writeheader()

    for row in output_array:
		csvwriter.writerow(row)
    output_file.close()
				
    
            
            
            

