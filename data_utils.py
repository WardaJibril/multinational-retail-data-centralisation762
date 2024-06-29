import yaml
from sqlalchemy import create_engine, inspect
import pandas as pd

class DatabaseConnector():
    def read_db_creds(self):
        #reads db credentails from yaml file
        with open("db_creds.yaml","r") as file:
            creds = yaml.safe_load(file)
        return creds
    
    def init_db_engine(self,creds):
        
        creds = self.read_db_creds()
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
    
    def upload_to_db(self, engine,df,table_name):
        
            df = pd.read_sql_table(table_name, engine,)

