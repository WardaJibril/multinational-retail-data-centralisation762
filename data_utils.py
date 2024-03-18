import yaml
from sqlalchemy import create_engine, inspect

class DatabaseConnector():
    def read_db_creds(self):
        #reads db credentails from yaml file
        with open("db_creds.yaml","r") as file:
            creds = yaml.safe_load(file)
        return creds
    
    def init_db_engine(self,creds):
        
        creds = self.read_db_creds()
        #creates sqlachemy url
        db_url = f"{creds["type"]}://{creds["user"]}:{creds["password"]}@{creds["host"]}:{creds["port"]}/{creds["databse"]}"
        #creates engine
        engine = create_engine(db_url)
        return engine

    def list_db_names(self,engine):
        #gets a list of all tables in the database
        inspector = inspect(engine)
        inspector.get_table_names()

        
        

