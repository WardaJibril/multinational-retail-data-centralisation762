# multinational-retail-data-centralisation762

This project aims to produce a system that stores the current company data in a centralised database location so that then can be queried to get up-to-date metrics for the business.

# file structure of project

There are four python files within this project. The main_script.py is the only python file that needs to be run. This file contains all the executable code.
the other three files contain the methods and classes for connecting, extracting and cleaning the data. 

The data is stored in multiple formats and each require a a diffrent extraction method as shown in the data_extraction.py. The data is stored in an S3 objects, AWS relation databases, local databases, csv files, pdf files. Also, some of the data is on a web page that can retreived using an API.

To clean the data, pandas dataframes are used as shown in the data_cleaning.py file.

The data_utils.py file has all the neccessary function to connect to local and cloud databases to either extract or load the data to the approriate location by use of an engine.

There is an Entity relationship diagram included in this project to help clarify th relationships between the table siwithon the database. 

The SQL script folder contains the sql code used to create the star based database schema.
