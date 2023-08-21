# DataSerpent 🐍

A lightweight flat-file database system built in Python.

## Features

- Create tables with custom columns and types.
- Insert records into tables.
- Query records with optional criteria.
- Delete records based on criteria.
- Simple Command Line Interface (CLI) for database operations.

## Requirements

- Python 3.x
- tkinter (for future GUI features)

## Quickstart

1. Clone the repository:

```bash
git clone https://github.com/Gojibodev/dataSerpent.git
cd DataSerpent
```

2. Run the program:

```bash
python data_serpent.py
```

3. Follow the on-screen instructions in the CLI.

## How To Use

When prompted by the CLI:

- **Create Table**: Provide a table name and columns in the format `name:type,name:type,...`.
  
  Example: `users name:string,age:int`

- **Insert Record**: Provide a table name and a record in the format `name=value,name=value,...`.
  
  Example: `users name=Alice,age=29`

- **Query Records**: Provide a table name and optionally a criteria in the format `name=value,name=value,...`. Leave blank for querying all records.
  
  Example: `users name=Alice`

- **Delete Records**: Provide a table name and a criteria in the format `name=value,name=value,...`.
  
  Example: `users age=29`

## Future Enhancements
- Indexes: For larger data sets, introducing a basic indexing system can speed up querying significantly.
- Import / Export of different file types instead of just .csv / .txt
- Data encryption
- GUI support for more user-friendly operations.
- Enhancements in querying capabilities like using logical operators.
- Backup and restore or logging capabilities

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change. Make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

[Gojibodev(me)](https://github.com/Gojibodev/)
