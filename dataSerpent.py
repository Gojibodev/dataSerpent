import os

# File extension for our tables
FILE_EXTENSION = ".csv"

def create_table(table_name, columns):
    """
    Create a new table with the specified name and columns.
    
    Args:
    - table_name (str): Name of the table.
    - columns (dict): Dictionary with column names as keys and data types as values.
    """
    # Create a header from the columns
    header = ",".join([f"{col_name}:{col_type}" for col_name, col_type in columns.items()])
    
    # Write the header to a new file
    with open(table_name + FILE_EXTENSION, 'w') as file:
        file.write(header + "\n")

def insert(table_name, record):
    """
    Insert a new record into the specified table.
    
    Args:
    - table_name (str): Name of the table.
    - record (dict): Dictionary with column names as keys and values to be inserted.
    """
    # Convert the record to a comma-separated string
    record_str = ",".join([str(value) for value in record.values()])
    
    # Append the record to the table file
    with open(table_name + FILE_EXTENSION, 'a') as file:
        file.write(record_str + "\n")

def query(table_name, criteria=None):
    """
    Query records from the specified table based on some criteria.
    
    Args:
    - table_name (str): Name of the table.
    - criteria (dict, optional): Dictionary with column names as keys and values to be matched.
    
    Returns:
    - List of records that match the criteria.
    """
    records = []
    
    with open(table_name + FILE_EXTENSION, 'r') as file:
        # Read the header to get column names and types
        header = file.readline().strip().split(',')
        columns = {col.split(':')[0]: col.split(':')[1] for col in header}
        
        # Read and filter records
        for line in file:
            values = line.strip().split(',')
            record = {col: (int(values[i]) if columns[col] == "int" else values[i]) for i, col in enumerate(columns)}
            
            if not criteria or all(record[col] == value for col, value in criteria.items()):
                records.append(record)
    
    return records

def delete(table_name, criteria):
    """
    Delete records from the specified table based on some criteria.
    
    Args:
    - table_name (str): Name of the table.
    - criteria (dict): Dictionary with column names as keys and values to be matched.
    """
    # Store the records we want to keep
    records_to_keep = []
    
    with open(table_name + FILE_EXTENSION, 'r') as file:
        # Read the header to get column names and types
        header = file.readline().strip()
        columns = {col.split(':')[0]: col.split(':')[1] for col in header.split(',')}
        
        # Read and filter records
        for line in file:
            values = line.strip().split(',')
            record = {col: (int(values[i]) if columns[col] == "int" else values[i]) for i, col in enumerate(columns)}
            
            if not all(record[col] == value for col, value in criteria.items()):
                records_to_keep.append(line.strip())
    
    # Rewrite the table file without the deleted records
    with open(table_name + FILE_EXTENSION, 'w') as file:
        file.write(header + "\n")
        file.write("\n".join(records_to_keep))

# Tests
create_table("users", {"name": "string", "age": "int"})
insert("users", {"name": "Alice", "age": 29})
insert("users", {"name": "Bob", "age": 30})


def cli_program():
    while True:
        # Display the main menu
        print("\nSimple DBMS CLI")
        print("1. Create Table")
        print("2. Insert Record")
        print("3. Query Records")
        print("4. Delete Records")
        print("5. Exit")
        
        # Get user choice
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            # Create Table
            table_name = input("Enter table name: ")
            columns_input = input("Enter columns (format: name:type,name:type,...): ")
            columns = {col.split(':')[0]: col.split(':')[1] for col in columns_input.split(',')}
            create_table(table_name, columns)
            print(f"Table '{table_name}' created successfully!")
        
        elif choice == "2":
            # Insert Record
            table_name = input("Enter table name: ")
            record_input = input("Enter record (format: name=value,name=value,...): ")
            record = {col.split('=')[0]: (int(col.split('=')[1]) if '=' in col and col.split('=')[1].isdigit() else col.split('=')[1]) for col in record_input.split(',')}
            insert(table_name, record)
            print(f"Record inserted into '{table_name}' successfully!")
        
        elif choice == "3":
            # Query Records
            table_name = input("Enter table name: ")
            criteria_input = input("Enter query criteria (format: name=value,name=value,... or leave blank for all records): ")
            criteria = {col.split('=')[0]: (int(col.split('=')[1]) if '=' in col and col.split('=')[1].isdigit() else col.split('=')[1]) for col in criteria_input.split(',')} if criteria_input else None
            records = query(table_name, criteria)
            print("\nQueried Records:")
            for record in records:
                print(record)
        
        elif choice == "4":
            # Delete Records
            table_name = input("Enter table name: ")
            criteria_input = input("Enter delete criteria (format: name=value,name=value,...): ")
            criteria = {col.split('=')[0]: (int(col.split('=')[1]) if '=' in col and col.split('=')[1].isdigit() else col.split('=')[1]) for col in criteria_input.split(',')}
            delete(table_name, criteria)
            print(f"Records matching criteria deleted from '{table_name}' successfully!")
        
        elif choice == "5":
            # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

#Main loop
cli_program()
