# converts the Excel file provided by Appraisal Systems to a CSV suitable for us in QGIS, Pandas, etc.
# http://www.asinj.com/revaluation.asp?p=current&id=359
# Anthony Townsend v 0.1 10 may 2018

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('infile', help="Excel file from Appraisal Systems")
parser.add_argument('outfile', help="CSV file to write")
args = parser.parse_args()

print ('infile: %s' % args.infile)
print ('outfile: %s' % args.outfile)


# 1. convert XLS to CSV

import pandas as pd
data_xls = pd.read_excel(args.infile, 'released as of April 18th', index_col=None)
data_xls.to_csv(args.outfile, encoding='utf-8')

try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO

with open(args.outfile, 'r') as file:
    in_memory_file = file.read()

# 2. open the CSV for cleaning
import csv
with open(args.outfile, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)

f = StringIO(in_memory_file)
reader = csv.reader(f, delimiter=',')
for row in reader:
    print('\t'.join(row))

# 3. strip $ and , from the money fields

# 4. compute the Pams_pin field

# 5. write the new file




