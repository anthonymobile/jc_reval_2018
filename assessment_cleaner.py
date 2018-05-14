# converts the Excel file provided by Appraisal Systems to a CSV suitable for us in QGIS, Pandas, etc.
# http://www.asinj.com/revaluation.asp?p=current&id=359

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
else:
    print('unrecognized file type')
    sys.exit(-2)

# 2. clean the money fields up

for col,type in zip(data_frame.columns, data_frame.dtypes):
    if type == np.dtype('O'):
        data_frame[col] = data_frame[col].apply(func=lambda x : str(x).replace('$','').replace(',',''))

# 3. compute the Pams_pin field

data_frame['pams_pin_new'] = ('0906_' + data_frame['BlockNo'].map(str) + '_' + str(data_frame['LotNo']) + '_' + data_frame['QualCode(s)'].map(str) )

# clean trailing underscores for those without QualCode(s)
data_frame['pams_pin_new'] = data_frame['pams_pin_new'].map(lambda x: x.rstrip('_'))



# 4. write the new file

if args.outfile:
    data_frame.to_csv(args.outfile, index=False)

