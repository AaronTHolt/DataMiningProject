from csv import DictReader, DictWriter
from collections import defaultdict

if __name__ == "__main__":
    
    data = DictReader(open('../KaggleData/2010_final_grade.csv', 'rU'))
    
    output = DictWriter(open('overall_grade_counts.csv', 'w'), ['School_grade', 'Total'], lineterminator='\n')
    output.writeheader()
    
    
    row_counts = 0

    grade_counts = defaultdict(int)
    for ii in data:
        if ii['School_Grade']:
            grade_counts[int(ii['School_Grade'])] += 1
    
    tot = 0
    
    for bb in xrange(1,14):
        tot += grade_counts[bb]
        #print bb, e_grade_counts[bb]

    
    for tt in xrange(1,14):
        output.writerow({'School_grade': tt, \
                        'Total': grade_counts[tt]
                        })
    
    
    
    print tot
    
        