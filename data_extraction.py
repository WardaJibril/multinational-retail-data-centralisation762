import pandas as pd
import tabula
from data_utils import DatabaseConnector
import requests
import boto3
from io import BytesIO
from urllib.parse import urlparse

class DataExtractor():
    
    def read_rds_table(self,db_connect,table_name):

        # Get the engine from DatabaseConnector
        db_connect = DatabaseConnector()
        creds = db_connect.read_cloud_db_creds()
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
    
    def extract_from_s3_URI(self,address):
        
        # Parse the S3 address to extract bucket name and key
        address_parts = address.replace("s3://", "").split("/")
        bucket_name = address_parts[0]
        object_key = "/".join(address_parts[1:])
        
        s3 = boto3.client('s3')
        
        # Download the file from S3 to a BytesIO object
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        data = response['Body'].read()
        
        # Read the CSV data into a pandas DataFrame
        product_data_df = pd.read_csv(BytesIO(data))
        
        return product_data_df
    
    def extract_from_s3_http(self,address):

        parsed_url = urlparse(address)
       
        bucket_name = parsed_url.netloc.split('.')[0] 
        object_key = parsed_url.path.lstrip('/') 

        s3 = boto3.client('s3')
        
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        data = response['Body'].read()
        
        # Read the CSV data into a pandas DataFrame
        date_details_df = pd.read_json(BytesIO(data))

        return date_details_df
    
