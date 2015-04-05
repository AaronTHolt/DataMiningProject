from csv import DictReader, DictWriter
from collections import defaultdict

if __name__ == "__main__":
    
    data = DictReader(open('../KaggleData/2010_final_grade.csv', 'rU'))
    
    output = DictWriter(open('grade_counts.csv', 'w'), ['School_grade', 'EMH', 'Total'], lineterminator='\n')
    output.writeheader()
    
    
    row_counts = 0
    e_grade_counts = defaultdict(int)
    m_grade_counts = defaultdict(int)
    h_grade_counts = defaultdict(int)
    for ii in data:
        if ii['School_Grade']:
            if ii['EMH'] == 'E':
                e_grade_counts[int(ii['School_Grade'])] += 1
            elif ii['EMH'] == 'M':
                m_grade_counts[int(ii['School_Grade'])] += 1
            elif ii['EMH'] == 'H':
                h_grade_counts[int(ii['School_Grade'])] += 1
    e_tot = 0
    m_tot = 0
    h_tot = 0
    
    for bb in xrange(1,14):
        e_tot += e_grade_counts[bb]
        m_tot += m_grade_counts[bb]
        h_tot += h_grade_counts[bb]
        #print bb, e_grade_counts[bb]

    
    for tt in xrange(1,14):
        output.writerow({'School_grade': tt, \
                         'EMH': 'E', \
                        'Total': e_grade_counts[tt]
                        })
        
    for kk in xrange(1,14):
        output.writerow({'School_grade': kk, \
                         'EMH': 'M', \
                        'Total': m_grade_counts[kk]
                        })
        
    for cc in xrange(1,14):
        output.writerow({'School_grade': cc, \
                         'EMH': 'H', \
                        'Total': m_grade_counts[cc]
                        })
        
    output1 = DictWriter(open('counts.csv', 'w'), ['EMH', 'Total'], lineterminator='\n')
    output1.writeheader()
    
    
    output1.writerow({'EMH': 'E', \
                    'Total': e_tot
                    })
    output1.writerow({'EMH': 'M', \
                    'Total': m_tot
                    })
    output1.writerow({'EMH': 'H', \
                    'Total': h_tot
                    })
    
    e_mean = 0.0
    for oo in xrange(1,14):
        e_mean += e_grade_counts[oo]
        #e_mean /= e_tot
    print e_mean
    
    
    
        
    
        