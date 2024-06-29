import pandas as pd
import tabula
from data_utils import DatabaseConnector
import requests



class DataExtractor():
    
    def read_rds_table(self,db_connect,table_name):

        # Get the engine from DatabaseConnector
        db_connect = DatabaseConnector()
        creds = db_connect.read_db_creds()
        engine = db_connect.init_db_engine(creds)
        

        # Read data from the specified table into a pandas DataFrame
        with engine.connect() as connection:
            df = pd.read_sql_table(table_name, connection)

        return df
    

    
    def retreive_pdf_data(self):

        link = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"

        pdf_data_df = tabula.read_pdf(link, pages="all")

        return pdf_data_df

    #returns number of stores to extract
    def list_number_of_stores(self):
        
        header = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        response = requests.get("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores", headers= header)
        # Check if the request was successful 
        if response.status_code == 200:
          number_of_stores = response.json()["number_stores"]
          print(f"number_of_stores: {number_of_stores}")
          return number_of_stores

    def retrieve_store_data(self, endpoint):
        header = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        store_data = []

        for store_number in range (1 , 452):
            response = requests.get(endpoint.format(store_number), headers= header)
            
            if response.status_code == 200:
               store_data.append(response.json())

        store_data_df = pd.DataFrame(store_data)
        return store_data_df

data_extract = DataExtractor()
#number_of_stores = data_extract.list_number_of_stores()
store_data_df = data_extract.retrieve_store_data(" https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{}")
store_data_df.to_csv('store_data.csv', index=False)