from data_utils import DatabaseConnector
import pandas as pd
import tabula



class DataExtractor():
    
    def read_rds_table(self,db_connect,table_name):
        
        # Get the engine from DatabaseConnector
        engine = db_connect.init_db_engine(creds)

        # Read data from the specified table into a pandas DataFrame
        with engine.connect() as connection:
            df = pd.read_sql_table(table_name, connection)

        print(f"TABLE NAME:{table_name} \n {df}")

        return df
    

    
    def retreive_pdf_data(self,link):

        link = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"

        pdf_data = tabula.read_pdf(link, pages="all")

        return pdf_data



db_connect = DatabaseConnector()
creds = db_connect.read_db_creds()
engine = db_connect.init_db_engine(creds)
# Get the name of the table containing user data using list_db_tables method
table_names = db_connect.list_db_names(engine)
data_extract = DataExtractor()
# Extract the table containing user data and return a pandas DataFrame
user_data_df = data_extract.read_rds_table(db_connect,"legacy_users")



