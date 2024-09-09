# multinational-retail-data-centralisation762

This project aims to produce a system that stores the current company data in a centralised database location so that then can be queried to get up-to-date metrics for the business.

#File structure of the project

there are four python files within this project. The main_script.py is the on ly file that needs to be run as it  file contains all the #### t.   
the other three files contain the functions for connecting, extracting and cleaning the data. the data is stored in multiple formats and each require a a diffrent extraction method as shown inthe data_extraction.py. ### csv-method, pdf, aws, api, 

To clean the data, pandas dataframes are used as shown in the data_cleaning.py file.

the data_utils.py file has all the neccessary function to connect to sql databases, ###aws, to either extract or load the data to the approriate location.

there is a Entity relationship diagram included in this project to help clarify th relationships between the table siwithon the database. 

the SQL script folder contains the sql code used to create the database schema.
