import yaml
from sqlalchemy import create_engine, inspect
import pandas as pd

class DatabaseConnector():
    def read_cloud_db_creds(self):
        #reads db credentails from yaml file
        with open("cloud_db_creds.yaml","r") as file:
            cloud_creds = yaml.safe_load(file)
        return cloud_creds
    
    def read_local_db_creds(self):
        #reads db credentails from yaml file
        with open("local_db_creds.yaml","r") as file:
            local_creds = yaml.safe_load(file)
        return local_creds
    
    def init_db_engine(self,creds):
        
        #creds = self.read_db_creds()
        #creates sqlachemy url
        db_url = f'postgresql+psycopg2://{creds["RDS_USER"]}:{creds["RDS_PASSWORD"]}@{creds["RDS_HOST"]}:{creds["RDS_PORT"]}/{creds["RDS_DATABASE"]}'
        #creates engine
        engine = create_engine(db_url)
        return engine

    def list_db_names(self,engine):
        #gets a list of all tables in the database
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        return table_names
    
    def upload_to_db(self, engine,df,table_name,if_exists='replace', index=False):
        
            df.to_sql(table_name, engine,if_exists=if_exists, index=index)
            print(f"Upload of {table_name} successful")

        

