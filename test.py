import unittest
import pandas as pd
from sqlalchemy import create_engine, text, inspect
from assignment import transform_and_load_data

class TestDataTransformation(unittest.TestCase):
    def setUp(self):
        """Set up a temporary in-memory SQLite database for testing"""
        self.engine = create_engine('sqlite:///:memory:')
        self.connection = self.engine.connect()

        # Create and populate the products table
        self.connection.execute(text("""
        CREATE TABLE products (
            product_name TEXT,
            price TEXT,
            category TEXT
        );
        """))
        self.connection.execute(text("""
        INSERT INTO products (product_name, price, category) VALUES
        ('Laptop', '$1200', 'electronics'),
        ('Coffee Maker', '$50', 'home goods'),
        ('Book', '$15.99', 'books'),
        ('Headphones', '$150', 'electronics'),
        ('Desk Chair', '$89.99', 'furniture');
        """))
        self.connection.commit()

    def tearDown(self):
        """Close the database connection after each test"""
        self.connection.close()

    def test_transform_and_load_data_creates_table(self):
        """Test that the function creates the products_cleaned table"""
        transform_and_load_data(self.connection)
        inspector = inspect(self.engine)
        self.assertTrue(inspector.has_table('products_cleaned'))

    def test_cleaned_table_has_correct_schema(self):
        """Test that the new table has the expected columns and data types"""
        transform_and_load_data(self.connection)
        df = pd.read_sql_table('products_cleaned', self.connection)
        self.assertListEqual(list(df.columns), ['product_name', 'price', 'category', 'is_expensive'])
        self.assertTrue(pd.api.types.is_numeric_dtype(df['price']))
        self.assertTrue(pd.api.types.is_integer_dtype(df['is_expensive']))

    def test_price_column_is_cleaned(self):
        """Test that the price column is correctly cleaned and converted"""
        transform_and_load_data(self.connection)
        df = pd.read_sql_table('products_cleaned', self.connection)
        self.assertFalse(df['price'].isnull().any())
        self.assertEqual(df.loc[df['product_name'] == 'Laptop', 'price'].iloc[0], 1200.0)

    def test_category_column_is_standardized(self):
        """Test that the category column is converted to uppercase"""
        transform_and_load_data(self.connection)
        df = pd.read_sql_table('products_cleaned', self.connection)
        self.assertTrue(all(df['category'].str.isupper()))

    def test_is_expensive_feature_is_correct(self):
        """Test that the is_expensive feature is calculated correctly"""
        transform_and_load_data(self.connection)
        df = pd.read_sql_table('products_cleaned', self.connection)
        self.assertEqual(df.loc[df['product_name'] == 'Laptop', 'is_expensive'].iloc[0], 1)
        self.assertEqual(df.loc[df['product_name'] == 'Coffee Maker', 'is_expensive'].iloc[0], 0)

if __name__ == '__main__':
    unittest.main()
