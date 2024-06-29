import pandas as pd 
class DataCleaning():
    def clean_user_data(self, user_data_df):
        # null values
        user_data_df = user_data_df.dropna()

        #drop rows with incorrectly typed country codes
        user_data_df['country_code'] = user_data_df['country_code'].str.strip().str.upper()
        def is_valid_country_code(code):
          return len(code) == 2 and code.isalpha()
        user_data_df = user_data_df[user_data_df['country_code'].apply(is_valid_country_code)]

        # Drop rows where first and last names and country are not strings
        user_data_df = user_data_df[(user_data_df['first_name'].apply(lambda x: isinstance(x, str))) & (user_data_df['last_name'].apply(lambda x: isinstance(x, str))) & (user_data_df['country'].apply(lambda x: isinstance(x, str)))]
        
        #remove duplictae rows
        user_data_df = user_data_df.drop_duplicates()
    
        # Reformat the dates to yyyy-mm-dd format and Convert the date column to datetime format, coerce errors
        user_data_df["join_date"] = pd.to_datetime(user_data_df["join_date"],format="%Y-%m-%d", errors="coerce")

        user_data_df["date_of_birth"] = pd.to_datetime(user_data_df["date_of_birth"],format="%Y-%m-%d", errors="coerce")

        return user_data_df 


    def clean_card_data(self,pdf_data_df):
     # ensure all card details are 13 - 16 characters long
        pattern = r'\b(?:\d[ -]*?){13,16}\b'
        pdf_data_df["card_number"] = pdf_data_df["card_number"].str.findall(pattern).apply(lambda x: ' '.join(x) if x else None)
        # remove rows with null values
        pdf_data_df = pdf_data_df.dropna()
        #format dates
        pdf_data_df["expiry_date"]= pd.to_datetime(pdf_data_df["expiry_date"],format="%m-%d", errors="coerce")
        pdf_data_df["date_payment_confimred"]= pd.to_datetime(pdf_data_df["date_payment_confimred"],format="%Y-%m-%d", errors="coerce")
        
        return pdf_data_df
    
   
