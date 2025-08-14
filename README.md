# SQL in Action: Data Transformation Assignment

## Problem Description

In this assignment, you will practice data transformation and cleaning tasks using a combination of SQL and Python. You will connect to a database, extract data, perform transformations, and load the cleaned data back into a new table. This assignment simulates a real-world data engineering workflow where you prepare data for analysis or machine learning.

## Learning Objectives

By completing this assignment, you will learn:
- How to connect to a database and execute SQL queries from Python
- How to perform data type conversions and handle inconsistencies
- How to clean and standardize text data
- How to create a new table and insert cleaned data
- How to combine SQL and pandas for effective data manipulation

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have the following packages installed:
   - pandas (>=1.3.0)
   - sqlalchemy (>=1.4.0)

## Instructions

1. Open the `assignment.py` file.
2. You will find a function definition: `transform_and_load_data(db_connection)`.
3. The function takes a database connection object as input.
4. Your tasks are to:
   *   **Task 1**: Extract the `products` data from the database.
   *   **Task 2**: Clean the `price` column by removing currency symbols and converting it to a numeric type.
   *   **Task 3**: Standardize the `category` column by converting all values to uppercase.
   *   **Task 4**: Create a new feature called `is_expensive` which is 1 if the price is greater than 100, and 0 otherwise.
   *   **Task 5**: Create a new table called `products_cleaned` and load the transformed data into it.

## Hints

*   Use `pd.read_sql_table()` to extract the initial data into a DataFrame.
*   Use string manipulation functions in pandas (e.g., `.str.replace()`, `.str.upper()`) to clean the data.
*   Use `pd.to_numeric()` to convert the `price` column to a numeric type.
*   Use a `lambda` function or `np.where()` to create the `is_expensive` feature.
*   Use `df.to_sql()` to create the new table and insert the cleaned data.

## Testing Your Solution

Run the test file to verify your implementation:
```bash
python test.py
```

The tests will check:
- That the function creates the `products_cleaned` table
- That the new table has the expected columns and data types
- That the data transformations are applied correctly
- That the `is_expensive` feature is accurately calculated

## Expected Output

Your function should create a new table named `products_cleaned` in the database with the transformed and cleaned data. The new table should have the following columns: `product_name`, `price`, `category`, and `is_expensive`.

## Sample Data Format

The database will contain a `products` table with the following columns:
- `product_name` (TEXT)
- `price` (TEXT)
- `category` (TEXT)

Example:
```
product_name | price   | category
----------------|---------|-----------
Laptop          | $1200   | electronics
Coffee Maker    | $50     | home goods
Book            | $15.99  | books
```

## Troubleshooting

### Common Errors
- `DatabaseError: execution failed on statement`: Check your SQL syntax for errors.
- `ValueError: could not convert string to float`: Ensure you have correctly cleaned the `price` column before converting it to a numeric type.
- `AttributeError`: Make sure you are using the correct pandas functions for string manipulation and data conversion.

## Further Exploration (Optional)

*   How would you handle different currency symbols in the `price` column?
*   Explore other data cleaning techniques, such as removing leading/trailing whitespace or handling inconsistent capitalization.
*   Can you add a new feature that calculates the discounted price for each product?
*   Look into using a dedicated data cleaning library like `datacleaner`.

## Resources

- [Pandas Data Cleaning Tutorial](https://www.geeksforgeeks.org/python-pandas-series-str-replace/)
- [Pandas `to_numeric` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html)
- [Pandas `to_sql` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
- [Data Cleaning with Python and Pandas](https://realpython.com/python-data-cleaning-pandas-numpy/)
