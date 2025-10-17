# ALX Book Store Database Project

A comprehensive MySQL database project for an online bookstore system, implementing proper database design with foreign key relationships and data management.

## 🚀 Project Overview

This project creates a complete database system for an online bookstore with the following features:

- **Database Name**: `alx_book_store`
- **Tables**: Books, Authors, Customers, Orders, Order Details
- **Relationships**: Proper foreign key constraints and referential integrity
- **Data Management**: Scripts for table creation, data insertion, and querying

## 📊 Database Schema

### Tables Structure

#### Authors Table
- `author_id` (Primary Key, AUTO_INCREMENT)
- `author_name` VARCHAR(215) - Author's full name

#### Books Table
- `book_id` (Primary Key, AUTO_INCREMENT)
- `title` VARCHAR(130) - Book title
- `author_id` (Foreign Key → Authors.author_id)
- `price` DOUBLE - Book price
- `publication_date` DATE - Publication date

#### Customers Table
- `customer_id` (Primary Key, AUTO_INCREMENT)
- `customer_name` VARCHAR(215) - Customer's full name
- `email` VARCHAR(215) UNIQUE - Customer's email address
- `address` TEXT - Customer's address

#### Orders Table
- `order_id` (Primary Key, AUTO_INCREMENT)
- `customer_id` (Foreign Key → Customers.customer_id)
- `order_date` DATE - Date when order was placed

#### Order_Details Table
- `orderdetailid` (Primary Key, AUTO_INCREMENT)
- `order_id` (Foreign Key → Orders.order_id)
- `book_id` (Foreign Key → Books.book_id)
- `quantity` DOUBLE - Quantity of books ordered

## 📁 Project Files

### Core Files

#### `alx_book_store.sql` (Task 0)
Complete database schema with all tables and relationships.

#### `MySQLServer.py` (Task 1)
Python script that creates the database with proper error handling.

**Features:**
- Creates `alx_book_store` database if it doesn't exist
- Handles connection errors gracefully
- Provides success/error messages
- Properly closes database connections

#### `task_2.sql` (Task 2)
Creates all required tables with proper foreign key relationships.

#### `task_3.sql` (Task 3)
Lists all tables in the database.

#### `task_4.sql` (Task 4)
Shows full description of the books table using INFORMATION_SCHEMA.

#### `task_5.sql` (Task 5)
Inserts a single customer record:
- Cole Baidoo (cbaidoo@sandtech.com)

#### `task_6.sql` (Task 6)
Inserts multiple customer records:
- Blessing Malik (bmalik@sandtech.com)
- Obed Ehoneah (eobed@sandtech.com)
- Nehemial Kamolu (nkamolu@sandtech.com)

## 🛠️ Setup Instructions

### Prerequisites
- MySQL Server 8.0 or higher
- Python 3.7 or higher
- mysql-connector-python package

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/Hayzedid/Intro_to_DB.git
cd Intro_to_DB
```

2. **Install Python dependencies**:
```bash
pip install mysql-connector-python
```

3. **Configure MySQL connection**:
Edit `MySQLServer.py` and update the connection parameters:
```python
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',    # Update this
    password='your_password', # Update this
    port=3306
)
```

### Running the Project

#### Method 1: Using Python Script
```bash
python MySQLServer.py
```

#### Method 2: Using MySQL Command Line

1. **Create database and tables**:
```bash
mysql -u root -p < alx_book_store.sql
```

2. **Create tables only**:
```bash
mysql -u root -p alx_book_store < task_2.sql
```

3. **List all tables**:
```bash
mysql -u root -p alx_book_store < task_3.sql
```

4. **Show books table description**:
```bash
mysql -u root -p alx_book_store < task_4.sql
```

5. **Insert single customer**:
```bash
mysql -u root -p alx_book_store < task_5.sql
```

6. **Insert multiple customers**:
```bash
mysql -u root -p alx_book_store < task_6.sql
```

## 🔗 Database Relationships

### Foreign Key Constraints

1. **Books → Authors**
   - `books.author_id` references `authors.author_id`
   - ON DELETE SET NULL, ON UPDATE CASCADE

2. **Orders → Customers**
   - `orders.customer_id` references `customers.customer_id`
   - ON DELETE CASCADE, ON UPDATE CASCADE

3. **Order_Details → Orders**
   - `order_details.order_id` references `orders.order_id`
   - ON DELETE CASCADE, ON UPDATE CASCADE

4. **Order_Details → Books**
   - `order_details.book_id` references `books.book_id`
   - ON DELETE CASCADE, ON UPDATE CASCADE

## 📋 Sample Data

### Customers
| ID | Name | Email | Address |
|----|------|-------|---------|
| 1 | Cole Baidoo | cbaidoo@sandtech.com | 123 Happiness Ave. |
| 2 | Blessing Malik | bmalik@sandtech.com | 124 Happiness Ave. |
| 3 | Obed Ehoneah | eobed@sandtech.com | 125 Happiness Ave. |
| 4 | Nehemial Kamolu | nkamolu@sandtech.com | 126 Happiness Ave. |

## 🎯 Key Features

### Database Design
- **Normalized Structure**: Follows 3NF principles
- **Referential Integrity**: Proper foreign key constraints
- **Data Types**: Appropriate data types for each field
- **Constraints**: Primary keys, unique constraints, and NOT NULL where appropriate

### Python Integration
- **Error Handling**: Comprehensive error handling for database operations
- **Connection Management**: Proper opening and closing of database connections
- **User Feedback**: Clear success and error messages

### SQL Best Practices
- **Uppercase Keywords**: All SQL keywords in uppercase
- **Consistent Naming**: Clear and consistent table and column naming
- **Comments**: Well-documented SQL scripts
- **Conditional Creation**: IF NOT EXISTS clauses to prevent errors

## 🔧 Advanced Features

### Data Integrity
- **Unique Email**: Customers must have unique email addresses
- **Cascade Operations**: Proper handling of related data deletion/updates
- **Default Values**: Sensible defaults for quantity fields

### Scalability
- **AUTO_INCREMENT**: Primary keys automatically generated
- **Indexed Foreign Keys**: Efficient querying of related data
- **Flexible Data Types**: TEXT for addresses, DOUBLE for prices and quantities

## 🚦 Usage Examples

### Query Examples

```sql
-- Get all books by a specific author
SELECT b.title, b.price, a.author_name 
FROM books b 
JOIN authors a ON b.author_id = a.author_id 
WHERE a.author_name = 'Author Name';

-- Get customer order history
SELECT c.customer_name, o.order_date, b.title, od.quantity
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN books b ON od.book_id = b.book_id
WHERE c.customer_id = 1;

-- Get total sales by book
SELECT b.title, SUM(od.quantity * b.price) as total_sales
FROM books b
JOIN order_details od ON b.book_id = od.book_id
GROUP BY b.book_id, b.title;
```

## 🔍 Testing

### Verification Steps

1. **Database Creation**:
```sql
SHOW DATABASES LIKE 'alx_book_store';
```

2. **Table Creation**:
```sql
USE alx_book_store;
SHOW TABLES;
```

3. **Data Insertion**:
```sql
SELECT COUNT(*) FROM customers;
SELECT * FROM customers;
```

4. **Foreign Key Constraints**:
```sql
SHOW CREATE TABLE books;
SHOW CREATE TABLE orders;
SHOW CREATE TABLE order_details;
```

## 📈 Future Enhancements

- **Inventory Management**: Track book stock levels
- **Order Status**: Add order status tracking
- **Categories**: Book categorization system
- **Reviews**: Customer review system
- **Discounts**: Pricing and discount management
- **Shipping**: Shipping address and tracking

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is part of the ALX Software Engineering Program.

## 🎉 Acknowledgments

- ALX Software Engineering Program
- MySQL Documentation
- Python mysql-connector documentation

---

**Status**: ✅ Complete MySQL database implementation for online bookstore ready for evaluation!
