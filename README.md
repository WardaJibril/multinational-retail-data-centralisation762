# Sales Data Engineering Pipeline

## Project Overview
This project demonstrates a complete end-to-end **data engineering pipeline** that ingests, cleans, transforms, and loads **sales data** into a **PostgreSQL data warehouse**. It simulates a real-world **business intelligence pipeline** where raw data from multiple sources is processed and stored for advanced analytics. The goal is to showcase **ETL workflows**, **data warehousing**, and **SQL analytics** to produce actionable business insights.

### Key Learnings:
- **Data transformation** and **cleaning** using **Python**
- Data loading into a **PostgreSQL data warehouse** using **SQLAlchemy**
- Advanced **SQL analytics** for deriving insights from sales data
- Integration of **AWS S3** for cloud-based storage

---

## Tools & Technologies Used
- **Python**: For data extraction, transformation, and cleaning
- **PostgreSQL**: Centralized data warehouse for structured data
- **Pandas**: Data wrangling and manipulation
- **AWS S3**: Cloud storage for CSV and JSON data files
- **Boto3**: AWS SDK for Python to interface with **AWS S3**
- **REST APIs**: For fetching data from external sources
- **SQL**: Advanced queries for analytics and reporting
- **Git & GitHub**: Version control for project development and collaboration

---

## Pipeline Workflow

### Data Sources
The pipeline processes data from multiple sources:
- **User**, **card**, **store**, and **product data** sourced from:
  - **AWS RDS Databases** (for user and sales data)
  - **RESTful APIs** (for store details)
  - **AWS S3 Buckets** (for CSV & JSON data)

### Data Extraction
Data is extracted using the following methods:
- **PostgreSQL**: Using **psycopg2** to query relational databases.
- **AWS S3**: Using **boto3** to interact with **S3** and download **CSV/JSON** files.
- **REST APIs**: Using **requests** to fetch store details from external APIs.

### Data Cleaning (ETL)
Data transformation and cleaning are performed through custom Python classes:
- **Standardizing Data Types**: Ensured consistency in types like **UUID**, **VARCHAR**, and **FLOAT**.
- **Unit Conversion**: Converted weights from pounds to kilograms where necessary.
- **Missing Values**: Handled missing data and ensured no nulls in critical columns.
- **Data Integrity**: Applied referential integrity and consistency in data relationships (e.g., foreign key constraints for joins).

### Data Loading
Cleaned DataFrames are loaded into **PostgreSQL** using **SQLAlchemy**, with the data structured in a **star schema** for easier querying:
- **dim_users** – User details
- **dim_store_details** – Store metadata
- **dim_products** – Product information
- **dim_card_details** – Card usage details
- **dim_date_times** – Date and time breakdown for sales
- **orders_table** (fact table) – Contains transaction data

---

## Analytical SQL Highlights
In the **analytics_queries.sql** file, I executed complex **SQL queries** to generate business insights, including:
- 🔹 **Top months per year by sales volume**
- 🔹 **Staff headcount by country**
- 🔹 **Store-type performance in Germany**
- 🔹 **Average time between sales** using **LEAD()** + **INTERVAL**
- 🔹 **Sales contribution by store type**

---

## Conclusion
This project demonstrates an efficient and scalable **sales data engineering pipeline** using industry-standard tools like **Python**, **PostgreSQL**, and **AWS S3**. It provides insights into **data cleaning**, **transformation**, **storage**, and **SQL analytics** to drive business decisions.
