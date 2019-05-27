#! /usr/bin/env python

import sqlite3

# create connection to the db called 'NEON_tck'
conn = sqlite3.connect('NEON_tck.db')
c = conn.cursor()

# peform basic search to determine sites with greater adult ticks present
c.execute ("""SELECT uid
                ,collectDate
                ,siteID
                ,plotID
                ,nlcdClass
                ,adultcount
                ,nymphcount
                ,larvacount
            FROM tck_fielddata
            WHERE adultcount >0
            ORDER BY siteID""")

data=c.fetchall()
for row in data:
    print (row)

# perform advanced search summarize counts across siteID and year
# then determine which sites had zero adults
c.execute("""SELECT siteID
                ,STRFTIME('%Y', collectDate) AS collectYear
                ,AVG(adultcount) as average_adultcount
                ,AVG(nymphcount) as average_nymphcount
                ,AVG(larvacount) as average_larvacount
            FROM tck_fielddata
            GROUP BY siteID, collectYear
            HAVING average_adultcount = 0
            ORDER BY siteID, collectYear""")

data=c.fetchall()
for row in data:
    print (row)

# perform join and then search
# I want to know which sites had ticks (and tick sp. name) carrying pathogens (and pathogen name)
c.execute("""SELECT fd.siteID
                ,STRFTIME('%Y', fd.collectDate) AS collectYear
                ,tax.genus
                ,tax.specificEpithet
                ,path.testPathogenName
                ,path.testResult
            FROM ((tck_fielddata AS fd
                INNER JOIN tck_taxonomyProcessed AS tax
                ON fd.sampleID = tax.sampleID)
                    INNER JOIN tck_pathogen AS path
                    ON tax.subsampleID = path.subsampleID)
            WHERE path.testResult = 'Positive'
                AND NOT path.testPathogenName='HardTick DNA Quality'
            ORDER BY fd.siteID, collectYear""" )

data=c.fetchall()
for row in data:
    print (row)

# similar to the above search but now... 
# I want to know simply which sites by year had ticks carrying pathogens
c.execute("""SELECT fd.siteID
                ,STRFTIME('%Y', fd.collectDate) AS collectYear
                ,path.testResult
            FROM ((tck_fielddata AS fd
                INNER JOIN tck_taxonomyProcessed AS tax
                ON fd.sampleID = tax.sampleID)
                    INNER JOIN tck_pathogen AS path
                    ON tax.subsampleID = path.subsampleID)
            WHERE path.testResult = 'Positive'
                AND NOT path.testPathogenName='HardTick DNA Quality'
            GROUP BY fd.siteID, collectYear
            ORDER BY fd.siteID, collectYear""" )

data=c.fetchall()
for row in data:
    print (row)

c.close()
conn.close()
