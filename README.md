# SQL NEON Tick and Pathogen Occurrence

## Brief Overview
Here, I continue to use the NEON Tick and Pathogen Occurrence data as used in my other repositories. For this repository I focus on creating a SQLite database containing three relational databases. I then perform several queries including a few basic searches and a few more advanced searches that involve joins.

## Description of the Datasets
All data is openly and freely accessible via the National Ecological Observatory Network website. The National Ecological Observatory Network (NEON) is a NSF funded project designed to  "characterize and quantify complex, rapidly changing effects of ecological processes across the US" over a 30 year time-frame. Data collected is intended to be used by "scientists, educators, planners, decision makers and public to map, understand and predict the effects of human activities on ecology and effectively address critical ecological questions and issues." (https://www.neonscience.org/about)

For my analyses, I focus on the ticks sampled using drag cloths and tick-born pathogen status datasets (data available here: https://data.neonscience.org/browse-data?showAllDates=true&showAllSites=true&showTheme=org). Datasets were downloaded on 02/13/2019 and a custom python script was used to compile data from individual csv files downloaded from NEON resulting in three relational datasets related by unique identifier keys (ER_diagram_relational_datasets.pdf for Entity Relationship (ER) Diagram for dataset relations)-- tck_fieldData, tck_taxonomyProcessed, and tck_Pathogen. Taxonomic identification and pathogensis analyses are still being carried out on field collected samples and as such tc_taxonomyProcessed and tck_pathogen datasets are incomplete. Below are details of the three datasets as of 02/13/2019.

### tck_fieldData
* 6,124 rows x 27 columns
* Details the count of adult, nymph and larva of ticks collected at fieldsites using a drop cloth method
* Samples were collected from 04/2014 to 11/2018 from 45 sites and 283 plots (note that not all sites and plots were sampled over the full time period)

### tck_taxonomyProcessed
* 2,962 rows x 31 columns
* Provides the taxonomic species identification of ticks collected from tck_fieldData
* The taxonomy has been processed for 25 sites and 130 plots for samples collected from 04/2014-09/2018

### tck_pathogen
* 78,956 rows x 27 columns
* Details the results of pathogensis analyses performed on ticks collected from tck_fieldData and identified in tck_taxonomyProcessed
* Results from pathongensis analyses have been obtained for 13 sites and 62 plots.

## Description of Python scripts

### create_db.py
I create three tables in the database called NEON_tck.db using data stored in csv files. First, I load the csv file into a pandas dataframe and then use pandas.DataFrame.to_sql() to convert the pandas dataframe into a SQL table. Finally I print the first two rows of each table to check that the code worked.

### SQLQuery.py
Here, I use the NEON_tck.db to perform SQL queries. For the more advanced queries requiring joins, the ER diagram is helpful to reference. 
