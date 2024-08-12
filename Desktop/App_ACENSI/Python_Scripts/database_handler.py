import pypyodbc 


DRIVER_NAME = 'SQL SERVER'
SERVER = 'FR-LTP-0577\SQLEXPRESS'
DATABASE = 'AdventureWorks2019'


connection_string = f"""
DRIVER={DRIVER_NAME};
SERVER={SERVER};  # Add missing closing quotation mark
DATABASE={DATABASE};
Trust_Connected=yes;
"""

