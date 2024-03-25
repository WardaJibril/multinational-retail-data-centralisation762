from data_utils import DatabaseConnector
import pandas as pd

class DataExtractor():
    
    def read_rds_table(self,db_connect,table_name):
        
        # Get the engine from DatabaseConnector
        engine = db_connect.init_db_engine(creds)

        # Read data from the specified table into a pandas DataFrame
        with engine.connect() as connection:
            df = pd.read_sql_table(table_name, connection)
        
        return print(f"TABLE NAME:{table_name} \n {df}")

db_connect = DatabaseConnector()

creds = db_connect.read_db_creds()

engine = db_connect.init_db_engine(creds)

# Get the name of the table containing user data using list_db_tables method
table_names = db_connect.list_db_names(engine)

data_extract = DataExtractor()

# iterate through the list of table names to extract the table data 
for table_name in table_names:
    
        # Extract the table containing user data and return a pandas DataFrame
    user_data_df = data_extract.read_rds_table(db_connect, table_name)
