#!/usr/bin/env python3
"""
MySQLServer.py - Creates the alx_book_store database in MySQL server
This script creates the database if it doesn't exist and handles errors gracefully.
"""

import mysql.connector
from mysql.connector import Error
import sys

def create_database():
    """
    Creates the alx_book_store database in MySQL server.
    Handles connection errors and database creation.
    """
    connection = None
    cursor = None
    
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change this to your MySQL username
            password='',  # Change this to your MySQL password
            port=3306
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # Database creation successful if no exception was raised
            print("Database 'alx_book_store' created successfully!")
                
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        print("Please check your MySQL server connection and credentials.")
        sys.exit(1)
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
        
    finally:
        # Close database connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
