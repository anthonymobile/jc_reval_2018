# converts the Excel file provided by Appraisal Systems to a CSV suitable for us in QGIS, Pandas, etc.
# http://www.asinj.com/revaluation.asp?p=current&id=359
# Anthony Townsend v 0.1 10 may 2018

import sys
import argparse
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--infile', dest='infile', default=None, help="Excel file from Appraisal Systems")
parser.add_argument('--outfile', dest='outfile', default=None, help="CSV file to write")
args = parser.parse_args()

if not args.infile:
		print('please provide inpute file')
		sys.exit(-1)

print ('infile: %s' % args.infile)
print ('outfile: %s' % args.outfile)


# 1. read data - csv or xlsx 

if args.infile.find('.csv') != -1:
		data_frame = pd.read_csv(args.infile)
elif args.infile.find('.xlxs'):
		data_frame = pd.read_excel(args.infile, 'released as of April 18th', index_col=None)

# 4. compute the Pams_pin field

# 5. write the new file

if args.outfile:
		data_frame.to_csv(args.outfile, index=False)

