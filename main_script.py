from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from data_utils import DatabaseConnector


db_connect = DatabaseConnector()
creds = db_connect.read_db_creds()
engine = db_connect.init_db_engine(creds)
table_names = db_connect.list_db_names(engine)

#extract the data
data_extract = DataExtractor()
user_data_df = data_extract.read_rds_table(db_connect,"legacy_users")
pdf_data_df = data_extract.retreive_pdf_data()
store_data_df = data_extract.retrieve_store_data(" https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{}")


#clean the data
clean = DataCleaning()
cleaned_user_data = clean.clean_user_data(user_data_df)
cleaned_pdf_data = clean.clean_card_data(pdf_data_df)


#upload clean data to sales database
upload = DatabaseConnector()
user_data_upload = upload.upload_to_db(engine, cleaned_user_data, "dim_users")
pdf_data_upload = upload.upload_to_db(engine,cleaned_pdf_data,"dim_card_details")
