from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from data_utils import DatabaseConnector

# Extract the table containing user data and return a pandas DataFrame
db_connect = DatabaseConnector()
creds = db_connect.read_db_creds()
engine = db_connect.init_db_engine(creds)

table_names = db_connect.list_db_names(engine)
data_extract = DataExtractor()

user_data_df = data_extract.read_rds_table(db_connect,"legacy_users")

#clean the data
clean = DataCleaning()
cleaned_user_data = clean.clean_user_data(user_data_df)

#upload clean data to sales database
upload = DatabaseConnector()
user_data_upload = upload.upload_to_db(engine, cleaned_user_data, "dim_users")