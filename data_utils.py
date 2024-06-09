import yaml
from sqlalchemy import create_engine, inspect
from data_cleaning import DataCleaning
from data_extraction import user_data_df
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
         # needs to uplaod any df into speciifed table 
        

         with engine.connect() as connection:
        
            df.to_sql(table_name, con=connection, if_exists='append', index=False)

         

db_connect = DatabaseConnector()
creds = db_connect.read_db_creds()
engine = db_connect.init_db_engine(creds)

table_names = db_connect.list_db_names(engine)

print(table_names)

clean = DataCleaning()
cleaned_user_data = clean.clean_user_data(user_data_df)

upload = DatabaseConnector()
user_data_upload = upload.upload_to_db(engine, cleaned_user_data, "dim_users")