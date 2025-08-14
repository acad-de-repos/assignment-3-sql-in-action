import pandas as pd
import numpy as np

def transform_and_load_data(db_connection):
  """
  Extracts product data, transforms it, and loads it into a new table.

  This function practices a common data engineering workflow:
  1. Data extraction from a database
  2. Data cleaning and standardization
  3. Feature creation
  4. Loading cleaned data into a new table

  Args:
    db_connection: An active database connection object.
  """
  # Task 1: Extract the products data
  # Hint: Use pd.read_sql_table() to read the 'products' table
  # Think about: How do you read a table from a database connection?
  df = None
  # Your code here

  # Task 2: Clean the price column
  # Hint: Use .str.replace() to remove '$' and pd.to_numeric() to convert
  # Think about: First remove the currency symbol, then convert to numbers
  # Your code here

  # Task 3: Standardize the category column
  # Hint: Use .str.upper() to convert to uppercase
  # Think about: How can you make all category values consistent?
  # Your code here

  # Task 4: Create the 'is_expensive' feature
  # Hint: Use np.where() or a lambda function to create the binary feature
  # Think about: How can you create a 1/0 column based on a price threshold?
  # Your code here

  # Task 5: Load the transformed data into a new table
  # Hint: Use df.to_sql() to create the 'products_cleaned' table
  # Think about: How do you write a DataFrame back to a database?
  # Your code here

  pass
