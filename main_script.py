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
product_data_df = data_extract.extract_from_s3_URI("s3://data-handling-public/products.csv")
orders_data_df = data_extract.read_rds_table(db_connect,"orders_table")
date_details_df = data_extract.extract_from_s3_http("https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json")

#clean the data
clean = DataCleaning()
cleaned_user_data = clean.clean_user_data(user_data_df)
cleaned_pdf_data = clean.clean_card_data(pdf_data_df)
cleaned_store_data = clean.clean_store_data(store_data_df)
cleaned_product_data = clean.convert_product_weights(product_data_df)
cleaned_order_data = clean.clean_orders_data(orders_data_df)
cleaned_date_data = clean.clean_date_data(date_details_df)


#upload clean data to sales database
upload = DatabaseConnector()
user_data_upload = upload.upload_to_db(engine, cleaned_user_data, "dim_users")
pdf_data_upload = upload.upload_to_db(engine,cleaned_pdf_data,"dim_card_details")
store_data_upload = upload.upload_to_db(engine,cleaned_store_data, "dim_store_details")
product_data_upload = upload.upload_to_db(engine,cleaned_product_data,"dim_products")
order_data_upload = upload.upload_to_db(engine, cleaned_order_data,"orders_table")
date_details_upload = upload.upload_to_db(engine, cleaned_date_data, "dim_date_times")