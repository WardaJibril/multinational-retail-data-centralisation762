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
     
        # remove rows with null values
        pdf_data_df = pdf_data_df.dropna()
        #format dates
        pdf_data_df["expiry_date"]= pd.to_datetime(pdf_data_df["expiry_date"],format="%m-%d", errors="coerce")
        

        return pdf_data_df
      
    def clean_store_data(self,store_data_df):
        # Convert column to numeric 
        store_data_df['staff_numbers'] = pd.to_numeric(store_data_df['staff_numbers'], errors='coerce')
        store_data_df['latitude'] = pd.to_numeric(store_data_df['latitude'], errors='coerce')
        store_data_df['longitude'] = pd.to_numeric(store_data_df['longitude'], errors='coerce')

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

            if isinstance(weight_str, str) and len(weight_str) >= 2:

                weight_str = weight_str.strip()

                unit = weight_str[-2:].lower() if weight_str[-2:].lower() in conversion_factors else weight_str[-1].lower()
                
                try:
                    if unit == 'kg':
                        return float(weight_str[:-2].strip())
                    elif unit == 'g':
                        return float(weight_str[:-1].strip()) * conversion_factors['g']
                    elif unit == 'ml':
                        return float(weight_str[:-2].strip()) * conversion_factors['ml']
                except ValueError:
                    return None  
            return None  
        
        product_data_df['weight'] = product_data_df['weight'].apply(convert_weight)
       
        product_data_df = product_data_df.dropna(subset=['weight'])
        
        return product_data_df
    
    def clean_orders_data (self,orders_data_df):
         orders_data_df = orders_data_df.drop(['first_name', 'last_name', '1'], axis=1, errors='ignore')
        
         return orders_data_df
    
    def clean_date_data (self,date_details_df):
        
        try:
            date_details_df['timestamp'] = pd.to_datetime(date_details_df['timestamp'], format='%H:%M:%S').dt.time
        except ValueError:
            # Handle ValueError (e.g., log, skip, or set to NaN)
            date_details_df['timestamp'] = pd.NaT

        date_details_df['month'] = pd.to_numeric(date_details_df['month'], errors='coerce')

        date_details_df['year'] = pd.to_numeric(date_details_df['year'], errors='coerce')

        date_details_df['day'] = pd.to_numeric(date_details_df['day'], errors='coerce')

        return date_details_df
    