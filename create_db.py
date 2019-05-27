#! /usr/bin/env python

import sqlite3
import sqlalchemy
import csv
import pandas as pd

# create connection to the db called 'NEON_tck'
conn = sqlite3.connect('NEON_tck.db')
c = conn.cursor()

# create 3 tables in the NEON_tck database and populate with data from csv file
# first table:
# # dictionary of column types
# dtype_dict= {#"uid": sqlalchemy.types.String(),
#     "namedLocation": sqlalchemy.types.String(),
#     "domainID": sqlalchemy.types.String(),
#     "siteID": sqlalchemy.types.String(),
#     "plotID": sqlalchemy.types.String(),
#     "plotType": sqlalchemy.types.String(),
#     "nlcdClass": sqlalchemy.types.String(),
#     "decimalLatitude": sqlalchemy.types.Float(),
#     "decimalLongitude": sqlalchemy.types.Float(),
#     "geodeticDatum": sqlalchemy.types.String(),
#     "coorinateUncertainty": sqlalchemy.types.Float(),
#     "elevation": sqlalchemy.types.Float(),
#     "elevationUncertainty": sqlalchemy.types.Float(),
#     "collectDate": sqlalchemy.types.Date(),
#     "eventID": sqlalchemy.types.String(),
#     "sampleID": sqlalchemy.types.String(),
#     "sampleCode": sqlalchemy.types.String(),
#     "samplingMethod": sqlalchemy.types.String(),
#     "totalSampledArea": sqlalchemy.types.String(),
#     "targetTaxaPresent": sqlalchemy.types.String(),
#     "adltCount": sqlalchemy.types.Numeric(),
#     "nymphCount": sqlalchemy.types.Numeric(),
#     "larvaCount": sqlalchemy.types.Numeric(),
#     "sampleCondition": sqlalchemy.types.String(),
#     "samplingProtocolVersion": sqlalchemy.types.String(),
#     "measuredBy": sqlalchemy.types.String(),
#     "remarks": sqlalchemy.types.String()}


# dtype_dict= {"uid": sqlalchemy.types.TEXT(),
#     "namedLocation": VARCHAR(),
#     "domainID": VARCHAR(),
#     "siteID": VARCHAR(),
#     "plotID": VARCHAR(),
#     "plotType": NVARCHAR(),
#     "nlcdClass": NVARCHAR(),
#     "decimalLatitude": DECIMAL(),
#     "decimalLongitude": DECIMAL(),
#     "geodeticDatum": VARCHAR(),
#     "coorinateUncertainty": DECIMAL(),
#     "elevation": sqlalchemy.types.DECIMAL(),
#     "elevationUncertainty": sqlalchemy.types.DECIMAL(),
#     "collectDate": sqlalchemy.types.DATE(),
#     "eventID": sqlalchemy.types.NVARCHAR(),
#     "sampleID": sqlalchemy.types.NVARCHAR(),
#     "sampleCode": sqlalchemy.types.NVARCHAR(),
#     "samplingMethod": sqlalchemy.types.NVARCHAR(),
#     "totalSampledArea": sqlalchemy.types.DECIMAL(),
#     "targetTaxaPresent": sqlalchemy.types.NVARCHAR(),
#     "adltCount": sqlalchemy.types.REAL(),
#     "nymphCount": sqlalchemy.types.REAL(),
#     "larvaCount": sqlalchemy.types.REAL(),
#     "sampleCondition": sqlalchemy.types.NVARCHAR(),
#     "samplingProtocolVersion": sqlalchemy.types.NVARCHAR(),
#     "measuredBy": sqlalchemy.types.NVARCHAR(),
#     "remarks": sqlalchemy.types.NVARCHAR()}

csv_file_name = '1_tck_fielddata_concatenated.csv'
read_tckPath = pd.read_csv(csv_file_name)
read_tckPath.to_sql('tck_fielddata', con=conn, if_exists='replace')

# second table:
csv_file_name = '2_tck_taxonomyProcessed_concatenated.csv'
read_tckPath = pd.read_csv(csv_file_name)
read_tckPath.to_sql('tck_taxonomyProcessed', con=conn, if_exists='replace')

# third table:
csv_file_name = '3_tck_pathogen_concatenated.csv'
read_tckPath = pd.read_csv(csv_file_name)
read_tckPath.to_sql('tck_pathogen', con=conn, if_exists='replace')


# check that tables have been created and populated
print('checking tck_fielddata')
print('printing first two rows of data in tck_fielddata:')

c. execute('SELECT * FROM tck_fielddata')
data=c.fetchall()
for i in range(2):
    print (data[i])

print('')
print('checking tck_taxonomyProcessed')
print('printing first two rows of data in tck_taxonomyProcessed:')

c. execute('SELECT * FROM tck_taxonomyProcessed')
data=c.fetchall()
for i in range(2):
    print (data[i])

print('')
print('checking tck_pathogen')
print('printing first two rows of data in tck_pathogen:')

c. execute('SELECT * FROM tck_pathogen')
data=c.fetchall()
for i in range(2):
    print (data[i])

# save changes to db and close connection to db
conn.commit()
c.close()
conn.close()
