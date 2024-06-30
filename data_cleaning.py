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
      
    def clean_store_data(self,store_data_df):
        # Convert 'staff_number' column to numeric 
        store_data_df['staff_numbers'] = pd.to_numeric(store_data_df['staff_numbers'], errors='coerce')

        #all longitude an latidute entries are no longer than 5 decimal points
        store_data_df['latitude'] = store_data_df['latitude'].round(5)
        store_data_df['longitude'] = store_data_df['longitude'].round(5)

        return store_data_df
   
    def convert_product_weights(self,product_data_df):
      
        conversion_factors = {
            'kg': 1,
            'g': 0.001,
            'ml': 0.001  
        }
        
        def convert_weight(weight_str):
            if weight_str[-2:].lower() == 'kg':
                return float(weight_str[:-2])  
            elif weight_str[-1].lower() == 'g':
                return float(weight_str[:-1]) * conversion_factors['g'] 
            elif weight_str[-2:].lower() == 'ml':
                return float(weight_str[:-2]) * conversion_factors['ml']
            else:
                return None  
        
        product_data_df['weight'] = product_data_df['weight'].apply(convert_weight)
        
        return product_data_df
    
    def clean_orders_data (self,orders_data_df):
         orders_data_df = orders_data_df.drop(['first_name', 'last_name', '1'], axis=1, errors='ignore')
        
         return orders_data_df
    
    def clean_date_data (self,date_details_df):
        
        date_details_df['timestamp'] = pd.to_datetime(df['timestamp'], format='%H:%M:%S').dt.time

        date_details_df['month'] = df['month'].astype(int)

        date_details_df['year'] = df['year'].astype(int)

        date_details_df['day'] = df['day'].astype(int)

        return date_details_df
    